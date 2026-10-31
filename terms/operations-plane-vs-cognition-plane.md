---
term: "Operations plane vs cognition plane"
category: "pipeline and runtime"
status: "current"
aliases: []
summary: "HA is the operations plane (no model in the loop, owns schedules); the LangGraph Head is the cognition plane (utterance-triggered, model in the loop)."
sources: []
---

## Definition

HA is the operations plane (no model in the loop, owns schedules); the LangGraph Head is the cognition plane (utterance-triggered, model in the loop). The Head must never own a schedule.

## History

- 2026-09-04: Recorded in Glossary v0.1, section 5.
