Checkpoint written to /Users/trpatel2/ClaudeChats/PhD/REVA-MPI-AI/rework/checkpoints/ledger_merged.md. Full content:

# Catalog-Coverage Ledger — Phase-1 Merge (148 entry verdicts)

Merged 2026-07-18. Every one of the 148 catalog entries is assigned exactly one verdict below; the class lists account for all of them, so nothing in the catalog is unexplained.

## 1. The Accounting

| Verdict | Count | Meaning |
|---|---|---|
| RATES-ONLY | 37 | Real failure/availability events, but only rates or device-level counts — no failure-class share breakdown. Side-table material. |
| NO-FAILURE-INFO | 35 | Telemetry, synthetic-injection, or workload data with zero real-failure signal. Honestly excluded. |
| COLUMN-LABEL | 25 | Per-job outcome labels (exit states/codes) but no cause attribution. Fills label rows of a column. |
| COLUMN-CAUSE | 19 | Quantitative cause-attributed failure shares (from data or the source paper). Fills cause rows of a column. |
| DUPLICATE-OF | 18 | Same artifact as another catalog entry; collapses into it (see §3). |
| PAPER-STATS | 8 | Published aggregate statistics only; raw data never released. Column possible but paper-derived. |
| REPOSITORY | 6 | Umbrella archive whose members carry their own verdicts. Not itself a column. |
| **Total** | **148** | |

### COLUMN-CAUSE (19)
- Acme LLM cluster trace (Shanghai AI Lab / AcmeTrace) — *Acme*
- AcmeTrace — utilization + failure/RAS subset — *Acme (same release; see §4)*
- Fire-Flyer 2 AI-HPC Xid Error Characterization (DeepSeek) — *Fire-Flyer*
- From Detection to Recovery: Operational Analysis on LLM Pre-training with 504 GPUs — *DGX-B200*
- Llama 3 405B Pre-training Interruption Breakdown (Table 5) — *Llama3-405B*
- MegaScale / ByteRobust — ByteDance failure statistics — *ByteDance (MISSING COLUMN)*
- Meta ML Research Cluster Reliability Data (arXiv:2410.21680) — *Meta-RSC*
- Microsoft Philly Trace (philly-traces) — *Philly*
- NVIDIA DGX Cloud Reliability Data (Nemotron) — *NVIDIA DGX Cloud (MISSING COLUMN)*
- Blue Waters K20X GPU error records — *BlueWaters*
- Story of Two GPUs (Delta GPU resilience artifact) — *Delta-A100-H100*
- Blue Gene/P Intrepid RAS + Job Logs — *Intrepid (MISSING COLUMN)*
- Blue Gene/Q Mira RAS Logs (LogAider) — *Mira*
- LANL failure data (22 HPC systems, 1996-2005) — *LANL-22sys*
- USRC Failure/Interrupt Data 1996-2005 (LA-UR-05-7318) — *LANL-22sys (same dataset; see §4)*
- LANL Trinity trace (ATLAS) — *Trinity (MISSING COLUMN)*
- Mira 2K-day Multi-Source Job Failure Logs — *Mira*
- NERSC I/O Failure Database (CFDR / Remedy tickets) — *NERSC fleet (MISSING COLUMN)*
- ALCF Cobalt workload + RAS traces (IIT / Zhiling Lan) — *Mira (Intrepid portion uncovered)*

