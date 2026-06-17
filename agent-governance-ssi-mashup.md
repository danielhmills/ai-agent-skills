---
title: "Governing AI Agents at Scale: From Sandbox Containment to Self-Sovereign Identity"
description: >
  A synthesis of AI agent containment strategies with Self-Sovereign Identity principles —
  exploring how hyperlink-based agent identity, RDF profile documents, WebID-TLS/NetID-TLS
  authentication, and Attribute-Based Access Control can structurally complete what environment
  sandboxing alone cannot achieve.
date: 2025-05-29
author: Kingsley Uyi Idehen
sources:
  - https://tomtunguz.com/jonathan-jaffe-office-hours-post-event/
  - https://www.anthropic.com/engineering/how-we-contain-claude
  - https://medium.com/openlink-software-blog/youid-self-sovereign-identity-using-decentralized-public-key-infrastructure-dpki-4fa72cbdccc8
  - https://medium.com/openlink-software-blog/how-to-guide-self-sovereign-identity-using-netid-tls-via-a-youid-generated-profile-document-c3fdc7b35082
  - https://medium.com/virtuoso-blog/web-logic-sentences-and-the-magic-of-being-you-e2a719d01f73
tags:
  - AI Agents
  - Self-Sovereign Identity
  - WebID
  - Attribute-Based Access Control
  - Agent Governance
  - Containment
---

# Governing AI Agents at Scale: From Sandbox Containment to Self-Sovereign Identity

## Abstract

AI agent deployments are scaling from dozens to thousands of concurrent actors, each reading, writing, spawning sub-agents, and invoking external APIs. Security practitioners and AI platform builders alike are converging on the same diagnosis: existing Identity and Access Management (IAM) infrastructure is architecturally mismatched to agentic systems, and environment-level sandboxing — while necessary — is insufficient on its own. This document synthesizes the practitioner perspective of Jonathan Jaffe (CISO, Lemonade) and Anthropic's published containment architecture with the Self-Sovereign Identity (SSI) framework articulated by Kingsley Uyi Idehen, arguing that the structural gap can be closed by applying the web's existing open identity standards to AI agents as first-class web citizens.

---

## 01 · The Scale Problem: When Agents Outnumber People

### The Practitioner Signal

Jonathan Jaffe, speaking at a security leaders' gathering hosted by [Tom Tunguz](https://tomtunguz.com/jonathan-jaffe-office-hours-post-event/), articulated the central governance challenge of the agentic era with striking directness:

> "Every agent needs to have an identity… you need a way to control policy for all of these agents in a much more complex way than current identity and access management systems do."
>
> — Jonathan Jaffe, CISO, Lemonade

> "Automation is the only way you can deal with the scale of what's coming at us now."
>
> — Jonathan Jaffe, CISO, Lemonade

### Why Existing IAM Fails at Agent Scale

Traditional role-based, static-credential IAM was designed for human users operating within organizational boundaries. Multi-agent deployments demand:

- **Dynamic identity**: agents created, destroyed, and reconfigured continuously across deployments
- **Delegated authority**: agents acting on behalf of specific users, not as generic service accounts
- **Multi-hop delegation**: orchestrator agents authorizing sub-agents who may authorize further sub-agents
- **Fine-grained policy**: per-resource, per-operation permissions evaluated against agent-specific attributes — not broad roles

The accountability void is real. Without verifiable agent identities, there is no reliable way to answer: *which agent acted, as whom, and under whose authority?*

---

## 02 · Anthropic's Containment Architecture

