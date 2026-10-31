---
term: "Borrowed-client bug"
category: "failure mode"
status: "current"
aliases: []
summary: "The memory manager parasitizing VectorDBManager's ChromaDB client, so switching Context Mode to Direct silently killed memory vector search, Chroma sync, and dedup."
sources: []
---

## Definition

The memory manager parasitizing VectorDBManager's ChromaDB client, so switching Context Mode to Direct silently killed memory vector search, Chroma sync, and dedup. Killed by the client factory.

## History

- 2026-09-04: Recorded in Glossary v0.1, section 3.
