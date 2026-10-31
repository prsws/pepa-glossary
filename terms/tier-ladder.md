---
term: "Tier ladder"
category: "pipeline and runtime"
status: "current"
aliases: []
summary: "The routing hierarchy for utterances: canned-phrase speed match → HA-native intent → LLM (PSA)."
sources: []
---

## Definition

The routing hierarchy for utterances: canned-phrase speed match → HA-native intent → LLM (PSA). Tiers below the LLM are invisible to PSA, which is why utterance observability is a design problem. PAHA states it as a latency ladder: preprocessor hit (sub-100 ms) → single ReAct step → ReAct iteration → escalation.

## History

- 2026-09-04: Recorded in Glossary v0.1, section 5.
