---
term: "Pepa Human Sentinel Arm"
expansion: "Pepa Human Sentinel Arm"
category: "arm"
status: "current"
aliases: ["PHSA", "Human Sentinel Arm"]
summary: "The arm that watches the person's health signals; it never diagnoses, prescribes or escalates on its own."
supersedes: "doctor-arm"
sources: ["Sensory Arm page on ai4aging.org", "project chat 2026-09-26"]
---

## Definition

Watches the human, not the house. It reads what the Sensory Arm collected (its "human scope") and does not collect anything itself. It starts with a recorder: a store that keeps the person's health records at hand so a doctor visit needs nothing but a phone.

## History

- 2026-09-26: Named, replacing "Doctor Arm".
- 2026-09-29: Decided to start with the recorder, documents first, medications soon after.
- 2026-10-07: Recorder version 2 decided as a separate microservice that holds the records and their rules and nothing else.
- 2026-10-27: Published position: the Sentinel consumes what the Sensory Arm gathered. It does not gather.
