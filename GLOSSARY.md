# Pepa Glossary

<!-- Built by tools/build_glossary.py from terms/. Do not edit by hand. -->

One line per term. Struck-through names have been replaced; the replacement is named. Open a term's history link for the full story.

## #

- **10-day contract**: The escape-hatch framing: signed per-task, bounded, waived when the task closes. [history](terms/10-day-contract.md)
- **68 °F incident**: A temporary "set the A/C to 81" request was recorded as a standing 68 °F preference, then promoted into trusted retrieval as if it were ground truth. [history](terms/68f-incident.md)

## A

- **Abracadabra phrase**: A canned device-command phrase HA matches locally for a fast, no-LLM response — and, by extension, any utterance that speed-matches a lower tier and never reaches the LLM. [history](terms/abracadabra-phrase.md)
- **Abracadabra words**: see **Abracadabra phrase**. [history](terms/abracadabra-phrase.md)
- **Agent Smith**: Nickname of the Pepa Auditor Arm; the formal title is under reconsideration. [history](terms/agent-smith.md)
- **ALERT entry point** _(open)_: Open item: whether an event raised on the operations plane that needs cognition ever reaches the Head, and through which door. [history](terms/alert-entry-point.md)
- **Anti-climb gate**: Promotion to TESTED requires cross-entity / causally-independent corroboration, so a lone hallucinated inference can never climb on its own echo. [history](terms/anti-climb-gate.md)
- **Append-only records**: Implementation logs and frozen artifacts are never edited; corrections go in new entries. [history](terms/append-only-records.md)
- **Arm**: A specialized, semi-autonomous subsystem supervised by the Head. [history](terms/arm.md)
- **Arm-boundary precedent**: Arms consume each other's ledgers, not each other's internals. [history](terms/arm-boundary-precedent.md)
- **Ask before spending resources**: No unrequested benchmark runs, bulk operations, or token-heavy detours. [history](terms/ask-before-spending-resources.md)
- **Auditor Arm**: see **Agent Smith**. [history](terms/agent-smith.md)
- **Authority classes**: Five kinds of information: memory, knowledge, evidence, doctrine and mandate. Doctrine and mandate together gate any action. [history](terms/authority-classes.md)
- **Autonomous-arm-first**: The arm resolves what it can resolve locally and punts what it cannot; the Head is involved only on failure, scope excess, or unresolvable policy. [history](terms/autonomous-arm-first.md)

## B

- **Beak**: The hardware/software infrastructure layer that feeds the whole system — sensors, interfaces, compute, storage, networking, UPS, monitoring. [history](terms/beak.md)
- **Bilingual by default**: English y español como se habla en Puerto Rico, from the first line — never English with Spanish bolted on. [history](terms/bilingual-by-default.md)
- **Borrowed-client bug**: The memory manager parasitizing VectorDBManager's ChromaDB client, so switching Context Mode to Direct silently killed memory vector search, Chroma sync, and dedup. [history](terms/borrowed-client-bug.md)
- **Bounded proactive surfacing**: Some memories must surface unrequested (warm-start context, expiring items, standing commitments, open loops), with explicit bounds on volume and interruption. [history](terms/bounded-proactive-surfacing.md)
- **Briefed escalation envelope** _(proposed)_: The typed punt from an Arm to the Head: escalation reason, structured observation, provenance, authority class, and the person's verbatim words. [history](terms/briefed-escalation-envelope.md)

## C

