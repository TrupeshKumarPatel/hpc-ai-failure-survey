# Reading Guide — the rework figures, in plain words

## The one idea behind everything

Papers report "failures" in three different ways, and mixing them was what made the old map unreadable:

1. **Cause data** — the paper says *why* things failed ("30% faulty GPU, 17% HBM memory..."). Only ~20 systems in the world publish this.
2. **Outcome labels** — the scheduler recorded *that* jobs failed (FAILED, TIMEOUT), but nobody knows why. ~18 systems.
3. **Rates only** — the paper gives MTBF or error counts ("a double-bit error every 160 hours") but no percentage breakdown. These can't go on a share map at all.

The old map forced all three into one grid, so most of it was gray. The rework gives each kind its own place.

## Figure A (figA_causes) — the main result

Only the ~20 clusters that actually publish cause-attributed shares. Read one column at a time: it shows where that cluster's failures come from. What you should see:

- Left side (traditional HPC): the **user/application** row carries the weight (Mira 99%, UIUC 48%, Conte 33%). Hardware is small.
- Right side (AI training): the **GPU/accelerator hardware** row lights up (Llama-3 59%, DGX/B200 59%, Fire-Flyer 45%, Minder 39%, ByteRobust 36%). The two TSUBAME columns are the bridge: early GPU-heavy HPC already looked like the AI side.
- Do NOT compare exact numbers across columns — each study counts against its own denominator. Compare the *shape* of columns.

## Figure B (figB_labels) — the honest second tier

The 18 clusters that only have outcome labels. One bar each: the share of jobs their scheduler marked failed/unsuccessful. Range is ~1% (Borg, but that's an artifact of Google's KILL-heavy accounting) to ~32% (Trinity). These bars can NEVER say why jobs failed — that is precisely the paper's data-gap argument.

## What's not in any figure, and why

- **Rates-only systems** (Titan, Frontier, Delta, LANL 22-systems, GWA, Backblaze, the SSD/SDC fleet studies): they publish MTBFs, event counts, or per-device rates, not shares. They appear in the side notes and prose, not the map. Forcing them in would mean inventing percentages.
- **Insufficient systems** (ALCF Polaris, ALCF Theta, Alibaba v2018): checked directly; no published outcome or cause shares exist. Documented in ledger.md with the evidence.
- Full entry-by-entry accounting of all 162 catalog entries: [`../survey/ledger.md`](../survey/ledger.md) / [`../survey/ledger.csv`](../survey/ledger.csv).

## Markers (only four)

`~` read off a bar chart (±1–2 points). `*` computed from a raw public trace, or shares of events rather than jobs. `<` upper bound. `†` printed value the paper doesn't reconcile internally (Llama-3 only).

## Where each number comes from

Every cell traces to a quoted source statement. The 33 original columns were triple-verified; see [`../verification/verification_report.md`](../verification/verification_report.md). The 11 columns added later to close coverage gaps carry the same per-cell quotes and were independently re-derived and adjudicated in a separate pass. The raw extraction records behind both (`matrix_notes.md`, `phase2_extracts_all.json`) live in the authors' working repository and are not part of this artifact.
