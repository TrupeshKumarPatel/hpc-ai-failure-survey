# Verification Report — Heat-Map Triple Check (2026-07-18)

**Trigger:** advisor-bound figures showed extensive gray; user requested a full 3x re-check plus a per-type taxonomy grounding.
**Method:** 34 agents in 5 phases. (1) Exhaustive enumeration: 931 raw failure-type mentions from 37 studies + the dataset catalog. (2) Classification: 88 canonical types, 11 classes, per-type rationale (see 08). (3) Verify-A: every cell of both matrices (filled AND gray) checked against its source section, with quotes. (4) Verify-B: blind re-derivation of all 33 columns by agents who never saw the matrix; 25 disagreements + 27 newly derived cells escalated. (5) Verify-C: adjudication by quoted evidence.

**Outcome:** matrix v2 (matrix_count_v2.csv, matrix_time_v2.csv, dots_v2.csv; figures fig1/fig2_*_v2). Changes applied: 6 hard value errors fixed; 1 wrong-matrix cell removed; 2 non-failures (preemption/eviction = policy) removed; systematic denominator fixes (Unicron renormalized to failure shares; NREL aggregates de-mixed); 2 new COUNT columns added (Philly, Acme) from quoted counts; 11th row added (Outcome-labels & unattributed) receiving 13 columns' label-only data; ~80 presence dots distinguish 'present but unquantified' from true silence; SDC re-scoped as manifestation overlay.

**Verdict:** sound after corrections. ~65% of filled cells confirmed by >=2 of 3 passes; ~45% untouched. Residual risk low-to-moderate: figure/bar reads (±1–2pp, marked ~), BlueWaters verified at abstract level (paywall), Llama-3 as-printed rows sum to ~94% (marked †), soft attribution in Fire-Flyer 54.9 and the FRESCO storage carve-out. No surviving cell rests on an unquoted derivation.

---

The full adjudication follows.

# Pass-3 Final Verification Report: FTXS Heat-Map Matrix

Conflict-resolution rule applied throughout: quoted evidence in Verify-A beats unquoted Verify-B derivations; where both are quote-backed, the more specific quote wins; where B's disagreement is a denominator convention rather than a value dispute, the matrix-wide convention (share of failures for COUNT, share of failure/lost time for TIME) decides. The taxonomy pass's meta row ("Outcome-labels & unattributed") is ADOPTED (see Section 4); "MOVE→meta" below means the value leaves the cause row and lands in that row with a dominant-class pointer.

---

## 1. FINAL CORRECTIONS LIST

### LANL-22sys
| Cell | Action | Justification |
|---|---|---|
| COUNT CPU/host-mem/PCIe = 50 | REMOVE point value; replace with range annotation "30 to >60 (per system)" | Source gives only a per-system range and a stacked bar chart; 50 is a fabricated midpoint. B's derivation confirms no point value exists. |
| COUNT software/system = 20 | REMOVE point value; replace with range "5–24 (per system)" | Source: "second largest; 5% to 24%". B's 14.5 is also an unquoted midpoint; neither is source-stated, so the range wins. Also avoids confusion with Unknown's genuine 20–30%. |
| All TIME cells | KEEP empty; add guard footnote | Per-category times (342/369/572/163/247 min) are repair DURATIONS, never downtime shares. Must not backfill. |

### BlueWaters
- KEEP all four: COUNT 42 / 20, TIME 23 / 53 (verbatim, repair-report basis). Two footnotes: (a) never mix with the Gainaru event-log basis (65.7/34.3); (b) values verified against the publisher abstract (paper paywalled).
- DEFER (prose only): user/app 18.75% of all runs (LogDiver) — different denominator (all 5M runs incl. successes).

### Titan
- KEEP fully empty (correct: GPU-only corpus, rates and MTBFs only, no cross-category shares). Keep trap numbers out (59% replaced GPUs = device fraction; 86/14 = within-DBE split).