### COLUMN-LABEL (25)
- Alibaba GPU Cluster Trace 2020 (cluster-trace-gpu-v2020) — *Alibaba-PAI*
- Alibaba PAI GPU cluster trace (cluster-trace-gpu-v2020) — *Alibaba-PAI (same trace; see §4)*
- SenseTime Helios GPU Trace (HeliosData) — *Helios*
- Helios GPU Cluster Traces (HeliosData) — *Helios (same release; see §4)*
- Tachyon HPC job failure log (KISTI) — *Tachyon*
- F-DATA (Fugaku) — *Fugaku*
- FRESCO Job Failure & Performance Data Repository — *Conte-FRESCO-A (+ UIUC-Cray-FRESCO-B)*
- Grid Workloads Archive (GWA) — *(MISSING COLUMN)*
- PM100 (Marconi100) — *Marconi100*
- The MIT Supercloud Dataset — *MIT-Supercloud*
- Alibaba cluster-trace-v2017 — *(MISSING COLUMN)*
- Alibaba cluster-trace-v2018 — *(MISSING COLUMN)*
- Google Borg Cluster Trace 2011 — *Borg-2011*
- Google Borg cluster trace 2019 — *Borg-2019*
- LANL Mustang cluster trace (ATLAS) — *(MISSING COLUMN)*
- Parallel Workloads Archive (PWA) — *PWA-aggregate*
- Polaris public job-history logs (ALCF) — *(MISSING COLUMN)*
- Theta job + Darshan I/O logs (ALCF) — *(MISSING COLUMN)*
- SURF Lisa "Generic and ML Workloads" — *SURF-Lisa*
- NREL Eagle HPC Jobs — *NREL-Eagle*
- NREL Kestrel HPC Jobs — *NREL-Kestrel*
- IN2P3 Computing Center 2024 Workload Dataset — *(MISSING COLUMN)*
- Two Sigma cluster trace (CMU ATLAS) — *TwoSigma*
- LAST — Lassen job/energy dataset (LLNL) — *(MISSING COLUMN)*
- DKRZ Mistral Slurm job-history dataset — *(MISSING COLUMN)*

### PAPER-STATS (8)
- Blue Waters Failure & Error Logs (LogDiver) — *BlueWaters*
- Desh / Doomsday Cray XC RAS & Console Log Corpus (NCSU) — *no column (heuristic labels, restricted)*
- OPT-175B Training Logbook / Chronicles (PDF) — *no column (narrative counts; could seed a coarse training-run column)*
- Unicron (Alibaba) — *Alibaba-Unicron*
- From Detection to Recovery (504x B200) — *DGX-B200*
- SuperBench (Microsoft Azure A100 fleet) — *SuperBench-Azure*
- L4 (Microsoft "Platform-X") — *Platform-X-L4*
- Fault-Tolerant HSDP at 100,000 GPUs (Meta) — *Meta-HSDP-100k*