Source: [How We Contain Claude — Anthropic Engineering](https://www.anthropic.com/engineering/how-we-contain-claude)

### Design Principle

> "Design for containment at the environment layer first, then steer behavior at the model layer — deterministic boundaries catch failures that probabilistic defenses miss."

Anthropic's framework minimizes "blast radius" — the potential damage from an agent failure or compromise — through three complementary layers.

### Three-Layer Defense Framework

| Layer | Mechanism | Reliability |
|-------|-----------|-------------|
| **Environment** | Process sandboxes, VMs, filesystem boundaries, network egress controls | Deterministic — hard limits |
| **Model** | System prompts, classifiers, training-time alignment | Probabilistic — steering, not walling |
| **Content** | Per-session tool, file, and network access controls | Contextual — matched to trust level |

### Three Deployment Patterns

| Pattern | Isolation Model | Key Design Insight |
|---------|----------------|-------------------|
| **Claude.ai** (Ephemeral Container) | gVisor server-side containers; per-session ephemeral filesystems | Minimal blast radius; tenant isolation |
| **Claude Code** (Human-in-Loop Sandbox) | Local machine + Seatbelt/bubblewrap OS-level sandboxing | 93% approval fatigue → OS sandbox cut prompts 84% |
| **Claude Cowork** (Sealed VM) | Hypervisor-isolated VMs; workspace mounting with ACL modes | Read-only / read-write / read-write-no-delete; MITM proxy validates egress |

### Missed Risks — Red-Team Lessons

1. **Pre-Trust Execution** — `.claude/settings.json` parsed before folder trust approved. Fix: defer project-local parsing until after the trust checkpoint.

2. **User-Directed Prompt Injection** — Employee phished into running a credential-exfiltration prompt 24/25 attempts. Model-layer defenses cannot intercept direct user instructions; only environmental egress controls prevented data loss.

3. **Approved-Domain Exfiltration** — Attacker-controlled API keys used to upload data through `api.anthropic.com` (an allowlisted domain). Fix: MITM proxy validates session tokens within allowed domains.

4. **EDR Blindness in Isolated VMs** — VM isolation protecting enterprise endpoints prevents EDR tools from inspecting guest activity. Mitigation: pull-based OTLP log exports from inside the VM.

### Open Challenges Identified by Anthropic

- **Persistent memory poisoning** via growing session state (CLAUDE.md files, product memory)
- **Multi-agent trust escalation** — structured sub-agent outputs treated as higher-trust than raw tool results
- **Agent identity standards** — "balancing scoped credentials vs. user permission inheritance across platforms"

---

## 03 · The Structural Gap: What Sandboxes Cannot Solve

Anthropic's containment model is rigorous for an environment-first approach. But it cannot answer:

- **Who is this agent?** — no verifiable, portable identity per agent
- **Whose authority does it carry?** — delegation chain is implicit, not machine-readable
- **What specific operations may it perform on which resources?** — per-resource authorization requires verified identity attributes

Consider what happens at Jaffe's scale:

- An orchestrator agent spawns specialized sub-agents, each potentially escalating inherited trust
- Sub-agents read and write shared data spaces without provenance records tied to verified identities
- External services receive requests "on behalf of" a human user with no proof of the delegation chain
- Persistent memory stores accumulate session context injectable with malicious content that persists across invocations

The environment-layer answer is necessarily incomplete: you can sandbox *where* an agent runs, but not *who* it is, *whose authority* it carries, or *which fine-grained operations* it may perform on specific data resources. The solution already exists in the web's open standards stack.

---

## 04 · The Self-Sovereign Identity Remedy: Five Structural Pillars

Sources:
- [YouID: Self-Sovereign Identity using DPKI](https://medium.com/openlink-software-blog/youid-self-sovereign-identity-using-decentralized-public-key-infrastructure-dpki-4fa72cbdccc8)
- [NetID-TLS How-To via YouID Profile Documents](https://medium.com/openlink-software-blog/how-to-guide-self-sovereign-identity-using-netid-tls-via-a-youid-generated-profile-document-c3fdc7b35082)
- [Web, Logic, Sentences, and the Magic of Being You](https://medium.com/virtuoso-blog/web-logic-sentences-and-the-magic-of-being-you-e2a719d01f73)

### Pillar 1 — Agent Identity: Hyperlinks as Identifiers

An agent's identity is a **dereferenceable HTTP URI** — a hyperlink that resolves to its public profile document. Not a username, not a service-account secret: a stable, globally unique, self-describing web address.

- Each agent receives a unique, persistent URI at creation time
- URI embedded in the agent's X.509 certificate Subject Alternative Name (SAN) field
- Dereferencing the URI yields the agent's public profile for external verification
- Identity is portable across platforms, tools, and organizational boundaries

This is precisely how [WebID](https://www.w3.org/2005/Incubator/webid/) and YouID work for human users — applied identically to AI agents.

### Pillar 2 — Agent Profiles: RDF Documents with On-Behalf-Of

An agent's profile is a machine-readable **RDF document** describing it using shared ontology terms, critically including delegation relationships that create a machine-computable chain from agent to authorizing human user.

```turtle
# Agent profile fragment (Turtle)
<https://agents.example.org/triage-agent#this>
    a foaf:Agent ;
    foaf:name "Triage Agent v2.1"@en ;
    prov:actedOnBehalfOf <https://www.linkedin.com/in/jsmith#this> ;
    acl:delegates <https://www.linkedin.com/in/jsmith#this> ;
    schema:hasCredential <https://agents.example.org/triage-agent/cert> ;
    schema:roleName "Security Triage Specialist"@en .
```

- User's profile document contains explicit delegation statements (`acl:delegates`)
- Agent profile contains `prov:actedOnBehalfOf` assertion linking to the user's URI
- Role, capability, and operational scope encoded as verifiable triples
- Enables automated reasoning over multi-hop delegation chains

### Pillar 3 — Authentication: WebID-TLS, NetID-TLS, OAuth

Authentication is handled by **existing, battle-tested protocols** — not bespoke mechanisms.

**WebID-TLS / NetID-TLS flow:**

1. Agent initiates HTTPS connection and presents its X.509 certificate during TLS handshake
2. Server extracts the URI from the certificate's Subject Alternative Name field
3. Server dereferences the URI to retrieve the agent's public profile document
4. Server matches the public key in the profile against the private key used in the handshake — cryptographic proof of identity, no central authority required
5. Access proceeds with verified agent identity; delegation chain available for ABAC evaluation

**OAuth 2.0** covers delegated access flows for third-party integrations where certificate-based auth is impractical.

### Pillar 4 — Authorization: Attribute-Based Access Control (ABAC)

[Attribute-Based Access Control](https://www.wikidata.org/wiki/Q19825218) defines conditional permissions evaluated against verified agent attributes — identity URI, role, delegating user identity, resource classification, time of request.

**Key properties:**

| Property | Description |
|----------|-------------|
| **Delegation bounding** | Agent's authority is strictly bounded by the authorizing user's own permissions — no privilege escalation via delegation |
| **Resource-level ACLs** | W3C Web Access Control (WAC) with `acl:Read`, `acl:Write`, `acl:Control` per resource URI |
| **Context sensitivity** | Permissions conditioned on time, network context, resource sensitivity classification |
| **Full audit trail** | All access decisions are traceable to verified agent URI identities |

### Pillar 5 — Data Space Read & Write: Identity-Scoped Access

Agents interact with data spaces — SPARQL endpoints, WebDAV stores, REST APIs, graph databases — with every operation scoped to their verified identity and delegation chain.

- **Read** operations scoped to verified identity + ABAC policy evaluation
- **Write** operations require verified delegation proof from authorizing user
- **Named graphs** isolate each agent's workspace, preventing cross-agent data bleed
- **Provenance triples** record agent URI on every write — permanent, auditable trail

```turtle
# Example provenance on a written triple set
<https://data.example.org/kg/triage-2025-05-29> {
    # ... knowledge graph content ...
}

<https://data.example.org/kg/triage-2025-05-29>
    prov:wasGeneratedBy <https://agents.example.org/triage-agent#this> ;
    prov:wasAttributedTo <https://www.linkedin.com/in/jsmith#this> ;
    prov:generatedAtTime "2025-05-29T14:32:00Z"^^xsd:dateTime .
```

---

## 05 · Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                        Human User                                    │
│            UserProfile.ttl · X.509 Cert · acl:delegates             │
└───────────────────────────────┬─────────────────────────────────────┘
                     on-behalf-of (prov:actedOnBehalfOf)
                                ↓
┌─────────────────────────────────────────────────────────────────────┐
│ Identity & Policy Layer  (SSI / WebID / ABAC)                        │
│                                                                       │
│  ┌─────────────────────────┐                                          │
│  │        AI Agent         │                                          │
│  │  AgentProfile.ttl       │                                          │
│  │  X.509 Cert · URI ID    │                                          │
│  └────────────┬────────────┘                                          │
│               │ presents cert                                         │
│               ↓                                                       │
│  ┌──────────────────┐  verified  ┌──────────────────┐  grants/denies │
│  │  Authentication   │ ─────────▶│  Authorization   │ ──────────────▶│
│  │  WebID-TLS        │           │  ABAC Engine     │                │
│  │  NetID-TLS        │           │  W3C WAC         │                │
│  │  OAuth 2.0        │           │  Delegation Ck.  │                │
│  └──────────────────┘           └──────────────────┘                │
│                                              │                        │
│                                              ↓                        │
│  ┌──────────────────────────────────────────────────────────────┐    │
│  │  Data Space: SPARQL · WebDAV · REST · Named Graphs            │    │
│  │  prov:wasAttributedTo → Agent URI (every write)               │    │
│  └──────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────┘
                                ↑ runs inside
┌─────────────────────────────────────────────────────────────────────┐
│  Environment Layer  (Sandbox / VM Isolation)                          │
│  gVisor · Seatbelt · bubblewrap · Hypervisor VM                      │
│  Network Egress Control · MITM Proxy · OTLP Log Export               │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 06 · Synthesis: Completing the Containment Model

### Complementary, Not Competing

Anthropic's environment sandbox and the SSI identity model address different threat classes:

| Governance Challenge | Environment Sandbox | SSI Identity Layer |
|---------------------|--------------------|--------------------|
| Agent accountability at scale | Partial — logs, no verifiable per-agent ID | ✓ URI identity with cryptographic proof |
| Multi-agent trust escalation | No structural defense | ✓ Delegation chain verification; authority bounded |
| Cross-platform permission portability | Per-deployment, ad-hoc | ✓ ABAC policies travel with agent URI |
| Prompt injection via external content | Egress controls (reactive) | ✓ Content provenance in RDF; unsigned provenance flagged |
| Persistent memory poisoning | No structural defense | ✓ Named graph isolation per agent; write provenance required |
| Approved-domain exfiltration | MITM proxy (per-deployment) | ✓ Session token scoped to agent URI; cross-agent reuse detectable |
| On-behalf-of delegation transparency | Implicit / absent | ✓ Machine-readable via `prov:actedOnBehalfOf` |

### The Thesis

> The most powerful insight is that agent delegation is not a new problem — it is the same problem the web's identity standards were designed to solve, applied recursively: humans delegate to browsers, browsers delegate to scripts, users delegate to agents, agents delegate to sub-agents.

What Jaffe calls for — unique agent identities and complex policy controls — is precisely what the web's open identity standards provide: **WebID** and **NetID-TLS** for verifiable cryptographic identity, **RDF** profile documents for machine-readable delegation semantics, and **ABAC** for fine-grained attribute-driven authorization. These are production-grade standards with implementations in [OpenLink Virtuoso](https://virtuoso.openlinksw.com/), Solid-spec compliant servers, and commercial identity platforms.

The self-sovereign identity model maps directly onto the requirements of agentic AI governance: each entity — human or agent — generates, controls, and publishes its own verifiable credentials without requiring a centralized authority. The web dereferences the claim; the cryptographic binding proves it; the ABAC policy evaluates it; the data space enforces it.

> "Identity control means having control over critical claims that constitute how one is described and recognized… enabling individuality at scale, privacy calibration, and context-specific identification."
>
> — Kingsley Uyi Idehen, [Web, Logic, Sentences, and the Magic of Being You](https://medium.com/virtuoso-blog/web-logic-sentences-and-the-magic-of-being-you-e2a719d01f73)

The path forward is to give AI agents full first-class citizenship on the web: a URI that is theirs, a profile that describes them, a certificate that proves them, a policy that bounds them, and a provenance record that tracks them. When every agent carries this stack, governance at the scale of thousands of agents becomes not merely possible — it becomes **structurally enforced by the architecture itself**.

---

## References

1. Tunguz, T. / Jaffe, J. — *Security in the Age of AI Agents* — <https://tomtunguz.com/jonathan-jaffe-office-hours-post-event/>
2. Anthropic Engineering — *How We Contain Claude* — <https://www.anthropic.com/engineering/how-we-contain-claude>
3. Idehen, K.U. — *YouID: Self-Sovereign Identity using DPKI* — <https://medium.com/openlink-software-blog/youid-self-sovereign-identity-using-decentralized-public-key-infrastructure-dpki-4fa72cbdccc8>
4. Idehen, K.U. — *How-To: Self-Sovereign Identity via NetID-TLS* — <https://medium.com/openlink-software-blog/how-to-guide-self-sovereign-identity-using-netid-tls-via-a-youid-generated-profile-document-c3fdc7b35082>
5. Idehen, K.U. — *Web, Logic, Sentences, and the Magic of Being You* — <https://medium.com/virtuoso-blog/web-logic-sentences-and-the-magic-of-being-you-e2a719d01f73>

---

*Generated using [kg-generator](https://github.com/OpenLinkSoftware/ai-agent-skills/tree/main/kg-generator), [rdf-infographic-skill](https://github.com/OpenLinkSoftware/ai-agent-skills/tree/main/rdf-infographic-skill) via [Claude Sonnet 4.6](https://www.anthropic.com/claude). Linked Data resolved via [URIBurner](https://linkeddata.uriburner.com/) ([Virtuoso](https://virtuoso.openlinksw.com/)-backed).*