### Mira
| Cell | Action | Justification |
|---|---|---|
| COUNT user/app = 99.4 | KEEP | Quoted verbatim. |
| COUNT CPU/host-mem = 0.6 | CHANGE → 0.47 | 0.6 is the TOTAL RAS share; compute-card/node hardware is 78.16% of it (0.6 × 0.7816 ≈ 0.47). Footnote the RAS sub-taxonomy rescale. |
| COUNT software/system | ADD 0.10 | RAS Software_Error 16.22% × 0.6% (A quote + B derivation agree). |
| COUNT network | ADD 0.017 | RAS MU 2.81% × 0.6% (A + B agree). |
| COUNT power/facility | ADD 0.001 | RAS Bulk Power Supply 0.16% × 0.6% (A + B agree). |
| TIME user/app = 32.86 | KEEP with footnote | TIMEOUT core-hours over TOTAL machine core-hours; excludes Bug/Kill/IO losses, understates user/app. |

### TSUBAME-2
| Cell | Action | Justification |
|---|---|---|
| COUNT GPU = 44.37, CPU = 1.78, storage = ~4, software = ~7.7 | KEEP | 44.37/1.78 text-stated; 4 and 7.7 bar-reads (keep tilde + bar-read footnote; Memory and Disk categories unquantified). |
| COUNT network = 8.7 | CHANGE → ~10.7 | Source has a separate IB category ~2% that the cell silently drops; A quotes it, B independently derived 10.7. |
| COUNT power/facility = 11.3 | REMOVE | It is the FAN category, source-classified as node hardware. The real power category (PSU) is an unquantified ~0.3–4% bar. Replace with presence dot. |

### TSUBAME-3
- KEEP 27.81 / 3.25 / 50.59 (the three text-stated values).
- ADD COUNT power/facility = ~1 (Power-Board bar read; A missed-number + B agree; tilde + bar-read footnote).

### Frontier
- KEEP empty in both share matrices. REJECT B's adds (software 79.2, GPU 20.8): those are 19-of-24 and 5-of-24 detections from ONE month of a node-screening program, not production failure shares. Presence dots + prose sidebar instead. Keep screening-cost numbers (1.4%, 0.18%) out.

### Tachyon
- MOVE both cells to meta row: count 8.6 (binary job-failure rate of ALL jobs) and time 37.5 (failed-job runtime over TOTAL runtime), pointer →user/app. The source never assigns user-vs-system blame; filing 100% under user/app was over-attribution and was inconsistent with Fugaku.

### Fugaku
- ADD meta row count = 10.4 (~2.5M of ~24M jobs; source layer "unknown"; footnote "upper bound"). Cause rows stay empty. This resolves the Tachyon/Fugaku convention conflict flagged by A.

### Marconi100
- FIX PROVENANCE: cite the F-DATA companion M100 Slurm Table 1 (~1.6M jobs, May–Oct 2020); the currently cited ExaData section explicitly denies any root-cause breakdown exists.
- MOVE→meta: user/app 10 (Failed, →user/app), CPU 0.01 (Node fail, →hardware). ADD to meta: Cancelled 8, Timeout 2, OOM 0.6 (currently missing entirely).
- REMOVE scheduler 0.1 (Preempted): source verbatim "scheduler policy, not a fault". Not a failure under any convention.

### SURF-Lisa
- MOVE→meta all three: count user 14 (FAILED state; footnote generic 14 vs ML 17), time user 26 (TIMEOUT only; footnote 26–27 both populations), time CPU 2.5 (NODE_FAIL runtime, generic node not CPU-specific; footnote ML 0.2). Column footnote: generic-population picks from a paper that always reports generic/ML pairs. Energy figure (~50%) stays out of both matrices.

### Conte-FRESCO-A
| Cell | Action | Justification |
|---|---|---|
| COUNT software/system = 53 | CHANGE → 35.5 | Quoted: 33% of system failures are exit-107 NFS/parallel-FS unreachability. Carving that out leaves 35.5 (B derived the same). |
| COUNT storage/filesystem | ADD 17.5 | The carved-out exit-107 share (≈17.5% of all failures); footnote that burst root causes include network congestion clusters (storage row per unified FS boundary rule). |
| COUNT user/app = 33 | KEEP | Quoted; footnote: share of non-walltime failures. |
| TIME software = 4.0, TIME user = 12.9 | KEEP with denominator footnote | Shares of ALL node-seconds incl. successes; B's 46.3 = adding walltime, which the meta row now holds instead. |
| Meta row | ADD walltime count 4.0% jobs / time 33.4% node-seconds (→user/app); indeterminate user/system 1.3% | Quoted; currently absent everywhere. |

