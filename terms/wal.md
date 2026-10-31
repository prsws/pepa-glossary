---
term: "WAL"
expansion: "write-ahead queue"
category: "pipeline and runtime"
status: "current"
aliases: []
summary: "Append-only JSONL on mmm4 where extraction output and explicit-user writes land first, draining to canonical when reachable."
sources: []
---

## Definition

Append-only JSONL on mmm4 where extraction output and explicit-user writes land first, draining to canonical when reachable. At-least-once delivery → canonical intake must be idempotent.

## History

- 2026-09-04: Recorded in Glossary v0.1, section 5.