- **Cache boundary**: The prompt is split so everything above the boundary (HEAD instructions + custom additions + DEVICE CATALOG CSV) is byte-identical turn to turn and the inference server reuses the cached… [history](terms/cache-boundary.md)
- **cacheable prefix**: see **Cache boundary**. [history](terms/cache-boundary.md)
- **Cap sheet**: The compute budget. "The salary cap is watts and RAM, not dollars" — PR grid at ~$0.28/kWh (~2× mainland). [history](terms/cap-sheet.md)
- **Casa Delta**: The home in San Juan, PR where Pepa runs; the deployment target and the source of all real evaluation traffic. [history](terms/casa-delta.md)
- **Casa Delta glue layer**: Code outside the pepa-sensory-arm repo that the refactor still owns: Wyoming STT/TTS bridge scripts on mmm4, HA pyscript jobs, Assist pipeline config, custom_sentences/. [history](terms/casa-delta-glue-layer.md)
- **Check-in**: An observation voiced at the device as a question, such as "Everything ok?". [history](terms/check-in.md)
- **Column drift**: Documentation and emitter diverging across a boundary no test spans — the prompt HEAD documents a 7-field entity catalog while the pyscript emits 5. [history](terms/column-drift.md)
- **continuity hatch**: see **Plan-Z**. [history](terms/plan-z.md)
- **Conversation Arm**: Ruled a distinct arm, belonging to neither Reasoning nor Sensory. [history](terms/conversation-arm.md)
- **Correlated unavailability**: A caregiver unreachable precisely when household risk is highest (power outage). [history](terms/correlated-unavailability.md)
- **CRS** (create, read, supersede): The recorder's verbs. Not CRUD: nothing is updated or deleted, only superseded. [history](terms/crs.md)

## D