### UIUC-Cray-FRESCO-B
- KEEP all four (4, 48, 1.4, 2.7; all quoted). B's alternates (0.3, 3.6, 11.6, 46.1) are denominator conversions, not value errors. Footnote: COUNT cells are share-of-failures while NREL-derived meta entries are share-of-jobs; matrix must state per-column denominators.
- ADD meta: indeterminate user/system 1.1% jobs / 8.0% node-seconds.

### NREL-Eagle
- REMOVE from user/app: count 16.4 and time 49.2. They are the FAILED+TIMEOUT+OOM+NODE_FAIL aggregate; they double-count NODE_FAIL (already in the CPU cell) and mislabel hardware events as user/app. MOVE aggregates to meta ("any failure state"); place FAILED-only 8.84 / 4.08 in meta with →user/app pointer.
- MOVE→meta (→hardware): count CPU 0.11 and time CPU 1.62 (NODE_FAIL; generic node, "undercounts hardware trouble").

### NREL-Kestrel
- Same restructure: 19.3 / 51.0 → meta aggregate; FAILED-only 12.90 / 3.90 → meta →user/app; CPU 0.34 / 3.5 → meta →hardware.
- MOVE scheduler 0.30 (DEADLINE) → meta (source layer "software"; scheduler pointer defensible, note divergence). ADD its time share ~0 (source states it).
- ADD meta: "CANCELLED by 0" (root/admin) ≈0.51% of jobs, system-initiated inside CANCELLED (footnoted).

### MIT-Supercloud
- KEEP count user 19.0 / time user 8.4 with scope footnote: development-failure subset only; the source's full user/app non-success is ~40.2% of jobs / ~61% of GPU-hours (B's 99.5/61 reflects that broader scope; quoted subset values stand, scope stated).
- CHANGE count GPU 0.5: remove from GPU row; record in meta as "<0.5% of job FAILURES, hardware overall, upper bound" (→hardware). It is an upper bound, hardware-general not GPU-specific, and on a different denominator than 19.0.