### RATES-ONLY (37)
Deduplicated by system where several entries describe the same fleet:
- **Titan GPU error studies (4 entries):** Nie HPCA'16 soft errors; GPU Lifetimes survival analysis; Nie 2018 SBE telemetry; Understanding GPU Errors (SC'15) — all GPU error rates/cross-sections, no job-failure shares
- **Marconi/Marconi100 telemetry (3):** ExaMon Marconi snapshot; M100 time-aggregated; M100 ExaData — binary node-health only
- **CFDR hardware/disk-replacement logs (7):** COM1, COM2, COM3, HPC1, HPC2, HPC3, PNNL MPP2 — component replacement rates only
- **FTA availability traces (4):** Grid'5000 g5k06; Condor+Notre Dame; non-HPC subsets (lri05, pl05, websites02, …); SETI@home — up/down intervals, no cause
- **Alibaba device fleets (4):** SNIA NVMe fail-slow/fail-stop; SSD SMART (dcbrain); SSD failures (Tianchi/FAST'21); HDD prediction (PAKDD 2020) — device labels, not cluster shares
- **LLM training narratives (5):** OPT-175B logbook (restart counts); BLOOM chronicles; GLM-130B logs; Imbue 70B bring-up; LLM360 loss spikes
- **Other (10):** Alibaba v2023 + HPN rates; neutron-beam GPU DUE study; Summit GPU DBE snapshots; Ampere memory errors (Zhu 2025, Delta+Polaris+Perlmutter); Cray XT logs (6 incident dumps); Sandia/LLNL five-system alert logs (HPC4); USRC MX20 disk file; Minder (ByteDance); TPUv4 resiliency; Backblaze Drive Stats

### NO-FAILURE-INFO (35)
- **Synthetic-injection anomaly datasets (10):** ALBADross, Prodigy artifact, E2EWatch, Proctor/Voltrino, Sandia Eclipse LDMS umbrella, HPAS (tool), Antarex/FINJ, HPC-ODA, Taxonomist (x2 entries) — labels are injected anomalies or app identity, not real failures
- **Darshan / I/O telemetry (10):** ALCF I/O Data Repository (Darshan), ALCF Polaris Darshan, ALCF Theta Darshan summaries, Summit April-2020 Darshan, darshan-logs example corpus, I/O Burst Prediction (BW+Mira+Theta), NCSA Blue Waters Darshan, Theta+Cori throughput (Isakov), TOKIO/pytokio Cori, Frontera I/O traces — survivorship-biased performance telemetry
- **Power/thermal/environment telemetry (6):** Summit power+thermal, Frontier energy/waste-heat, Adastra MI250 power, Trinity SEDC sensors, Perlmutter LDMS/DCGM (2 entries: system telemetry + GPU workload characterization)
- **Usage/metadata with zero failure signal (6):** USRC memory-usage stats, USRC MX8/15/16/23 usage traces, USRC fsstats, USRC VPIC checkpoints, USRC workstation FS metadata, ALCF public reports portal (Theta/Polaris I/O-utilization)
- **Other (3):** RoWD/SCRIPT-AI (workload-type labels), smaller AI SDC studies (injected faults), DKRZ Mistral I/O dataset — *(count: 10+10+6+6+3 = 35)*

### REPOSITORY (6)
CFDR (USENIX), CMU PDL ATLAS, Failure Trace Archive (FTA), ALCF Public Data Catalog, ALCF Public Data reports portal (Mira/Theta), SNIA IOTTA. Members are catalogued and verdicted individually.

### DUPLICATE-OF (18) — see §3.

## 2. Missing Columns (Phase-2 extraction targets)

14 flags, deduplicated to 14 distinct systems:

| System | What it offers | Access | Priority |
|---|---|---|---|
| LANL Trinity (ATLAS trace) | CAUSE — JOBFAIL events + errno-style completion_code (e.g. ENOMEM); per-cause shares computable | public | **HIGH** |
| ALCF Intrepid (BG/P RAS + Cobalt jobs) | CAUSE — FATAL events with 82 ERRCODEs across 6 components, paired job logs | public (CFDR) | **HIGH** |
| ALCF Polaris (job-history logs) | LABEL — job state + PBS exit status | public | **HIGH** |
| ALCF Theta (Cobalt job logs) | LABEL — exit status/codes, outcome states | public | **HIGH** |
| Alibaba colocation v2017 | LABEL — Failed/Terminated/Cancelled/Interrupted + machine soft/hard-error events | public | **HIGH** |
| Alibaba colocation v2018 | LABEL — Failed vs Terminated per instance try | public | **HIGH** |
| IN2P3 Computing Center 2024 | LABEL — 44M jobs with execution/exit records | public | **HIGH** |
| LANL Mustang | LABEL (weak) — only Completed/Cancelled/Timeout, no FAILED state; 61-month trace | public | **HIGH** (flag weakness) |
| Grid Workloads Archive (GWA) | LABEL (weak) — SWF Status 0/1/5 across ~9 grids; Status unreliable in some traces | public | **HIGH** (flag reliability) |
| ByteDance MegaScale/ByteRobust | CAUSE — 38K explicit failures with category percentages, symptom-to-cause taxonomy | paper-only | MED |
| NVIDIA DGX Cloud (Nemotron) | CAUSE — error-attribution shares (ECC 38.9%, PCIe 6.6%, NIC 5.7%) | public blog, no data | MED |
| NERSC fleet 2001-2006 (I/O Failure DB) | CAUSE — outage events with subsystem + cause categories; companion report quantifies | on-request | MED |
| LLNL Lassen (LAST) | LABEL — job-step disposition, ~1.4M jobs | public-but-verify | MED |
| DKRZ Mistral (Slurm job history) | LABEL — job state/exit fields | unverified | LOW |

## 3. Duplicate Map

| Duplicate entry | Collapses into |
|---|---|
| AcmeTrace (Seren + Kalos cluster traces) | Acme |
| Alibaba GPU cluster trace 2023 (v2023) | Alibaba-PAI (v2023 + HPN entry) |
| Alibaba GPU Cluster Traces (v2020/v2023/Lingjun roll-up) | Alibaba-PAI (Lingjun adds no failure data) |
| Llama 3 405B Reliability Breakdown (root-cause table) | Llama3-405B (same Table 5) |
| MegaScale production failure narrative (NSDI'24) | ByteDance MegaScale/ByteRobust |
| Philly Trace (second listing) | Philly |
| Revisiting Reliability… (RSC-1/RSC-2 second listing) | Meta-RSC |
| Nie et al. Titan GPU error trace (DSN 2018) + TitanGPULife | Titan |
| Titan GPU Failure/Lifetime Data (K20X DBE/OTB) | Titan (= TitanGPULife) |
| Blue Gene/P Intrepid RAS Log (CFDR second listing) | Intrepid |
| LANL HPC Failure Data (Schroeder & Gibson) | LANL-22sys |
| Loghub HPC RAS log collection | Sandia/LLNL five-system logs (Oliner-Stearley) |
| Loghub Sandia/LLNL Supercomputer System Logs | Sandia/LLNL five-system logs (Oliner-Stearley) |
| Prodigy Eclipse Dataset (second listing) | Sandia Eclipse Prodigy artifact (Zenodo 8079388) |
| Google Borg Cluster Traces (combined roll-up) | Borg-2011 + Borg-2019 |
| ALCF I/O Data Repository (Mira Darshan, second listing) | ALCF Mira/Theta Darshan |
| ALCF Mira Darshan I/O Logs (third listing) | ALCF Mira/Theta Darshan |
| Argonne Leadership Computing Facility DATA CATALOG (IEEE DataPort) | ALCF Public Data portal |

Unmarked near-duplicates found during the merge (verdicted twice instead of once): Acme (2x COLUMN-CAUSE), Alibaba PAI v2020 (2x COLUMN-LABEL), Helios (2x COLUMN-LABEL), LANL-22sys (2x COLUMN-CAUSE), OPT-175B logbook (RATES-ONLY + PAPER-STATS), From Detection to Recovery / DGX-B200 (COLUMN-CAUSE + PAPER-STATS). These do not change any conclusion — each pair points at one system that is (or is not) a column exactly once — but the true unique-artifact count is 6 lower than the raw verdict counts suggest.

## 4. Discrepancies vs v1/v2 treatment

1. **Titan column has no COLUMN-grade source.** Every Titan entry is RATES-ONLY or DUPLICATE (GPU error rates/survival, no job-failure or cause-share breakdown), yet Titan is a v2 matrix column. Either the column is built on GPU-error rates being treated as failure shares (should be demoted to a side table), or its actual source needs to be documented.
2. **Frontier column not fed by any catalog entry.** The only Frontier entry (energy/waste-heat) is NO-FAILURE-INFO; the column reportedly comes from the SC'23 defect study, which is absent from this catalog and should be added as an entry.
3. **Intrepid has public cause-labeled data but no column**, even though its sibling Mira (same ALCF Cobalt+RAS pairing, same research group) is a column. Strongest missing-column case.
4. **DGX-B200 column rests on on-request data** — one entry says COLUMN-CAUSE with data via lablup.com contact, the twin entry says PAPER-STATS ("tables, no raw dump"). The matrix should record which it actually used; if the data request was never fulfilled, the column is paper-stats grade.
5. **OPT-175B verdict conflict** — same logbook judged RATES-ONLY in one entry and PAPER-STATS (column-seedable counts) in another. Resolve to PAPER-STATS: hand-extracted counts could seed a coarse training-run column analogous to Llama3-405B; currently excluded.
6. **Marconi100 column is fine but only via PM100** — the two M100 telemetry entries are RATES-ONLY; the column's label data must be cited to PM100 specifically, not "Marconi100 data" generically.
7. **FTA lanl05 vs LANL-22sys** — FTA is marked gone, but its only cause-labeled member duplicates the still-public LANL-22sys column, so nothing is actually lost.
8. **Grid'5000 appears twice with different fates** — dead as an FTA availability trace (RATES-ONLY, gone) but alive inside the public GWA with job Status labels; the GWA copy is the usable one.

## 5. Plain-language summary

Of the 148 catalog entries reviewed, 18 are flat-out duplicates (the same dataset listed under two or three names) and 6 are umbrella archives rather than datasets, leaving roughly 124 real artifacts. Of those, 35 contain no failure information at all — they are performance telemetry, power readings, or lab experiments with artificially injected faults, so excluding them from the failure matrix is honest, not an oversight. Another 37 record real failures but only as rates or device counts (a disk was replaced, a node went down) without saying what share of failures each cause explains, so they feed side tables rather than columns. That leaves 44 column-grade entries with per-job outcome labels or genuine cause breakdowns, plus 8 paper-only statistics: most of these are already columns in the v2 matrix, but 14 systems with usable data are not — 9 of them public and labeled (Trinity, Intrepid, Polaris, Theta, Alibaba v2017/v2018, IN2P3, Mustang, GWA), which become the Phase-2 extraction targets. The audit also surfaced two columns (Titan, Frontier) whose catalog sources do not actually support them as built, which needs fixing alongside the additions.