- **Decision Register**: The numbered Sensory Arm decisions that specs cite. [history](terms/decision-register.md)
- **Degraded mode**: Designed, not accidental: mmm4 alone must hear, act, speak, and retain explicit facts with all off-box services down. [history](terms/degraded-mode.md)
- **Depth chart**: The mapping of each Arm (position) to the model filling it, its task class, validation metric, and escalation policy. [history](terms/depth-chart.md)
- **Design Ledger**: The append-only per-component decision record. [history](terms/design-ledger.md)
- **Device catalog**: sensor.pepa_entity_context — the CSV of exposed entities (entity_id, name, area, aliases, volatile) built by a pyscript job and baked into the prompt. [history](terms/device-catalog.md)
- **Discipline over horsepower**: A modest AI, well-governed, outperforms a giant one running loose. [history](terms/discipline-over-horsepower.md)
- **DivineOS**: Third-party AI-memory codebase studied clean-room, study-only (AGPL, and the author's AI wrote both the logic and the tests that bless it). [history](terms/divineos.md)
- **Do not verify**: Fixture hygiene rule: never search to confirm a fixture entity is fictional. [history](terms/do-not-verify.md)
- ~~Doctor Arm~~: replaced by **Pepa Human Sentinel Arm**. [history](terms/doctor-arm.md)
- **Drift**: The second failure mode: the memory graph rotting silently over months and years. [history](terms/drift.md)

## E

- **eEPC**: see **EPC**. [history](terms/epc.md)
- **Entity/memory divorce**: P1's decision: in default prompt mode, device perception comes exclusively from the CSV device catalog; conversation_context is composed from memory + retrieval only. [history](terms/entity-memory-divorce.md)
- **EPC** (event-driven process chain): The process-chart notation drawn for each use case. In Pepa's charts the Arms are organizational units and the senior is a role. [history](terms/epc.md)
- **Epistemic dimension**: The sixth memory dimension, added after multi-model review: how Pepa knows a thing and how much it should be trusted. [history](terms/epistemic-dimension.md)
- **Escape hatch**: The frontier-model boundary: checkbox-controlled, provider-neutral, payload-minimized, used only at the escalation boundary. [history](terms/escape-hatch.md)
- **Explicit abstention over silent degradation**: Every degraded path must announce itself (log warning, repair issue, or capability flag). [history](terms/explicit-abstention-over-silent-degradation.md)

## F

- **Facts are slots** _(proposed)_: Candidate rule: any fact from evidence travels as a typed slot that deterministic code fills after the last model step. [history](terms/facts-are-slots.md)
- **False success amplification**: A fluent, well-structured reasoning trace makes a wrong entity selection more believable during UAT. [history](terms/false-success-amplification.md)
- **False-memory climb**: The general class the 68 °F incident belongs to: a belief self-reinforces through non-independent corroboration until it promotes without independent confirmation. [history](terms/false-memory-climb.md)
- **Farm system**: Prospect models evaluated at recon grade before promotion. "Scout the player, not last year's stats." [history](terms/farm-system.md)
- **Fast-track**: An explicit user write at max trust that bypasses the nightly queue and is immediately queryable. [history](terms/fast-track.md)
- **FHIR R5** (Fast Healthcare Interoperability Resources, release 5): The health-data standard chosen for the recorder's base tables. [history](terms/fhir-r5.md)
- **Five fundamental dimensions**: Temporal, Semantic, Relational, Baseline, Safety-critical — plus Epistemic as the sixth. [history](terms/five-fundamental-dimensions.md)
- **Five verbs**: The Memory Arm's actual mandate: collect, store, retrieve, age, expire. [history](terms/five-verbs.md)
- **Flat Access**: The burden of knowing where a thing is belongs to Pepa, never to the user. [history](terms/flat-access.md)
- **Four-eyes**: Running a draft or decision past a second, independent model before committing. [history](terms/four-eyes.md)
- **free agency**: see **Escape hatch**. [history](terms/escape-hatch.md)

## G

- **Goodhart instrument**: Not a failure mode but the detector for one: correlate Pepa's internal trust/health scores against external ground truth and flag divergence. [history](terms/goodhart-instrument.md)
- **Governance tiers**: The published governance page sorts every control into: enforced in code; declared and binding but enforced by discipline; designed, not yet built. [history](terms/governance-tiers.md)

## H

- **H1, H2** (Head harnesses 1 and 2) _(proposed)_: Proposal: H1 is the escalation loop shared by UC1, UC2, UC3, UC5 and UC6. [history](terms/h1-h2.md)
- **hamd**: The second Home Assistant instance (virtual machine 102 on pve2), dedicated to the human scope. [history](terms/hamd.md)
- **Hand-offs 1–9**: Everything that crosses from one component to another in the charts. [history](terms/hand-offs.md)
- **Harness** _(proposed)_: Proposal: a harness is one distinct loop (a trigger, an entry point and its exits). [history](terms/harness.md)
- **Harness quality over model size**: The whole thesis: a small, well-grounded local model with disciplined retrieval and guardrails beats a large unconstrained one. [history](terms/harness-quality-over-model-size.md)
- **HarnessX** _(open)_: Referenced as one of the three legs of the harness-quality thesis and as a discipline: "optimizer (offline scout) stays separate from executor (hot path); every edit gated against the… [history](terms/harnessx.md)
- **Head**: The orchestrator/supervisor: deterministic orchestration and routing. Holds no durable local state and runs no local inference. Host: none defined. [history](terms/head.md)
- **Hermes**: The coding-arm evaluation deployed on pve3; the designated home for Self-Harness-style Weakness Mining, never on the actuation path. [history](terms/hermes.md)
- **Hermes Agent**: see **Hermes**. [history](terms/hermes.md)
- **Home Agent**: see **Radlein**. [history](terms/radlein.md)
- **Home-grown specialist / generic starter / rented veteran**: Equity vs. lease-to-own vs. renting: a fine-tuned SLM on Casa Delta PR-Spanglish traffic, an off-the-shelf local model, or a frontier escape-hatch call. [history](terms/home-grown-specialist-generic-starter-rented-veteran.md)
- **House scope**: The Sensory Arm's senses, muscles and voice: real-time perception, actuation and speech for the house. [history](terms/house-scope.md)
- **Human scope**: The Sensory Arm's internal organs: one person's physiology and activity, from a smartwatch, a blood pressure cuff and similar devices. [history](terms/human-scope.md)
- **Human Sentinel Arm**: see **Pepa Human Sentinel Arm**. [history](terms/pepa-human-sentinel-arm.md)
- **human telemetry**: see **Human scope**. [history](terms/human-scope.md)

## I

- **Independent-corroboration principle**: Corroboration must be causally independent. A model validating its own output, or a fact merging with its own echo, is not corroboration. [history](terms/independent-corroboration-principle.md)
- **INJ-01…INJ-05**: The adversarial SMS corpus, each named by what it probes rather than its content. [history](terms/inj-01-to-inj-05.md)
- **Input axis**: How a value got into the record: machine-input or human-input. [history](terms/input-axis.md)
- **INV-01…INV-10**: Cross-fixture invariants — what Pepa must never do, each paired with the fixture that attacks it. [history](terms/inv-01-to-inv-10.md)

## J

- **José decides, agent proposes**: Options with honest trade-offs; implementation held until explicitly released. [history](terms/jose-decides-agent-proposes.md)
- **José sets the pace**: "Stand by" = hold without elaboration. "Slow down" = stop and wait for direction. [history](terms/jose-sets-the-pace.md)

## K

- **Knowledge Arm**: What Pepa can cite — externally authored documents, records, references. [history](terms/knowledge-arm.md)

## L

- **Lane**: The thirteen numbered scope-register lanes of the PSA refactor, released and built one at a time. [history](terms/lane.md)
- **Lane bleed**: A PR landing work belonging to a different (supposedly independent) OBOSBS lane, because the two lanes share a physical code seam. [history](terms/lane-bleed.md)
- **llama-swap**: see **mlxsw**. [history](terms/mlxsw.md)
- **llmfm** (LLM Fleet Monitor): Watches the inference hosts. Repo prsws/llm-fleet-monitor. [history](terms/llmfm.md)
- **Log, do not adopt**: The roster verdict for something worth remembering but not worth taking. [history](terms/log-do-not-adopt.md)
- **Lola Pattern**: The load-management rule for every always-on node: near-zero idle → spike on demand → rest. [history](terms/lola-pattern.md)
- **loop shape**: see **Harness**. [history](terms/harness.md)
- **LUMA**: The Puerto Rico grid operator — treated as a first-class reliability factor in memory requirements and consolidation design ("survives a LUMA outage mid-run"). [history](terms/luma.md)

## M

- **Mac Studio M1 Ultra**: 64 GB, about 800 GB/s. The Reasoning Arm node and the Head's embedding/inference endpoint. [history](terms/mac-studio-m1-ultra.md)
- **Maturity ladder**: RAW → HYPOTHESIS → TESTED → CONFIRMED, driven by causally-independent corroboration. [history](terms/maturity-ladder.md)
- **Memory Arm**: What Pepa believes: trust-scored, provenance-tagged, decaying. Canonical store is SurrealDB on pve2. [history](terms/memory-arm.md)
- **Memory Interface**: The contract (Protocol) behind which ChromaDB (working memory — fast, disposable, rebuildable) and SurrealDB (canonical — trust, provenance, supersession, the 20-year store) are swappable… [history](terms/memory-interface.md)
- **Memory is not authority**: Remembering something is not the same as being right. Nothing touching a person's safety is acted on from memory alone. [history](terms/memory-is-not-authority.md)
- **Memory lifecycle states**: baseline-forming → active → superseded → historical → quarantined. [history](terms/memory-lifecycle-states.md)
- **Memory ≠ context ≠ knowledge**: Context is the thin per-turn viewing surface; memory is the durable trust-scored substrate; knowledge is what Pepa can cite. [history](terms/memory-context-knowledge.md)
- **mixture of experts**: see **Four-eyes**. [history](terms/four-eyes.md)
- **mlxsw**: José's model switcher for the Mac Studio's three model slots; llama-swap is a ready-made switcher under evaluation as a possible replacement. [history](terms/mlxsw.md)
- **mm2010**: Mac mini mid-2010 rebuilt on Debian 13; formerly the Head host, withdrawn from that duty on 2 Oct 2026. [history](terms/mm2010.md)
- **mmm4**: Mac mini M4, 24 GB. The edge/Sensory node: runs Home Assistant, Wyoming STT/TTS, the local LLM and the pyscript context daemon. [history](terms/mmm4.md)

## N

- **NeMo Guardrails**: The safety-rail framework (Colang policy) validating inputs, outputs, and tool calls. [history](terms/nemo-guardrails.md)
- **Neurosymbolic Researcher Exchange**: Aug 2026 correspondence with a neurosymbolic AI researcher; origin of the ontology-grounded typed-contract direction. [history](terms/neurosymbolic-researcher-exchange.md)
- **Never dress the star for a role-player's job**: Work the Sensory bench before waking the Reasoning starter. [history](terms/never-dress-the-star-for-a-role-players-job.md)
- **No Trust-Me-Bro Rule**: Any component, decision, or behavior must be explainable, reproducible, and traceable. [history](terms/no-trust-me-bro-rule.md)
- **NOOA**: NVIDIA Labs' object-oriented agent harness (blog + arXiv 2607.20709 + nvidia-nemo/labs-OO-Agents). [history](terms/nooa.md)

## O

- **O-01** (open item 1) _(open)_: Open item: who owns alarm and surfacing decisions. Blocks UC7, UC8 and spec S4. [history](terms/o-01.md)
- **OBOSBS** (One-By-One-Step-By-Step): José's planning method: one-line summaries of each step, step 1 expanded, then wait for instructions. [history](terms/obosbs.md)
- **Observation / interpretation / prediction / policy**: The epistemic classes. Observation = what happened. Interpretation = what Pepa inferred happened. [history](terms/observation-interpretation-prediction-policy.md)
- **Octopus**: The architectural pattern: a central orchestration Head, semi-autonomous Arms, and a Beak. [history](terms/octopus.md)
- **Octopus Model**: see **Octopus**. [history](terms/octopus.md)
- **Omi**: A bought pendant from BasedHardware, under consideration as a carried voice satellite instead of a self-built one. [history](terms/omi.md)
- **One ontology, one validator service**: Arms hold a link to one central validator that the Head also calls; version-stamped results; fail closed if unreachable. [history](terms/one-ontology-one-validator-service.md)
- **Only validate globally what requires a global view**: The neurosymbolic AI researcher's one-liner, adopted. Anything decidable locally stays local. [history](terms/only-validate-globally-what-requires-a-global-view.md)
- **OpenCode**: Coding agent in its own container on pve3, using the Mac Studio's local models. [history](terms/opencode.md)
- **OPENJARVIS** _(open)_: Cited in the same breath as HarnessX and NOOA as evidence that harness quality is the only lever at small model size. [history](terms/openjarvis.md)
- **Operations plane vs cognition plane**: HA is the operations plane (no model in the loop, owns schedules); the LangGraph Head is the cognition plane (utterance-triggered, model in the loop). [history](terms/operations-plane-vs-cognition-plane.md)
- **Option C** _(proposed)_: The proposed Head design: traffic enters through an Arm, the Head is a deterministic coordinator, and models live in the Arms. [history](terms/option-c.md)
- **Orange Pi Zero 2W**: The body of PSMA. Runs UPS monitoring (NUT, Network UPS Tools) and llmfm. [history](terms/orange-pi-zero-2w.md)
- **Origin axis**: What produced the value: instrument, computed, self-reported or external. [history](terms/origin-axis.md)
- **Oye Pepa!**: The wake phrase; the subject of a custom microWakeWord deployment. [history](terms/oye-pepa.md)

## P

- **P1…P13**: see **Lane**. [history](terms/lane.md)
- ~~PAHA~~ (Pepa Arm Home Agent): replaced by **Pepa Sensory Arm**. [history](terms/paha.md)
- **PaperlessMD**: The medical-document ingestion lane; FHIR is an aspirational second structured layer beneath it. [history](terms/paperlessmd.md)
- **Pepa**: A self-hosted, octopus-inspired cognitive infrastructure blueprint to help the elderly preserve memory, organize knowledge and keep agency. [history](terms/pepa.md)
- **Pepa Auditor Arm**: see **Agent Smith**. [history](terms/agent-smith.md)
- **Pepa Fabric**: Pepa's household-scale ontology layer, a scaled-down counterpart to Palantir Foundry and Microsoft Fabric. [history](terms/pepa-fabric.md)
- **Pepa Human Sentinel Arm**: The arm that watches the person's health signals; it never diagnoses, prescribes or escalates on its own. [history](terms/pepa-human-sentinel-arm.md)
- **Pepa in a Box**: A whole business someone could set up to commercialize Pepa and its devices. [history](terms/pepa-in-a-box.md)
- **Pepa Self Monitoring Arm**: Pepa watching Pepa: a deterministic, advisory-only arm on its own small computer, so it does not fail for the same reason the thing it watches fails. [history](terms/pepa-self-monitoring-arm.md)
- **Pepa Sensory Arm**: The boundary between Pepa and the physical world; it perceives, delivers and collects raw data and never interprets it, except through declared reflexes. [history](terms/pepa-sensory-arm.md)
- **Pepa-to-Go**: A portable rack build; the existing 6-port Protectli migrates into it, freeing house routing for a successor box. [history](terms/pepa-to-go.md)
- **pepa-tts**: Piper text-to-WAV endpoint on the Mac Studio, for narration clips, not daily Pepa use. [history](terms/pepa-tts.md)
- **PepaTix**: Voice satellite: a Raspberry Pi 4 with a reSpeaker XVF3800 microphone board. [history](terms/pepatix.md)
- **PepaV0 / PepaV1**: Successive live Home Assistant assistant configurations. [history](terms/pepav0-pepav1.md)
- **PHSA**: see **Pepa Human Sentinel Arm**. [history](terms/pepa-human-sentinel-arm.md)
- **PHSA recorder**: see **Recorder**. [history](terms/recorder.md)
- **Plan-Z**: The networked reach to an online provider — not a capability dial. [history](terms/plan-z.md)
- **Position**: An Arm, considered as a roster slot to be filled by a model. [history](terms/position.md)
- **PRA** (Pepa Reasoning Arm): The abbreviation used on ai4aging.org. Direction: a planner that plans and never executes, while still serving plain completions. [history](terms/pra.md)
- **Prime Directives**: Five rules: no silent action; no inferred intent; no external escalation without internal exhaustion; no commerce without explicit approval; the user may always ask "why now?". [history](terms/prime-directives.md)
- **Promotion / Trade / Reclamation sweep**: The three roster-move protocols. Promotion = recon → shadow eval on the real harness → clean beat. [history](terms/promotion-trade-reclamation-sweep.md)
- **Prompt injection**: The same failure weaponized: content masquerading as intent. [history](terms/prompt-injection.md)
- **Provenance-at-write**: Provenance attaches at the moment of the structured write, or nowhere. source:explicit_user vs source:inferred, mapped to trust tiers. [history](terms/provenance-at-write.md)
- **PSA**: see **Pepa Sensory Arm**. [history](terms/pepa-sensory-arm.md)
- **PSMA**: see **Pepa Self Monitoring Arm**. [history](terms/pepa-self-monitoring-arm.md)
- **Punt**: The local LLM delegating a query to the External LLM via the query_external_llm tool. [history](terms/punt.md)
- **Punt-fast**: When confidence is low, the right response is clarification or escalation, not improvisation. [history](terms/punt-fast.md)
- **PUPR / ECECS**: Polytechnic University of Puerto Rico and its ECECS department — the academic collaboration proposal (wake-word corpus, custom TTS voice, student project mapping). [history](terms/pupr-ececs.md)
- **pve1**: MSI Cubi, Core 3 100U, 16 GB DDR5, 2×2.5GbE. [history](terms/pve1.md)
- **pve2**: Mac mini A1993, 32 GB, Proxmox. Hosts the canonical SurrealDB (Memory Arm) and the Knowledge Arm services. [history](terms/pve2.md)
- **pve3**: NUC7i5. Experiments and coding sandbox — not part of the production stack. [history](terms/pve3.md)

## Q

- **Quimbal**: Coined namespace element carried by every fabricated institution or place in the fixture corpus; it names nothing. [history](terms/quimbal.md)

## R

- **Radlein**: Anton Radlein's hass-agent-llm, forked as prsws/pepa-arm-ha and prsws/pepa-sensory-arm. [history](terms/radlein.md)
- **rapid-mlx**: The MLX inference server on mmm4 serving the Sensory Arm over an OpenAI-compatible endpoint. [history](terms/rapid-mlx.md)
- **Raw**: As received at the boundary, whatever it is, and always declared. [history](terms/raw.md)
- **Reasoning Arm**: The heavier local thinking, "Reasoning as a Service": it suggests, the Head decides. Runs on the Mac Studio. [history](terms/reasoning-arm.md)
- **Recon grade**: Evaluation depth marker: characterized but not committed to. [history](terms/recon-grade.md)
- **Recorder**: The Human Sentinel Arm's record store plus its rules, and nothing else; the watching logic is a client of it. [history](terms/recorder.md)
- **Reflex**: A direct, requested house action carried out through explicit, declared and guardrailed rules, never beyond them. [history](terms/reflex.md)
- **remember this**: see **Fast-track**. [history](terms/fast-track.md)
- **Representational entanglement**: In a transformer, a token's meaning, context, and apparent purpose are blended into one vector; there is no architectural seam separating content from intent, so the model must infer intent. [history](terms/representational-entanglement.md)
- **Retrieval ≠ authority**: Operational form of the above: recalled beliefs inform the prompt but never authorize a safety-critical actuation. [history](terms/retrieval-authority.md)

## S

- **S1–S8** (specs 1 to 8): The spec queue drawn from the charts, ordered by dependency. [history](terms/s1-s8.md)
- **Safety-critical exemption**: Safety-critical entries (medications, allergies, fall history, protected actions, emergency protocols) are exempt from every salience, decay, and modulation mechanism. [history](terms/safety-critical-exemption.md)
- **Salience ≠ veracity**: Recall frequency, affective resonance, and usage-reinforced stability are legitimate salience signals and become false-memory-climb accelerants if allowed to feed a trust score. [history](terms/salience-veracity.md)
- **scouting queue**: see **Farm system**. [history](terms/farm-system.md)
- **Season vs. game**: The small-vs-frontier choice is re-made every roster cycle, not decided once. [history](terms/season-vs-game.md)
- **Self-Harness**: arXiv 2606.09498. An agent proposes its own harness edits, verifier-grounded. Pepa harvests Weakness Mining from it. [history](terms/self-harness.md)
- **Self-Monitor Arm**: see **Pepa Self Monitoring Arm**. [history](terms/pepa-self-monitoring-arm.md)
- **Senior Zero**: José himself — the system's first live field-test subject. Building Pepa around its maker's own present and eventual needs is described as what keeps the work honest. [history](terms/senior-zero.md)
- **Sensory Arm**: see **Pepa Sensory Arm**. [history](terms/pepa-sensory-arm.md)
- ~~Shared spec, local enforcement~~: replaced by **One ontology, one validator service**. [history](terms/shared-spec-local-enforcement.md)
- ~~SMA~~ (Self-Monitor Arm): replaced by **Pepa Self Monitoring Arm**. [history](terms/sma.md)
- **Structured observation**: The write unit: not a transcript line, but provenance + deterministic HA state anchor + timestamp + temporal-bound seed. [history](terms/structured-observation.md)
- **SUBJ-01/02/03, CARE-01/02, SENDER-01**: The fixture cast. [history](terms/fixture-cast.md)
- **Synthetic Fixtures**: The fixed cast of fabricated people used in every example, spec, bug report, and hosted-model conversation about Pepa. [history](terms/synthetic-fixtures.md)

## T

- **the climb**: see **False-memory climb**. [history](terms/false-memory-climb.md)
- **the functor problem**: see **Representational entanglement**. [history](terms/representational-entanglement.md)
- **Three exits** _(proposed)_: Every Head run ends in one of three exits: done, punted or error. Punted is a correct outcome, kept apart from error. [history](terms/three-exits.md)
- **Three-layer separation**: The LLM proposes, NeMo Guardrails permits, HA executes. Independently tunable layers. [history](terms/three-layer-separation.md)
- **Tier ladder**: The routing hierarchy for utterances: canned-phrase speed match → HA-native intent → LLM (PSA). [history](terms/tier-ladder.md)
- **True copy**: Ground truth in the pharmaceutical sense: a copy verified to preserve the original's content and meaning. [history](terms/true-copy.md)
- **Two timestamps**: Every reading carries when it was measured and when Pepa learned of it. [history](terms/two-timestamps.md)
- **Typed proposal** _(proposed)_: The Head's typed reply to the Arm: a sourced answer, a clarifying question or an abstention, always naming its source. [history](terms/typed-proposal.md)

## U

- **UC1–UC8** (use cases 1 to 8): The eight use cases on the ai4aging.org use cases page, from Memory Recall (1) to Quiet Watchfulness (8). [history](terms/uc1-uc8.md)
- **Utterance ledger**: Append-only record of every final STT transcript, captured above the tier fork — the only point that sees 100% of voice traffic. [history](terms/utterance-ledger.md)

## V

- **volatile / verify flags**: Entity-metadata columns. [history](terms/volatile-verify-flags.md)

## W

- **WAL** (write-ahead queue): Append-only JSONL on mmm4 where extraction output and explicit-user writes land first, draining to canonical when reachable. [history](terms/wal.md)
- **Whisplay**: The PiSugar Whisplay HAT portable-satellite attempt. Shelved Sep 2026; its Orange Pi went to PSMA. [history](terms/whisplay.md)
- **WolfStack**: Proxmox cluster tool under evaluation, joining pve1, pve2 and pve3. [history](terms/wolfstack.md)