### PWA-aggregate
- MOVE→meta: count 8.4 / time 13.3 (status 0 layer explicitly "user/app or system, indistinguishable"; failed-vs-cancelled split is a logging convention). Footnote cancelled 5.3 / 6.2; combined non-complete 13.7 / 19.5 (= B's numbers) available if cancelled is included.

### Delta-A100-H100
- REMOVE count GPU = 60: raw-event share of A100 critical Xids only (H100 analogue is 95%; in an all-GPU-error dataset GPU ≈ 100% by construction; MMU errors mostly application-induced).
- REJECT B's network add (11.5 / NVLink 13.0): NVLink stays in the GPU class per taxonomy ruling, and it is the same event-share basis.
- ADD (footnoted, optional) TIME GPU ≈ 0.6–0.7: quoted node availability 99.4/99.3%, 5,700 node-hours lost to GPU downtime; basis = share of node-hours, not of failure time.
- Presence dots: user/app, storage (missing logs), SDC/fail-slow.

### Philly
- KEEP all seven TIME cells (all verified as %-of-total-RTF sums).
- ADD full COUNT column from quoted trial counts (footnote: trials = failure EVENTS inflated by fixed-retry policy): GPU 0.03, network 2.8, storage 5.0, software 5.4, user/app 57.3, data/input 24.2, scheduler 0.37 (preempted; policy-not-fault footnote, kept for symmetry with the filled TIME 1.66). A's computed values adopted; B matches within rounding.

### Helios
- MOVE→meta: count 15.5 / time 9.3 (Slurm FAILED label; NODE_FAIL and TIMEOUT explicitly folded in; only qualitative "majority are user errors"). Presence dot on user/app.

### Alibaba-PAI
- MOVE→meta: count 24.3 (pure outcome label; source layer "unknown"; user/app was inference).
- REMOVE time 14.7 from the TIME matrix: it is an inst_num-weighted CAPACITY share, not a time share; no PAI time-lost aggregate exists. May be recorded in meta as a capacity share with footnote.

### Acme
- KEEP all five TIME cells (57.0, 8.62, 2.12, 14.7, 3.2); column footnote: shares of FAILED-JOB GPU time, not cluster GPU time. Never backfill CPU/host with NodeFailure 14.30 (source-classed "unknown"; goes to meta).
- ADD COUNT column from quoted Nums (total 2,575): GPU 3.4, network 6.5, storage 0.4, software 15.7, user/app 73.4, data/input 0.2. ADD meta: NodeFailure 16 events / 14.30% of failure GPU time (unknown).

### Meta-RSC
- MOVE→meta: count user 24 (share of ALL jobs in a status mix, not of failures; as a failure share, app exits are "the overwhelming majority", dot only).
- ADD meta: infra failures 0.2% of jobs / 18.7% of runtime (→hardware aggregate; fills the otherwise-empty TIME column at meta level).
- Standing guard: lemon-node Table II percentages (GPU 28.2 etc.) are defective-NODE shares of 40 lemons; never promote.

### Llama3-405B
| Cell | Action | Justification |
|---|---|---|
| COUNT CPU/host-mem/PCIe = 2.0 | CHANGE → 1.5 | Class rows sum to 1.5 (CPU 0.5 + System Memory 0.5 + IO Expansion Board 0.5); 2.0 required counting Server Chassis, which is not this class. Chassis 0.5 → meta/unattributed hardware. |
| COUNT SDC = 1.4 | KEEP as overlay with cross-ref | It is inside GPU 58.7 (source category: GPU); exclude from column sums per the SDC-overlay rule. |
| COUNT GPU 58.7, network 10.1, storage 0.7, power 8.3, software 13.4 | KEEP | All verified as printed-row sums. Column footnote: percentages as-printed (they sum to ~94% vs counts totaling 419; never recompute). |
| Meta row | ADD NCCL Watchdog Timeouts 1.7 | Source category "Unknown"; belongs to no cause cell. |

### Alibaba-Unicron
- CHANGE all four COUNT cells to the failure-share denominator (current values are shares of ALL tasks incl. 56.6% successes; A computed the renorms, B independently agrees): GPU 11.6 → 26.7, network 21.1 → 48.6, software 5.3 → 12.2, user/app 2.1 → 4.8. Footnote: task-hang (3.1 of tasks) inside software is a fail-slow symptom, cross-ref SDC overlay.
- REJECT B's CPU/host add (4.8): A confirms genuine silence; invalid DMA mapping is already inside the GPU sum.

### Platform-X-L4
- ADD COUNT SDC/fail-slow = 16.6 (quoted symptom share of 428 failures: hangs + slowdowns; legitimate under the re-scoped manifestation-overlay row; the root-cause withholding does not apply to the published symptom split).
- All else stays qualitative. Guard: "training crash 57.5%" is a symptom bin "often from hardware faults", never a user/app share.

### Meta-HSDP-100k
- KEEP 31.7, 18.3, 5.3, 4.4, 6.5, 5.5 (all verified sums).
- ADD COUNT user/app = 7.1 (Software Bug row; provably dropped: 92.1 + 7.1 + 1.0 ≈ 100).
- CHANGE software/system 20.4 → 11.4 and MOVE NCCL Watchdog Timeouts 9.0 → meta (symptom bin, "root cause often hw/network"), applying the taxonomy's NCCL-timeout rule and matching Llama3's handling. (Fallback if minimal-change is preferred: keep 20.4 with a symptom-contamination footnote.)
- ADD meta: Unknown 1.0.

### Fire-Flyer
- KEEP 45.0 / 54.9 with two footnotes: shares of raw Xid EVENTS (not incidents or job failures); 54.9's user/app attribution is soft (source: hardware should be considered if software bugs ruled out).
- REJECT B's adds: network 30 (denominator = hardware faults EXCLUDING Xid_74) and CPU 54 events (different 6-month window). Presence dots instead.

### DGX-B200
- KEEP GPU 58.9 (verified 10/17 Xid sum).
- REMOVE CPU 11.8: both candidate 2-of-17 rows fail the class (GPU ECC is GPU-class and already inside 58.9; "machine unreachable" is component-unattributed; PCIe explicitly excluded from the taxonomy). Move "machine unreachable" 11.8 → meta/unattributed.
- KEEP SDC 19.0 with denominator footnote (4/21 failures vs /17 Xid basis of the other cells; the /17 analogue "Others, performance degradation" = 29.4 noted).
- DEFER to prose: DGX Cloud "<1% of downtime hardware-attributable" (different system in the merged section).

### SuperBench-Azure
- RE-BASIS the whole column: 0.23 / 2.03 / 6.04 are % of NODES flagged defective at BUILD-OUT, single cherry-picked benchmarks, categories non-exclusive (total 10.36%). KEEP values only with a distinct cell marker + column footnote excluding it from cross-column share comparison; otherwise demote to dots. B's 28.3/22.3/49.4 REJECTED (unquoted, basis unclear).
- ADD (same basis, footnoted) SDC/fail-slow 0.33 (compute-comm overlap gray failure; note row-remap 3.19/0.18).
- All TIME cells stay empty (correct).

### Borg-2011
- MOVE→meta: count 1.7 (FAIL share of terminations) and time 33 (CPU time of "unsuccessful" = failed + killed). ADD KILL 40.7 to meta (→user/app). Footnote the pair's definitional mismatch (FAIL-only vs unsuccessful umbrella; B's 42.4 = FAIL+KILL).

