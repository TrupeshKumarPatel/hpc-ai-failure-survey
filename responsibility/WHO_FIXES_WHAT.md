# Who Fixes What — verified remediation-responsibility mapping (research completed 2026-08-07, 108/108 agents)

Full report with quotes: `whofixes_final.json` in the authors' working repository (not part of this artifact). All findings 3-0 verified unless noted.
Primary sources: NVIDIA Xid catalog + GPU Debug Guidelines + A100 memory-error docs; NCSA Delta SC'25; Meta RSC.

## The verified triad (NVIDIA + Meta independently)
- END USER / app developer: debugs suspected programming issues (Compute Sanitizer, CUDA-GDB).
- SYSTEM OPERATOR: all immediate service restoration (drain/cordon, GPU reset, node reboot, health-check re-admission).
- VENDOR: the durable fix; NVIDIA's Field Diagnostic tool is the sole documented arbiter of RMA (row-remap thresholds: 8 rows/bank, re-fault of remapped row, 512 total; SRAM DBE threshold).

## Per class
1. Uncorrectable memory (Xid 48/94/95/64): driver auto-contains (vendor software) + user restarts killed app (94=RESTART_APP) + operator resets (48/95/64) + vendor RMA by threshold. Delta practice: SREs monitor and initiate replacement.
2. Correctable/row-remap telemetry (Xid 63): IGNORE per event — nobody acts on single events; fleet-level aggregation is operator practice (Delta SREs). Prediction value lives at fleet level.
3. NVLink (Xid 74): operator reset/reboot; vendor only if persistent.
4. Off-bus/PCIe (Xid 79): operator restart-bare-metal; then vendor (chiefly PCIe hardware).
5. GSP/driver (Xid 119/120): operator reset/power-cycle immediate; durable fix = NVIDIA driver updates.
6. MMU/illegal access (Xid 13/31/43): end user/app developer primary. DOCUMENTED INTRA-NVIDIA DIVERGENCE: Xid catalog routes 13/31 to the developer first; GPU Debug Guidelines route 13 through operator diagnostics and 31 to the vendor.
7-8. Network + filesystem, node-level manifestations: operator automated health checks own immediate remediation. Fabric-wide/Lustre-wide outages: NO verified owner.
9. Application faults + walltime: end user (vendor and operator sources agree).
10. Correlated fleet/batch defects: NO verified owner attribution survived.
11. Silent data corruption: NO verified owner attribution survived.

## The headline gap (verified absence, low-confidence only because it is an absence)
No surviving verified source assigns ANY remediation role to middleware/library developers (MPI, NCCL, checkpoint libraries, schedulers) for any class. The recovery layer between operator reset and vendor RMA is undocumented — that unowned layer is where fault-tolerance research (communicator repair, shrink semantics, prediction-driven mitigation) operates.
