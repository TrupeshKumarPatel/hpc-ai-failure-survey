# HPC-AI Failure Survey — Evidence Artifact

The complete evidence bundle behind the SC26 research poster **"Do AI Workloads
Fail Differently? A Cross-Cluster Characterization of Failure Types in AI and
HPC Systems"** and its companion FTXS'26 workshop paper **"Characterizing
Failure Types Across HPC and AI Clusters"** (Trupesh Patel and Purushotham V. Bangalore, The University
of Alabama).

Every quantitative claim in the poster and paper traces to a file in this
repository, and every matrix cell traces to a quoted sentence in its published
source.

Looking for the datasets themselves? [**`survey/INDEX.md`**](survey/INDEX.md) lists all 162
entries with links; [`survey/dataset_catalog.md`](survey/dataset_catalog.md) describes what each one contains.

## Contents

| Path | What it is |
|---|---|
| **[`survey/INDEX.md`](survey/INDEX.md)** | **Start here.** All **162** surveyed datasets and operational reports in one browsable table, grouped by evidence verdict, with a link to each source. |
| `survey/dataset_catalog.md` | What each entry actually is: organization, system, period, scale, contents, what failure information it carries, access terms and URLs, and caveats. |
| `survey/ledger.csv`, `survey/ledger.md` | The verdict per entry with its justification: 20 cause-attributed, 25 outcome-label only, 44 rates-only, 36 no failure information, 19 duplicates, 8 paper-statistics only, 10 umbrella repositories. |
| `taxonomy/failure_type_taxonomy.md` | 88 canonical failure types in 11 classes, each with its class-assignment rationale and a cause / symptom / outcome-label tag. |
| `taxonomy/raw_type_enumeration.md` | The 931 raw failure-type mentions enumerated verbatim from 37 studies, before canonicalization. |
| `matrices/matrix_count_v3.csv` | Failure-class shares by count basis, 44 system columns; each column keeps its source's own denominator. |
| `matrices/matrix_time_v3.csv` | The time-basis (lost compute / GPU-hours / node-hours) view. |
| `matrices/gpu_matrix_design.md` | The GPU error-class matrix (12 systems, 11 classes, K20X to B200) with design rationale and per-cell source quotes. |
| `verification/verification_report.md` | The three-pass verification protocol (per-cell quote audit, blind re-derivation, adjudication) and the six value errors it caught and corrected. |
| `responsibility/WHO_FIXES_WHAT.md` | The who-fixes-what mapping: each failure class to its documented remediation owner (application developer / operator / vendor), from NVIDIA and site documentation, including documented points of divergence. |
| `figures/` | The three poster figures and the matplotlib script that regenerates them from the matrices (`python figures/render_final_figs.py`; requires Python 3 + matplotlib + numpy). |

## Reading the matrices

The surveyed studies report against five incompatible bases (failures, jobs,
interruptions, raw error events, defective nodes). **Columns are never
comparable to each other** — each keeps its own denominator, stated per column.
Compare within a column only. Values marked `~` are chart reads (1–2 pp
uncertainty), `*` are counted from raw public traces, `<` are upper bounds.

## Provenance and license

All values derive from published, publicly accessible sources: peer-reviewed
failure studies, arXiv operational reports, public dataset documentation, and
vendor documentation. No proprietary or personal data is included. Quoted
sentences remain the property of their original publishers and are reproduced
as short excerpts for verifiability.

Original content in this repository is licensed under CC BY 4.0.