### Borg-2019
- MOVE→meta: count 1.0 (FAIL of ended jobs); ADD KILL 85 to meta.
- REMOVE scheduler 3.2: per-collection INCIDENCE (~0% at event level), source layer "software", and eviction is policy per taxonomy. Record in meta as incidence with footnote if retained at all. B's proposal to re-home it under software/system REJECTED (wrong metric for a share cell regardless of row).

### TwoSigma
- MOVE→meta: time 50 (source layer "unknown"; authors explicitly refuse root-cause attribution; figure-read). ADD meta count 27–30 (figure-read twin that was dropped). Footnote: figure-reads, no printed numbers.

---

## 2. QUALITATIVE-CELL LIST (presence dots)

| Class | Column | Evidence (one line) |
|---|---|---|
| network | LANL-22sys | "small single-digit share (Fig. 1)" |
| user/app | LANL-22sys | human error, smallest bars in Fig. 1 |
| power/facility | LANL-22sys | environment small single-digit; power outages, A/C |
| storage | LANL-22sys | PFS most common software failure in system F |
| scheduler | LANL-22sys | scheduler software most common software failure (system H) |
| CPU/host TIME + software TIME | LANL-22sys | downtime rankings only (largest / second largest) |
| network | BlueWaters | Gemini HSN MTBI 857.7 h; share behind paywall |
| power/facility | BlueWaters | lumped in ~38% remainder |
| storage (COUNT+TIME) | BlueWaters | 74.4% of SWOs involved Lustre; Lustre dominates downtime (rank only) |
| GPU | BlueWaters | XK ~2x XE failure rate per node-hour |
| scheduler | BlueWaters | resource-mgmt software "most representative" software cause |
| SDC/fail-slow | BlueWaters | 28 escaped multi-bit errors; undercounted hangs |
| GPU (COUNT+TIME), CPU, user/app, software, SDC | Titan | rates/Xid frequencies only (DBE MTBF ~160 h, OTB, Xid 13/31, driver Xids, SBEs) |
| scheduler | TSUBAME-2 | PBS bar ~0.3–4% |
| power/facility | TSUBAME-2 | PSU bar unquantified (FAN 11.3 removed as hardware) |
| network | TSUBAME-3 | Omni-Path bar ~0.3–3.6%; hfi errors in software loci |
| storage | TSUBAME-3 | Disk/Lustre bars; XFS/Lustre/ext4 bugs inside the 50.59 software bucket |
| scheduler | TSUBAME-3 | SGE OOM 1.8% of software root loci (sub-denominator) |
| GPU + software + network | Frontier | 5 hw defects / 19 transients in one screening month; network folded in transients |
| user/app | Helios | "majority of failures are user errors" (no number) |
| hardware(node), data/input, software | Helios | NODE_FAIL "very rare"; incorrect inputs, runtime failure listed unquantified |
| user/app, storage, SDC | Delta-A100-H100 | MMU mostly app-induced; storage logs missing; degraded SBEs + unlogged lockups |
| GPU, CPU, network, storage, software, power, SDC | Meta-RSC | Fig. 4 categories present, none individually quantified; PCIe-XID79 co-occurrence; IB spike; FS mounts; PSU lemon-only; NCCL timeout hangs |
| SDC TIME | Llama3-405B | stragglers, stalled NVLink transfers, 1–2% diurnal throughput dip |
| SDC, scheduler | Alibaba-Unicron | task hang 3.1 (inside software, cross-ref); 9-min resubmission wait (recovery cost) |
| GPU, network, CPU, storage, user/app, software, scheduler | Platform-X-L4 | root-cause ranking published, all percentages withheld (hw most common; network top hw sub-type; user 2nd; framework small; platform least) |
| SDC, network, CPU | Fire-Flyer | SDC uncaught by ECC (gradnorm/loss); IB flash cuts (sub-denominator); 54 CPU ECC events (other window) |
| network, storage, power, software, user/app | DGX-B200 | link flapping/NCCL; bus error from slow FS; BIOS/power/thermal; watchdog hangs; illegal memory access (no fractions) |
| SDC | SuperBench-Azure | broken redundant IB links, qualitative gray failure |
| scheduler, CPU | Borg-2011 | low-priority task evictions (no job share); REMOVE events ambiguous with maintenance |
| CPU, GPU, power | SURF-Lisa | NODE_FAIL "rare by count", OOM unquantified; GPU >90 C 17% of time (throttle, not failure); rack cooling limits |
| CPU, storage TIME, network, data/input | Conte-FRESCO-A | OOM correlations (r=0.83); IO-rate failure peaks; exit-107 burst clusters; missing-file inside user bucket |
| CPU, storage, scheduler | UIUC-FRESCO-B | OOM correlation; remote-IO failure peak; SIGTERM user-vs-scheduler inseparable |
| GPU | NREL-Kestrel | gpu-h100 vs standard comparison enabled, not performed |
| software, storage, network, GPU, power | Marconi100 | Nagios check categories exist, no per-category counts published |
| software, CPU, power | PWA-aggregate | maintenance/software/hardware downtime unlogged in SWF |
| power, SDC | Acme | GPU overheating from ~5 C server-room rise; loss spikes / stuck training (uncounted) |

