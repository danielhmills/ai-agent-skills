#!/usr/bin/env python3
"""
YouID Template Filler
Replicates the TplPrep logic from the YouID browser extension's uploader.js.

Template syntax:
  %{key}       — Simple substitution (replaced with value, error if key missing in remaining content)
  !{key}       — Conditional line: entire line is removed if key is empty/unset
  !!{key}      — Conditional block start: text until !!.
  !!{key}...   — Prefix variant: !!{key}<line> means line is conditional on key
  !!.<newline> — Conditional block end

Usage:
  python3 template_fill.py <template_file> <data_json> [output_file]
  echo '{"key":"val"}' | python3 template_fill.py <template_file> -
  (reads data JSON from stdin when arg is -)
"""

import json
import re
import sys


def parse_data(data_str):
    return json.loads(data_str)


def is_set(val):
    if val is None:
        return False
    s = str(val)
    return len(s) > 0


def process_conditional_blocks(lines, data):
    """Handle !!{key} ... !! . conditional blocks."""
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.lstrip()
        # Check for conditional block start: !!{key}
        m = re.match(r'^(\s*)!!\{(\w+)\}\s*$', line)
        if m:
            indent = m.group(1)
            key = m.group(2)
            # Find the matching !!.
            block_lines = []
            i += 1
            found_end = False
            while i < len(lines):
                end_stripped = lines[i].lstrip()
                if end_stripped.startswith('!!.'):
                    i += 1
                    found_end = True
                    break
                block_lines.append(lines[i])
                i += 1
            if is_set(data.get(key)):
                result.extend(block_lines)
            continue
        # Check for !!{key} prefix (line is conditional but content follows on same line)
        m2 = re.match(r'^(\s*)!!\{(\w+)\}(.*)$', line)
        if m2:
            indent = m2.group(1)
            key = m2.group(2)
            rest = m2.group(3)
            if is_set(data.get(key)):
                result.append(indent + rest + '\n')
            i += 1
            continue
        result.append(line)
        i += 1
    return result


def process_conditional_lines(lines, data):
    """Handle !{key} conditional lines."""
    result = []
    for line in lines:
        # Check for !{key} anywhere on the line
        # The whole line is conditional on this key
        if re.search(r'!\{(\w+)\}', line):
            # Check if ALL !{key} conditions in this line are satisfied
            def check_condition(m):
                key = m.group(1)
                return '' if not is_set(data.get(key)) else m.group(0)

            # Test by looking for any unsatisfied condition
            new_line = line
            all_satisfied = True
            for m in re.finditer(r'!\{(\w+)\}', line):
                key = m.group(1)
                if not is_set(data.get(key)):
                    all_satisfied = False
                    break
            if all_satisfied:
                # Strip all !{key} markers from the line
                new_line = re.sub(r'!\{(\w+)\}', '', line)
                result.append(new_line)
            # else: entire line is removed
        else:
            result.append(line)
    return result


def substitute_values(lines, data):
    """Handle %{key} substitution."""
    result = []
    for line in lines:
        def replacer(m):
            key = m.group(1)
            if key not in data:
                raise ValueError(f"Missing required template variable: {key}")
            val = data[key]
            if val is None:
                raise ValueError(f"Template variable '{key}' is None (required but not set)")
            return str(val)
        new_line = re.sub(r'%\{(\w+)\}', replacer, line)
        result.append(new_line)
    return result


def fill_template(template_text, data):
    lines = template_text.splitlines(keepends=True)
    lines = process_conditional_blocks(lines, data)
    lines = process_conditional_lines(lines, data)
    lines = substitute_values(lines, data)
    return ''.join(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage: template_fill.py <template_file> <data_json> [output_file]", file=sys.stderr)
        sys.exit(1)

    template_file = sys.argv[1]
    data_source = sys.argv[2]
    output_file = sys.argv[3] if len(sys.argv) > 3 else None

    with open(template_file) as f:
        template_text = f.read()

    if data_source == '-':
        data_str = sys.stdin.read()
    else:
        with open(data_source) as f:
            data_str = f.read()

    data = parse_data(data_str)

    result = fill_template(template_text, data)

    if output_file:
        with open(output_file, 'w') as f:
            f.write(result)
    else:
        print(result, end='')

    # Report any unused data keys (helpful for debugging)
    used_keys = set()
    for m in re.finditer(r'%\{(\w+)\}', result):
        used_keys.add(m.group(1))
    unused = set(data.keys()) - used_keys
    if unused:
        pass  # Suppress for clean output
        # print(f"[note] unused variables: {', '.join(sorted(unused))}", file=sys.stderr)


if __name__ == '__main__':
    main()
