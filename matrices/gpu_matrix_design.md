# GPU Error-Class Heat Map — Merged Matrix Design

Purpose: answer Bangalore's question "which GPU failure classes are most frequent?" to prioritize
REVA-MPI fault-tolerance work. Merged from 12 per-system extractions (checkpoints `gpu_*.json`,
per-system source extractions (held in the authors' working repository)).

**Cardinal rule for the heat map: values are NEVER comparable across columns.** The 12 systems use
5 incompatible denominator bases (raw rates, logged-event shares, failure/interruption shares,
failed-job GPU-time shares, node-defect shares). Color/intensity must be computed WITHIN each
column (rank or normalized share), with a denominator badge per column header.

---

## 1. Unified row list of GPU error classes

Merged classes (synonyms folded in; canonical Xids in parentheses):

1. **uncorrectable-memory** (DBE Xid 48; contained/uncontained Xid 94/95; row-remap FAILURE Xid 64
   on H100; Titan "DBE"; Blue Waters `DBE` tag; Acme "ECCError" job-killing; Llama3 "GPU HBM3
   Memory"). Always application-fatal.
2. **correctable-memory** (SBE; row-remap EVENT Xid 63; consecutive-SBE degradation; SuperBench
   row-remapping gray failure). Transparent to apps; value is as a PREDICTOR, not a failure class.
   Individual SBEs are unlogged on Delta/DeltaAI corpora — those cells are floors.
3. **MMU/illegal-access** (Xid 13/31/43). **Largely APP-INDUCED masquerading as hardware**: Delta
   authors treat most Xid 31 as user illegal access; Fire-Flyer bins 13/31/43/45 as
   "software causes" (~54.9%); Titan authors note one confirmed Xid 13 case that WAS hardware —
   attribution "extremely challenging". Heat map must visually flag this row (hatching or
   footnote glyph) so it is not read as hardware unreliability.
   Boundary note: Xid 43 sits between this class and driver; Titan sources put it under driver,
   Fire-Flyer under illegal-access — kept where each source put it, flagged in cell notes.
4. **GSP/driver** (Xid 119/120 GSP RPC timeout; K20X-era sw-Xids 43/44/59/62; Blue Waters
   `UNABLE_TO_RESET`; TSUBAME-3 "GPU driver-related" software loci; Llama3 "GPU System Processor").
5. **NVLink** (Xid 74 on A100; Xid 145/149 on B200; Acme "NVLinkError"; Fire-Flyer NVLink-Bridge
   Xid 74; SuperBench NVLink all-reduce defect). Absent by construction pre-Pascal (Titan/BW).
6. **off-bus / device-lost** (Xid 79; Titan "OTB"; Blue Waters `INVALID_DEVICE` nearest analog;
   Llama3 "Faulty GPU" incl. falling off the bus; Meta-RSC Xid-79/PCIe co-occurrence).
7. **interface/PCIe** (non-Xid PCIe path: Meta-RSC lemon "PCIe"; SuperBench H2D/D2H bandwidth).
   Overlaps physically with off-bus (Titan OTB was a PCIe/SXM connector defect) — keep separate
   rows, note the overlap.
8. **thermal/power** (Llama3 thermal interface/sensor; PMU SPI Xid 122/123 could sit here or in
   other; Titan/Acme/TSUBAME name thermal only as a MODIFIER/root-cause narrative, never a
   quantified class).
9. **SDC — silent data corruption** (Llama3 only source with a count; invisible in every
   Xid/ECC-based taxonomy by definition).
10. **generic/unattributed GPU** (no sub-class breakdown in source: TSUBAME "GPU" category;
    Meta-RSC lemon "GPU"; Acme "CUDAError").
11. **other-named** (system-specific, kept as footnotes: Titan resistor-corrosion batch event;
    BW `MODULE_MISSING`; Delta PMU-SPI + node lockups; Fire-Flyer Xid 45 + misc uncorrectables;
    B200 machine-unreachable + performance degradation; Llama3 GPU SRAM; SuperBench benchmark
    categories incl. non-GPU).

---

## 2. The matrix

Legend: plain number = % of that column's denominator. `R:` = rate, not share (no share
denominator exists). `~` = inferred/decoded/figure-read. `*` = special basis, see column note or
cell. `nq` = named in source but unquantified (render hatched). `—` = not reported / structurally
absent (render grey, NOT zero). `0` = measured zero. `n/a` = class cannot exist on that hardware.

| Class | TIT (Titan K20X) | BW (BlueWaters K20X) | TSU (TSUBAME 2/3) | DA (Delta A100) | DH (Delta H100) | A3 (Ampere-3sys) | FF (Fire-Flyer A100) | B200 (DGX B200) | LL (Llama3 H100) | AC (Acme A100) | RSC (Meta RSC A100) | SB (SuperBench A100) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| uncorrectable-memory (Xid 48/94/95, +64 DH) | R: ~4.3/mo (MTBF ~160 h) | ~0.009 | — | 0.17 | 3.19* | 0.8* (upper bnd) | 0.25* | 11.8 | 17.2* (HBM3, no SBE/DBE split) | 11.00 (time-share) | nq | — |
| correctable-memory (SBE / Xid 63) | R: ≥100/day (floor) | — | — | 0.45 (floor) | 1.26* (floor) | 99.2* (lower bnd) | 1.9* | — | — | — | — | 3.37 (node-share) |
| MMU/illegal-access (Xid 13/31/43) **[app-induced]** | R: 40–200/mo (Xid 13 peak) | ~36.84 | — | 59.8 | 95.39* | — | 53.01* | — | — | — | — | — |
| GSP/driver (Xid 119/120 / sw-Xids) | R: ≤37/mo (Xid 43 peak) | ~21.09 | ~42.7* (of 171 T3 sw loci; ≈21.6 of all T3) | 26.0 | 0.16* | — | 0.01* | 5.9 | 4.1* | — | nq | — |
| NVLink (Xid 74/145/149) | n/a | n/a | — | 12.97 | 0* | — | 42.57* | 29.4 | nq (hangs, not in Table 5) | 30.25 (time-share) | nq | 0.30 (node-share) |
| off-bus / device-lost (Xid 79 / OTB) | R: peak 26/mo (pre-fix) | ~41.94 (INVALID_DEVICE) | nq | 0.067 | 0* | — | 0.29* | 11.8 | 30.1* (Faulty GPU incl. off-bus) | — | 43* (co-occ. share of PCIe errors, RSC-1) | — |
| interface/PCIe (non-Xid) | (in OTB) | — | — | — | — | — | — | — | — | — | 15.4 (lemon-node) | 2.03 (node-share) |
| thermal/power | nq (modifier only) | — | nq | 0.52* (PMU SPI 122/123) | 0* | — | — | — | 1.4* | nq (July-2023 narrative) | — | — |
| SDC | — | — | — | — | — | — | — | — | 1.4* | — | — | — |
| generic/unattributed GPU | — | — | 44.37* (T2) / 27.81* (T3) | — | — | — | — | — | — | 15.77 (CUDAError, time-share) | 28.2 (lemon-node) | — |
| other-named | 59% of FLEET replaced (resistor corrosion, 2016–17) | ~0.12 MODULE_MISSING | — | 0.18* node lockups (outside denom) | 9 lockups (outside denom) | — | 1.85* Xid 45 + 0.14* misc | 11.8 machine-unreachable + 29.4 perf-degradation | 4.5* GPU SRAM | — | — | 10.36 overall defective nodes; 6.04 IB-NIC (non-GPU, largest) |

### Per-column denominators (MUST render under/over the heat map)

- **TIT** — Titan K20X, 18,688 GPUs, 2013–15 (+2019 survival). NO share denominator exists;
  cells are rates (events/month or /day system-wide) or MTBF-derived. Within-class shares in
  quotes only (e.g. 86% of DBEs in device memory).
- **BW** — Blue Waters XK7, 4,224 K20X, 518 days. Share of 593,195 logged GPU-subsystem error
  EVENTS (5 tags, DSN'15 Fig. 3(b), CID-decoded, `~`); bursty repeated logging dominates; not
  failures.
- **TSU** — TSUBAME-2 (897 failures, 2012–13) / TSUBAME-3 (338 failures, 2017–20). Share of ALL
  logged system failures; GPU appears only as an all-cause category. Driver row: share of 171
  T3 SOFTWARE root loci.
- **DA** — NCSA Delta, 448 A100, 895 days. Share of 14,821 critical Xid EVENTS (sums exactly).
- **DH** — Delta GH200, 608 H100, 146 days. Share of 1,821 critical Xid EVENTS (`*`: short
  window, GH200-integrated H100s may not transfer to discrete SXM/PCIe).
- **A3** — Ampere-3sys (Delta+Polaris+Perlmutter), 10,693 GPUs, 67.77M GPU-h. Share of 7,242,596
  DCGM DRAM ECC events ONLY; Polaris SBEs unrecorded (SBE=lower/DBE=upper bound). All non-memory
  rows structurally absent.
- **FF** — Fire-Flyer 2, 10,000 PCIe A100, ~1 yr. Share of 12,970 raw Xid EVENTS (sums exactly);
  one flaky NVLink Bridge can emit many events.
- **B200** — 504-GPU B200 cluster, 55 days. Share of only 17 taxonomy failure events (tiny n;
  sums to 100%).
- **LL** — Llama3 405B run, 16,384 H100, 54 days. PRINTED Table-5 % of 419 unexpected job
  interruptions; printed %s sum to ~94% and do not reconcile with counts — cite as printed,
  never recompute.
- **AC** — Acme Seren+Kalos, 4,704 A100-SXM, 6 mo. Share of failed-job GPU TIME (counts tiny:
  NVLink 54, CUDA 21, ECC 12); classifications "may overlap".
- **RSC** — Meta RSC-1/2, ~24k A100, 11 mo. Share of 40 lemon-NODE root causes (node-defect
  basis); off-bus cell is a different basis again (co-occurrence share of PCIe errors).
- **SB** — Azure SuperBench, 24k+ A100 build-out, 90 days. % of NODES flagged per benchmark;
  categories overlap, don't sum; build-out phase overstates burned-in rates.

---

## 3. Prioritization read (what Bangalore's heat map should say)

**(a) The biggest raw event class is not a hardware problem.** MMU/illegal-access dominates every
event-count column that logs it (Delta A100 60%, Delta H100 95%, Fire-Flyer 53%, Blue Waters ~37%)
but is predominantly application-induced. FT implication: this argues for cheap crash-containment
and fast job-level recovery (the failure IS frequent and kills jobs at 74–90% probability), not
for hardware prediction. It also poisons any naive "predict Xids" ML target — the label mixes app
bugs with hardware faults.

**(b) When you count real hardware incidents, interconnect/attach dominates.** NVLink is the top
or near-top hardware class in every incident-basis column that can see it: Fire-Flyer 42.6% of
Xid events (PCIe A100 + NVLink Bridge), B200 29.4% (Xid 145/149, top category), Acme 30.25% of
failure GPU time. Off-bus/PCIe is its sibling: Llama3 30.1% (largest single Table-5 row),
B200 11.8%, Meta-RSC PCIe 15.4% of lemon causes with 43–63% Xid-79 co-occurrence, Titan's
pre-2014 OTB era, Blue Waters INVALID_DEVICE ~42% of logged GPU events. **First FT priority:
communication-path fault tolerance — link/communicator repair, shrinking/replacement semantics,
NCCL/MPI-layer recovery. This is exactly REVA-MPI territory.**

**(c) Uncorrectable memory is low-frequency but 100%-fatal and getting WORSE.** Event shares are
small (0.17–3.2% on Delta corpora, 0.25% Fire-Flyer) but every DBE kills the app; on
interruption/time bases it is material (Llama3 HBM3 17.2%, Acme 11%, B200 11.8%). Generational
trend is negative: H100 uncorrectable-memory MTBE 88,768 h = 3.2x worse than A100 (283,271 h),
and H100 row-remapping succeeds in only 59% of uncorrectable cases. **Second FT priority:
checkpoint/restart economics and memory-error containment sized for HBM3-class DBE rates, not
K20X-era rates.**

**(d) The A100→H100 flip (same site, same telemetry, Delta):**
- GSP/driver: 26.0% → 0.16% (3,857 → 3 events) — essentially eliminated by GH200 integration +
  driver maturity. Fire-Flyer saw 1 GSP event in a year. Don't invest FT effort here; it's a
  driver-maturation problem that vendors fix.
- NVLink Xid 74: 12.97% → 0 on GH200 nodes — but B200/NVSwitch systems put NVLink (145/149) right
  back at #1. The class is form-factor dependent, not "solved". Fire-Flyer's 42.6% is
  NVLink-Bridge-specific.
- Memory: uncorrectable share rises 0.17% → 3.19% and MTBE worsens 3.2x. Profile flipped from
  interconnect/GSP-dominated (A100) to memory-dominated (H100).
- MMU grows 60% → 95% (app behavior, not hardware).

**(e) Correctable errors are a prediction feature, not a failure class.** Titan: SBEs hundreds/day
but <5% of cards ever see one, heavily skewed, offender nodes hotter; SuperBench: >10 remapped
rows ⇒ 83.3% regression rate (vs 5.6% for 1–10); Ampere-3sys: 94% of Delta SBE interarrivals <1 h
(bursty). **Feed these into the AI/ML fault-prediction side of the dissertation as leading
indicators; do not rank them as a failure class.**

**(f) Fleet/batch pathologies rival steady-state rates.** Titan: 59% of the fleet replaced for a
corroded resistor (813 DBE/OTB events in one quarter, MTBF collapse >1 day → 2.7 h); Meta-RSC
lemon nodes; TSUBAME-2's 70% multi-GPU correlated failures cut to <8% by proactive health tests;
SuperBench 10.36% defective at build-out. **Third FT priority: fleet-level anomaly detection and
correlated-failure modeling — single-GPU-failure-rate assumptions are wrong exactly when it
matters.**

**Priority order for FT effort:** 1) NVLink/off-bus/PCIe interconnect recovery, 2) uncorrectable-
HBM containment + checkpoint sizing, 3) correlated/batch failure detection, 4) app-fault
containment (huge event counts, cheap wins), 5) SBE/remap telemetry as ML predictors. GSP/driver:
deprioritize.