---

## 3. METRIC RE-FILINGS

1. Alibaba-PAI time 14.7: OUT of TIME matrix entirely (instance-capacity share, not time).
2. SuperBench-Azure entire COUNT column: re-basis as "defective-node % at build-out, non-exclusive"; distinct marker; excluded from cross-column comparison.
3. Philly new COUNT column: footnote "trial = failure event, retry-inflated".
4. Fire-Flyer 45.0/54.9: footnote "raw Xid event shares, not incidents/job failures".
5. Delta-A100-H100: any retained numbers are Xid-event shares (count) or node-hour shares (time), never failure shares.
6. Llama3-405B COUNT column: "as-printed Table 5 percentages; do not recompute against counts (sum ~94%)".
7. Acme TIME column: denominator = failed-job GPU time, not cluster time.
8. FRESCO A/B TIME cells: denominator = ALL node-seconds incl. successes.
9. FRESCO A/B COUNT cells: share-of-failures denominator; state per-column denominators wherever meta-row entries use share-of-jobs.
10. Mira: all RAS-derived cells footnoted as rescaled sub-taxonomy shares; TIME 32.86 = timeout core-hours of total machine core-hours.
11. DGX-B200: mixed denominators flagged (/17 Xids vs /21 failures).
12. TSUBAME-2/3 tilde values: bar-chart reads, not text-stated.
13. TwoSigma and Borg meta entries: figure-reads / termination-event bases as noted.
14. Guard list (never enter either matrix): LANL repair durations; Titan 59% replaced GPUs; Meta-RSC lemon-node Table II; Frontier screening-cost shares; SuperBench MTBI simulation; BlueWaters Gainaru event-log split; SURF-Lisa energy 50%.

---

## 4. TAXONOMY ACTIONS

Apply to the matrix now:
1. ADD the meta row "Outcome-labels & unattributed" (count + time), with dominant-class pointers. Receiving columns: Tachyon, Fugaku, Marconi100, SURF-Lisa, NREL-Eagle, NREL-Kestrel, PWA-aggregate, Helios, Alibaba-PAI, Meta-RSC, Borg-2011, Borg-2019, TwoSigma, plus unattributed entries from FRESCO (user/system indeterminate, walltime), Llama3 (NCCL 1.7, chassis), HSDP (NCCL 9.0, Unknown 1.0), Acme (NodeFailure), DGX-B200 (machine unreachable), MIT-Supercloud (<0.5 hardware bound). This is the single largest structural change and is what makes the HPC-vs-AI comparison honest: label-only traces stop masquerading as attributed data.
2. NVLink→GPU/accelerator boundary rule as a footnote (already enforced above: blocks the Delta network add; keeps Fire-Flyer Xid_74 and Llama3 NVLink in GPU).
3. SDC/fail-slow re-scoped as manifestation overlay: cells carry cross-refs (Llama3 1.4 inside GPU 58.7, excluded from sums; Unicron task-hang cross-ref; DGX 19.0 kept; Platform-X 16.6 add legitimized).
4. Preemption/eviction = policy, not failure (enforced: Marconi Preempted 0.1 removed; Borg-2019 3.2 removed; Philly preempted cells kept only with policy footnote).

Defer to prose (no matrix change): GPU-memory vs GPU-compute split; storage-device vs FS-software split (unified row + boundary footnote retained); separate facility-operations class (Host Maintenance stays in power/facility with scope note); Frontier screening data; DGX Cloud <1% figure; BlueWaters LogDiver 18.75.

---

## 5. VERDICT

The matrix is SOUND AFTER CORRECTIONS, with three qualifications.

- Of ~97 filled cells, approximately 63 (about 65%) were confirmed by at least 2 of the 3 passes (quote-verified by Verify-A and not disputed, or disputed only on denominator convention, by Verify-B). About 45% survive completely untouched (no value change, no move, no mandatory footnote): the cleanest columns are BlueWaters, TSUBAME-3, Philly TIME, Acme TIME, Meta-HSDP, FRESCO-B, and the correctly-empty Titan/Frontier/Fugaku columns.
- Hard value errors found: 6 (LANL 50 and 20 fabricated/overstated; Llama3 CPU 2.0; DGX CPU 11.8; T2 power 11.3 misclass; T2 network 8.7 undercount). Wrong-matrix errors: 1 (PAI 14.7). Non-failure entries: 2 (Marconi Preempted, Borg-2019 eviction). Systematic denominator errors: Unicron (4 cells) and the NREL aggregates (4 cells).
- The dominant defect was never fabrication (LANL aside) but basis-mixing: outcome labels filed as user/app causes, event shares filed as failure shares, and at least five distinct denominators coexisting in one COUNT matrix. The meta row plus per-column basis footnotes resolve this structurally rather than cell-by-cell.

Residual risk after corrections, estimated low-to-moderate: (a) bar-chart and figure reads carry ±1–2pp uncertainty (TSUBAME tildes, TwoSigma, PWA); (b) BlueWaters rests on abstract-level verification (paywall); (c) Llama3 as-printed percentages are internally unreconciled by ~6pp; (d) attribution softness persists in Fire-Flyer 54.9 and the FRESCO software/storage carve-out; (e) the meta-row migration itself is a new editing step that should get one mechanical re-check (row sums per column, e.g. HSDP ≈100, Llama3 ≈94 as-printed, Unicron renorms summing to ~92.4 + others 7.6) before the camera-ready. No cell that survives this list rests on an unquoted derivation.