---

## 4. Gaps (render as grey "no data", never as zero)

- **TSUBAME**: no GPU sub-class breakdown at all — the DSN'21 paper quantifies only the all-cause
  GPU category; off-bus, thermal, correlated reboots named qualitatively only.
- **Ampere-3sys**: DRAM ECC only; NVLink/off-bus/MMU/GSP/thermal/row-remap rows structurally
  absent (and contrary to earlier hints, no retired-page telemetry either).
- **SuperBench**: benchmark-defined taxonomy; off-bus, DBE, MMU, GSP, thermal unmapped.
- **Meta-RSC**: GPU memory, NVLink, driver/firmware, GPU-unavailable named but "not individually
  quantified"; only lemon-node shares exist.
- **Blue Waters**: no failure-share (vs event-share) GPU breakdown in open sources; DSN'14
  per-category splits paywalled/unverifiable; correctable SBEs absent from corpus.
- **Titan**: no unified share denominator — rates only; no NVLink (pre-NVLink hardware); thermal
  only as modifier.
- **Thermal/power**: quantified NOWHERE except Llama3 (1.4%) and Delta's PMU-SPI oddity (0.52%);
  everywhere else a narrative modifier. A known blind spot, not evidence of rarity.
- **SDC**: one count in one system (Llama3, 6 events). Structurally invisible to every Xid/ECC
  taxonomy. Cannot be heat-mapped honestly beyond that cell.
- **Correctable SBEs**: unlogged by design on Delta A100/H100; unrecorded on Polaris. All
  correctable cells are floors.
- **Generation gap**: no K80/P100(except TSU all-cause)/V100-era system with class-level data —
  the matrix jumps from K20X (2013–15) to A100 (2021+).
- **Xid 43 ambiguity**: classified under driver (Titan) vs illegal-access (Fire-Flyer, Delta
  grouping); any cross-system MMU-vs-driver comparison inherits this.

---

Checkpoint written: [local path removed]