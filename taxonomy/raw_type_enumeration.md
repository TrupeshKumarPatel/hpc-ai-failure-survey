# Appendix 08a: Raw Failure-Type Enumeration (all 931 mentions)

Every failure-type mention found across the 37 studies + catalog, exactly as each source names it. One row per mention per source. This is the ground truth behind [`failure_type_taxonomy.md`](failure_type_taxonomy.md).

| Raw name | Source | Layer hint | Share/rate | Evidence |
|---|---|---|---|---|
| Infrastructure (category) | Acme (Hu et al., NSDI'24) | hardware | 281 occurrences (~11% of failed jobs), ~82% of failure GPU time | Failure type table row: 'Failures from the computational platform or remote storage' |
| Framework (category) | Acme (Hu et al., NSDI'24) | software | 404 occurrences, ~14.7% of failure GPU time | Table row: runtime errors tied to tensor ops, shapes, dtypes |
| Script (category) | Acme (Hu et al., NSDI'24) | user/app | 1,890 occurrences, ~3.2% of failure GPU time | Table row: programming errors or user oversights; fail fast at job start |
| NVLinkError | Acme (Hu et al., NSDI'24) | hardware | Num=54, 30.25% of failure GPU time (S,K) | Table row: top GPU-time consumer; linked to GPU overheating in Kalos July 2023 |
| CUDAError | Acme (Hu et al., NSDI'24) | hardware | Num=21, 15.77% (S,K) | Table row: often the true root cause behind NCCLTimeout/RuntimeError cascades |
| NodeFailure | Acme (Hu et al., NSDI'24) | unknown | Num=16, 14.30% (S only) | Table row: 'uncategorized errors caused by unclear hardware issues' |
| ECCError | Acme (Hu et al., NSDI'24) | hardware | Num=12, 11.00% (S,K) | Table row: GPU memory ECC; longest-lived failures (TF avg 1303.4 min); tied to overheating |
| NetworkError | Acme (Hu et al., NSDI'24) | network | Num=12, 4.53% (S,K) | Table row: many stem from auxiliary services (metric reporting, logging, monitoring, alerting) |
| ConnectionError | Acme (Hu et al., NSDI'24) | network | Num=147, 3.44% (S,K) | Table row: most frequent infrastructure error by count; auxiliary-service network instability |
| S3StorageError | Acme (Hu et al., NSDI'24) | storage/IO | Num=10, 2.12% (S only) | Table row: remote storage failures; longest average time-to-failure (TF avg 2317.8 min) |
| NCCLTimeoutError | Acme (Hu et al., NSDI'24) | network | Num=6, 0.50% (K only) | Table row: collective-communication timeout |
| NCCLRemoteError | Acme (Hu et al., NSDI'24) | network | Num=3, 0.15% (K only) | Table row: remote NCCL failure, classed with network-system hardware issues |
| DataloaderKilled | Acme (Hu et al., NSDI'24) | software | Num=6, 4.38% (K only) | Table row: costliest framework failure per incident (TF avg 1580.6 min, avg 445 GPUs) |
| AttributeError | Acme (Hu et al., NSDI'24) | software | Num=67, 3.90% (S,K) | Table row: framework runtime error, mostly fails at startup |
| OutofMemoryError | Acme (Hu et al., NSDI'24) | software | Num=14, 3.28% (S,K) | Table row: framework; avg 572 GPUs |
| RuntimeError | Acme (Hu et al., NSDI'24) | software | Num=65, 1.72% (S,K) | Table row: tensor ops/shape/dtype errors |
| AssertionError | Acme (Hu et al., NSDI'24) | software | Num=105, 1.24% (S,K) | Table row: TR/TF 445.87% — restarts far costlier than time-to-failure |
| ValueError | Acme (Hu et al., NSDI'24) | software | Num=33, 0.16% (S,K) | Table row: framework config error |
| ZeroDivisionError | Acme (Hu et al., NSDI'24) | software | Num=5, 0.03% (S,K) | Table row: framework; TF avg 14.5 min |
| ModelLoadingError | Acme (Hu et al., NSDI'24) | software | Num=104, 0.00% (K only) | Table row: frequent but tiny jobs, negligible GPU time |
| DatasetLoadingError | Acme (Hu et al., NSDI'24) | software | Num=5, 0.00% (K only) | Table row: single-GPU, TF avg 1.6 min |
| FileNotFoundError | Acme (Hu et al., NSDI'24) | user/app | Num=568, 2.83% (S,K) | Table row: second-most-frequent error overall; user oversight |
| OSError | Acme (Hu et al., NSDI'24) | user/app | Num=266, 0.28% (S,K) | Table row: script category |
| TypeError | Acme (Hu et al., NSDI'24) | user/app | Num=620, 0.06% (S,K) | Table row: most frequent single error type by count; fails almost immediately |
| NameError | Acme (Hu et al., NSDI'24) | user/app | Num=18, 0.02% (S,K) | Table row: script; TF avg 3.2 min |
| PermissionError | Acme (Hu et al., NSDI'24) | user/app | Num=7, 0.01% (S only) | Table row: script; TF avg 4.3 min |
| ImportError | Acme (Hu et al., NSDI'24) | user/app | Num=111, 0.01% (S,K) | Table row: script; TF avg 1.1 min |
| KeyError | Acme (Hu et al., NSDI'24) | user/app | Num=260, 0.01% (S,K) | Table row: script; TF avg 3.0 min |
| SyntaxError | Acme (Hu et al., NSDI'24) | user/app | Num=10, 0.00% (S,K) | Table row: script; TF avg 0.7 min |
| ArgumentError | Acme (Hu et al., NSDI'24) | user/app | Num=3, 0.00% (S only) | Table row: script; TF avg 0.7 min |
| CalledProcessError | Acme (Hu et al., NSDI'24) | user/app | Num=4, 0.00% (S only) | Table row: extreme restart-to-failure ratio (TR/TF 5714.29%) |
| IndexError | Acme (Hu et al., NSDI'24) | user/app | Num=23, 0.00% (S,K) | Table row: script; TF avg 1.6 min |
| Loss spike (training-metric anomaly that doesn't recover) | Acme (Hu et al., NSDI'24) | user/app |  | Recovery notes: restart trigger (2); mitigated by rolling back to an earlier healthy checkpoint and skipping offending data batches |
| Stuck training | Acme (Hu et al., NSDI'24) |  |  | Recovery notes: restart trigger (3) 'stuck training' |
| CUDA error | MegaScale (Jiang et al., NSDI'24) | software | no count given; example within the 'over 90%' of exceptions auto-detected/recovered | Table row: runtime CUDA errors surfaced in stdout/stderr, caught by log filtering rules |
| Segmentation fault | MegaScale (Jiang et al., NSDI'24) | software | no count given; second named example in the auto-recovered >90% class | Table row: process crashes detected via log parsing and missing heartbeats |
| NCCL communication timeout | MegaScale (Jiang et al., NSDI'24) | network | no count given | Table row: collectives hang/timeout; default NCCL timeout too aggressive at scale, must be raised |
| Network interface flapping (frequent network interface flaps) | MegaScale (Jiang et al., NSDI'24) | network | no rate given; recurring in production | Table row: NIC link down/up within seconds; bad link quality between NIC, AOC cable, and switch |
| Hardware anomalies that manifest probabilistically | MegaScale (Jiang et al., NSDI'24) | hardware | residual <10% of faults not caught by machine self-checks | Table row: faulty GPUs/hosts that pass self-checks but fail under load |
| Computational stragglers | MegaScale (Jiang et al., NSDI'24) | hardware | ~0.5% of machines, ~10% slower; excluding them improved MFU by ~0.7% | Table row: silent performance degraders found with CUDA-event-based performance diagnosis |
| Gradual MFU decrease over training (silent performance anomaly) | MegaScale (Jiang et al., NSDI'24) | user/app | no number; MFU 'gradually decreased' | Table row: ranks initiated reduce-scatter late (time skew, GC/PyTorch fluctuations); system appeared normal while efficiency degraded |
| OOM (out of memory) | Meta-RSC (arXiv:2410.21680) | user/app | 0.1% of jobs end in Slurm OOM state (RSC-1) | Table row: Taxonomy Table I attributes OOM to user program only; also a distinct Slurm terminal state |
| GPU Unavailable | Meta-RSC (arXiv:2410.21680) | hardware | not individually quantified | Table row: attributed to system software OR hardware infrastructure in Table I |
| GPU Memory Errors | Meta-RSC (arXiv:2410.21680) | hardware | among top contributors; not individually quantified | Table row: uncorrectable GPU memory/ECC symptoms |
| GPU Driver/Firmware Error | Meta-RSC (arXiv:2410.21680) | software | not individually quantified | Table row: system-software domain in Table I |
| GPU NVLink Error | Meta-RSC (arXiv:2410.21680) | hardware | not individually quantified | Table row: hardware-infrastructure domain; XID 74-class events discussed |
| Infiniband Link | Meta-RSC (arXiv:2410.21680) | network | a dominant category in Fig. 4; summer-2024 spike driven by 'a handful of nodes' | Table row: IB link flaps/downs on the backend fabric |
| Filesystem Mounts | Meta-RSC (arXiv:2410.21680) | storage/IO | 'became a key failure mode on RSC-1' after the mount health check was added | Table row: stale/failed FS mounts detected by health checks |
| Main Memory Errors | Meta-RSC (arXiv:2410.21680) | hardware | not individually quantified (DIMM = 20.5% of lemon-node root causes) | Table row: host DRAM/DIMM uncorrectable errors |
| Ethlink Errors | Meta-RSC (arXiv:2410.21680) | network | not individually quantified | Table row: Ethernet (frontend) link errors |
| PCIe Errors | Meta-RSC (arXiv:2410.21680) | hardware | 43% (RSC-1) / 63% (RSC-2) co-occur with GPU XID 79 | Table row: PCIe bus errors strongly correlated with GPU-off-bus events |
| NCCL Timeout | Meta-RSC (arXiv:2410.21680) | unknown | not individually quantified | Table row: Table I marks all three domains — network, or another rank stuck/never started; attribution ambiguous |
| System Services | Meta-RSC (arXiv:2410.21680) | software | not individually quantified | Table row: node system-service failures; can arise from any of the three domains |
| NODE_FAIL (Slurm state, infra failure) | Meta-RSC (arXiv:2410.21680) | hardware | 0.1% of jobs; infra failures overall = 0.2% of jobs but 18.7% of runtime | Table row: scheduler-visible node death |
| Job status mix (context) | Meta-RSC (arXiv:2410.21680) | user/app | RSC-1: 60% completed, 24% failed, 10% preempted, 2% requeued, 0.6% timeout | Table row: most job failures are application-level, not infrastructure |
| Lemon-node root causes (Table II) | Meta-RSC (arXiv:2410.21680) | hardware | GPU 28.2%, DIMM 20.5%, PCIe 15.4%, EUD 10.3%, BIOS 7.7%, NIC 7.7%, PSU 5.1%, Optics 2.6% | Table row: breakdown of the 40 identified lemon (repeat-offender) nodes |
| GPU XID 79 ('GPU fell off the bus') | Meta-RSC (arXiv:2410.21680) | hardware | co-occurs with 43%/63% of PCIe errors on RSC-1/RSC-2 | PCIe Errors row detail: co-occurrence with GPU XID 79 and IPMI Critical Interrupt |
| GPU XID 74-class events | Meta-RSC (arXiv:2410.21680) | hardware | discussed but not rate-quantified | GPU NVLink Error row detail: 'XID 74-class events discussed but not rate-quantified' |
| IPMI Critical Interrupt | Meta-RSC (arXiv:2410.21680) | hardware | 21% of PCIe errors co-occur with PCIe + XID 79 + IPMI Critical Interrupt simultaneously | PCIe Errors row detail: simultaneous triple co-occurrence |
| FAILED (Slurm state, application exit code) | Meta-RSC (arXiv:2410.21680) | user/app | 24% of RSC-1 jobs | Job status mix row: '24% failed (application exit code)' |
| Preempted (Slurm state) | Meta-RSC (arXiv:2410.21680) | user/app | 10% of RSC-1 jobs | Job status mix row: '10% preempted' |
| Requeued (Slurm state) | Meta-RSC (arXiv:2410.21680) | user/app | 2% of RSC-1 jobs | Job status mix row: '2% requeued' |
| Timeout (Slurm state) | Meta-RSC (arXiv:2410.21680) | user/app | 0.6% of RSC-1 jobs | Job status mix row: '0.6% timeout' |
| Faulty GPU | Llama 3 (arXiv:2407.21783, Table 5) | hardware | 148 (30.1%) | Table row: GPU failures including falling off the bus (category: GPU) |
| GPU HBM3 Memory | Llama 3 (arXiv:2407.21783, Table 5) | hardware | 72 (17.2%) | Table row: HBM3 memory faults on GPU |
| Software Bug | Llama 3 (arXiv:2407.21783, Table 5) | software | 54 (12.9%) | Table row: bugs in training software stack (category: Dependency) |
| Network Switch/Cable | Llama 3 (arXiv:2407.21783, Table 5) | network | 35 (8.4%) | Table row: RoCE fabric switch and cable failures |
| Host Maintenance | Llama 3 (arXiv:2407.21783, Table 5) | facility | 32 (7.6%) | Table row: unplanned host maintenance events (category: Unplanned Maintenance) |
| GPU SRAM Memory | Llama 3 (arXiv:2407.21783, Table 5) | hardware | 19 (4.5%) | Table row: GPU on-chip SRAM faults |
| GPU System Processor | Llama 3 (arXiv:2407.21783, Table 5) | hardware | 17 (4.1%) | Table row: GPU system processor failures |
| NIC | Llama 3 (arXiv:2407.21783, Table 5) | hardware | 7 (1.7%) | Table row: host network interface card failures (category: Host) |
| NCCL Watchdog Timeouts | Llama 3 (arXiv:2407.21783, Table 5) | unknown | 7 (1.7%) | Table row: collective-communication hangs with undetermined root cause (category: Unknown) |
| Silent Data Corruption | Llama 3 (arXiv:2407.21783, Table 5) | hardware | 6 (1.4%) | Table row: SDC producing wrong results without error signal |
| GPU Thermal Interface + Sensor | Llama 3 (arXiv:2407.21783, Table 5) | hardware | 6 (1.4%) | Table row: GPU thermal interface/sensor faults |
| SSD | Llama 3 (arXiv:2407.21783, Table 5) | storage/IO | 3 (0.7%) | Table row: host SSD failures (category: Host) |
| Power Supply | Llama 3 (arXiv:2407.21783, Table 5) | hardware | 3 (0.7%) | Table row: host power supply failures |
| Server Chassis | Llama 3 (arXiv:2407.21783, Table 5) | hardware | 2 (0.5%) | Table row: server chassis faults |
| IO Expansion Board | Llama 3 (arXiv:2407.21783, Table 5) | hardware | 2 (0.5%) | Table row: IO expansion board faults |
| Dependency | Llama 3 (arXiv:2407.21783, Table 5) | software | 2 (0.5%) | Table row: external dependency failures |
| CPU | Llama 3 (arXiv:2407.21783, Table 5) | hardware | 2 (0.5%) | Table row: host CPU failures |
| System Memory | Llama 3 (arXiv:2407.21783, Table 5) | hardware | 2 (0.5%) | Table row: host DRAM failures |
| NVLink failures (stalled point-to-point transfers, not fail-fast errors) | Llama 3 (arXiv:2407.21783) | hardware |  | Recovery notes: 'special detection tooling for NVLink failures (which manifest as stalled point-to-point transfers rather than fail-fast errors)' |
| Mixed NCCL/NVLink hangs | Llama 3 (arXiv:2407.21783) | network |  | Recovery notes: tooling 'for mixed NCCL/NVLink hangs' |
| Stragglers (slow-but-not-failed communicators) | Llama 3 (arXiv:2407.21783) | hardware |  | Recovery notes: 'straggler-detection tools built on NCCLX to identify slow-but-not-failed communicators' |
| Diurnal throughput variation from midday temperature (GPU dynamic frequency scaling) | Llama 3 (arXiv:2407.21783) | facility | 1-2% throughput variation | Recovery notes: 'environmental effects that degrade rather than fail: 1-2% diurnal throughput variation from midday temperature' |
| Datacenter power fluctuations from synchronized GPU idle/busy transitions | Llama 3 (arXiv:2407.21783) | facility | tens-of-MW instantaneous | Recovery notes: 'tens-of-MW instantaneous datacenter power fluctuations... during checkpointing and collective startup/teardown' |
| finish successfully | Unicron (arXiv:2401.00134) | user/app | 56.6% | Table row: complement of the 43.4% abnormal-termination rate (Figure 1) |
| NCCL timeout | Unicron (arXiv:2401.00134) | network | 10.1% | Table row: largest single failure cause; detection delayed up to 30 min by all-reduce timeout; SEV3 |
| ECC errors | Unicron (arXiv:2401.00134) | hardware | 5.0% | Table row: GPU memory ECC faults; SEV1 — triggers node isolation/reconfiguration |
| NVLink errors | Unicron (arXiv:2401.00134) | hardware | 4.5% | Table row: GPU interconnect failures; SEV1 |
| other network errors | Unicron (arXiv:2401.00134) | network | 4.0% | Table row: residual network error bucket; SEV3 |
| link flapping | Unicron (arXiv:2401.00134) | network | 3.9% | Table row: intermittent network link up/down; SEV3, remediable by in-place reattempt |
| others | Unicron (arXiv:2401.00134) | unknown | 3.3% | Table row: uncharacterized residual category, not broken down |
| task hang | Unicron (arXiv:2401.00134) | software | 3.1% | Table row: process stalls without exiting; caught by 3x-average-iteration-time threshold; SEV2 |
| illegal memory access | Unicron (arXiv:2401.00134) | user/app | 2.1% | Table row: CUDA illegal memory access exceptions; SEV2 — restart process on affected node |
| invalid DMA mapping | Unicron (arXiv:2401.00134) | hardware | 2.1% | Table row: DMA mapping faults (driver/hardware boundary); SEV1 |
| connection refused | Unicron (arXiv:2401.00134) | network | 2.1% | Table row: TCP connection refused; SEV3 transient, reattempt in-place |
| CUDA errors | Unicron (arXiv:2401.00134) | software | 1.6% | Table row: generic CUDA runtime errors; SEV2 |
| connection reset | Unicron (arXiv:2401.00134) | network | 1.0% | Table row: TCP connection reset; SEV3 transient |
| GPU driver errors | Unicron (arXiv:2401.00134) | software | 0.6% | Table row: driver-level faults; SEV1 despite small share (node must be drained) |
| transient faults (cross-cutting split) | Unicron (arXiv:2401.00134) | unknown | 73% of all errors | Table row: 'typically remediable by restarting the system'; restart path costs ~68 min downtime |
| hardware faults requiring node drainage (cross-cutting split) | Unicron (arXiv:2401.00134) | hardware | node drainage needed in 37% of cases | Table row: labor-intensive recovery (manual fault ID, node drain, Megatron down-scaling, checkpoint realignment) |
| lost connection (SEV1) | Unicron (arXiv:2401.00134) | network |  | Recovery notes, Table 1 severity list: 'SEV1 (lost connection, ECC, invalid DMA mapping, NVLink, GPU driver)' |
| exited abnormally (SEV2) | Unicron (arXiv:2401.00134) | software |  | Recovery notes, Table 1 severity list: 'SEV2 (exited abnormally, illegal memory access, CUDA errors, task hang, other software errors)' |
| other software errors (SEV2) | Unicron (arXiv:2401.00134) | software |  | Recovery notes, Table 1 severity list: SEV2 category includes 'other software errors' |
| Training crash (symptom) | L4 | user/app | 57.5% of 428 failures | Table row: 'Job crashes after iterative training starts, often from hardware faults; single local fault (GPU, network router) kills whole synchronous job' |
| Launching failure (symptom) | L4 | software | 21.3% of 428 failures | Table row: 'Failures before iterative training, e.g., GPU driver/CUDA toolkit version mismatch at env init, model-parallelism misconfiguration at model loading' |
| Abnormal behavior (symptom) | L4 | unknown | 16.6% of 428 failures | Table row: 'Hangs and slowdowns: epoch takes 2x longer, or training stalls at an iteration with no RDMA traffic' |
| Others (symptom) | L4 | facility | 4.7% of 428 failures | Table row: 'Failures not tied to a specific training job, e.g., platform or remote-storage unavailability' |
| Hardware fault (root cause) | L4 | hardware | Most common root cause (exact % withheld) | Table row RQ2: 'much higher than reported in previous studies'; four named sub-types (Network, Accelerator, Node, Storage) |
| Network Fault (hardware sub-type) | L4 | hardware | most common hardware sub-type | Table detail: "Network Fault (most common hardware sub-type; 'NIC port link down', 'increased pcs_err_cnt')" |
| Accelerator Fault (hardware sub-type) | L4 | hardware | one of the two most prevalent sub-types (Finding 2) | Table detail: "ECC/stuck-at memory errors, power faults; 'double bit ecc error', 'Aicore kernel execute failed'" |
| Node Fault (hardware sub-type) | L4 | hardware |  | Table detail: 'mainboard damage, power leakage, disk errors; detected via missing heartbeats since failed node is unreachable' |
| Storage Fault (hardware sub-type) | L4 | hardware |  | Table detail: "remote distributed storage; 'Failed to load checkpoint'" |
| User fault (root cause) | L4 | user/app | Second largest root cause (exact % withheld) | Table row RQ2 with four named sub-types (Configuration Error, Program/Script Bug, Software Incompatibility, Misoperation) |
| Configuration Error (user-fault sub-type) | L4 | user/app |  | Table detail: 'Configuration Error (e.g., low Notify-register timeout)' |
| Program/Script Bug (user-fault sub-type) | L4 | user/app |  | Table detail: 'most bugs in user-modified parts of adopted code: error paths, null refs, inconsistent model params' |
| Software Incompatibility (user-fault sub-type) | L4 | user/app |  | Table detail: 'version mismatches across OS image/driver/framework/toolkit' |
| Misoperation (user-fault sub-type) | L4 | user/app |  | Table detail: 'e.g., external checkpoint storage without access permissions' |
| Framework fault (root cause) | L4 | software | Small proportion (exact % withheld) | Table row: 'Bugs in training frameworks (PyTorch, DeepSpeed, customized ones like CNTK); customized frameworks more fault-prone' |
| Platform fault (root cause) | L4 | software | Least proportion (exact % withheld) | Table row: 'Resource-management logic bugs, job-scheduling anomalies (abnormal preemption), platform config defects (network settings)' |
| Diagnosability split (RQ3) | L4 | unknown | 53.9% log-only / 36.0% hybrid / 10.1% non-log diagnosable | Table row: 'Logs are useful for 89.9% of failures; of failure-indicating logs: 54.8% error level, 13.6% info, 8.5% debug' |
| HCCP/ROCE errors ('ROCE(,hccp_service.bin):error cqe status') | L4 | network |  | Header prose lists 'HCCP/ROCE errors' as Huawei Ascend signatures; recovery notes deployment case: L4 isolated 8 divergent nodes with 'ROCE(,hccp_service.bin):error cqe status' |
| Notify register timeout | L4 | user/app |  | Header prose: log examples ('Aicore kernel execute failed', Notify register timeout, HCCP/ROCE errors) are Huawei Ascend NPU signatures |
| GPU HBM3 Memory | HSDP (Meta FT-HSDP) | hardware | 155 (22.9%) | Table row: 'GPU high-bandwidth memory errors; single largest interruption cause' |
| PCIe Device | HSDP (Meta FT-HSDP) | hardware | 122 (18.0%) | Table row: 'PCIe device faults on the host' |
| NCCL Watchdog Timeouts | HSDP (Meta FT-HSDP) | software | 61 (9.0%) | Table row: 'Collective-communication watchdog timeouts (symptom category; root cause often hw/network)' |
| Faulty GPU Compute | HSDP (Meta FT-HSDP) | hardware | 50 (7.4%) | Table row: 'GPU compute-unit faults' |
| Software Bug | HSDP (Meta FT-HSDP) | user/app | 48 (7.1%) | Table row: 'Bugs in training software stack' |
| Host Maintenance | HSDP (Meta FT-HSDP) | facility | 42 (6.2%) | Table row: 'Host maintenance events interrupting the job' |
| Kernel Fault | HSDP (Meta FT-HSDP) | software | 39 (5.8%) | Table row: 'OS kernel faults' |
| System Reboot | HSDP (Meta FT-HSDP) | software | 38 (5.6%) | Table row: 'Unexpected host reboots' |
| Numerics/Silent Data Corruption | HSDP (Meta FT-HSDP) | hardware | 37 (5.5%) | Table row: 'SDC / numerical corruption events' |
| Network Switch/Cable | HSDP (Meta FT-HSDP) | network | 36 (5.3%) | Table row: 'Fabric switch and cable failures' |
| SSD | HSDP (Meta FT-HSDP) | storage/IO | 30 (4.4%) | Table row: 'Local SSD failures' |
| GPU SRAM Memory | HSDP (Meta FT-HSDP) | hardware | 8 (1.2%) | Table row: 'GPU on-die SRAM errors' |
| Unknown | HSDP (Meta FT-HSDP) | unknown | 7 (1.0%) | Table row: 'Undiagnosed interruptions' |
| System Memory | HSDP (Meta FT-HSDP) | hardware | 2 (0.3%) | Table row: 'Host DRAM errors' |
| System Cooling | HSDP (Meta FT-HSDP) | facility | 2 (0.3%) | Table row: 'Cooling failures' |
| GPU Thermal Interface + Sensor | HSDP (Meta FT-HSDP) | hardware | 1 (0.2%) | Table row: 'GPU thermal interface/sensor fault' |
| Stall-time inflation from bugs and power-smoother overhead (98K-GPU run) | HSDP (Meta FT-HSDP) | software |  | Caveats: 'Measured 98K-GPU stall time exceeded expectation; post-hoc analysis attributed inflation to bugs and power-smoother overhead' |
| NVLink Error (Xid_74) | Fire-Flyer | hardware | 5,521 events, 42.57% of total Xid errors | Table row: 'Errors on the NVLink Bridge connecting paired PCIe A100s; inherent connector fault rate several orders of magnitude higher' |
| Software Causes - Xid_43 (illegal memory access) | Fire-Flyer | user/app | 4,342 events, 33.48% | Table row: 'Application-triggered; standout software error... but may also mask hardware memory corruption' |
| Software Causes - Xid_31 | Fire-Flyer | user/app | 2,487 events, 19.18% | Table row: 'Application-program-triggered GPU memory anomaly (fifo/MMU error class)' |
| Software Causes - Xid_13 | Fire-Flyer | user/app | 45 events, 0.35% | Table row: 'Application-triggered (graphics engine exception class)' |
| Software Causes - Xid_45 | Fire-Flyer | user/app | 240 events, 1.85% | Table row: 'Application-triggered (preempted/aborted channels). Software-cause group total: 7,114 events, ~54.9%' |
| GPU Memory ECC Error (Xid_63/64/94/95) | Fire-Flyer | hardware | 277 events: xid_63=245 (1.89%), xid_64=2 (0.02%), xid_94=13 (0.10%), xid_95=17 (0.13%) - ~2% of total | Table row: 'with A100 row remapping most instances resolved by a simple GPU reset; GPU ECC faults considerably surpass CPU ECC faults' |
| Uncorrectable GPU Failures (Xid_44/48/61/62/69/79) | Fire-Flyer | hardware | 57 events: xid_44=1, xid_48=2, xid_61=13, xid_62=3, xid_69=1, xid_79=37 (0.29%); group ~0.45% | Table row: 'Uncorrectable GPU error reported back to the user application; requires GPU reset or node reboot to clear' |
| Other Failures - GPU GSP Error (Xid_119) | Fire-Flyer | hardware | 1 event, 0.01% | Table row: 'GPU GSP module failure; needs fieldiag test and usually RMA replacement' |
| IB Network Flash Cut (link failures) | Fire-Flyer | network | 30% of hardware faults excluding Xid_74; 89 flash cuts Oct 2023-Mar 2024; ~200 IB link failure events/year | Table row: 'IB link flaps disrupt application communication and kill multi-node tasks' |
| Main Memory (CPU) ECC errors | Fire-Flyer | hardware | 54 events in Oct 2023-Mar 2024 (Table VII total = 292) | Table row: 'Host DRAM ECC errors; far fewer than GPU ECC faults over the same window' |
| SDC not caught by ECC (gradnorm spikes, loss explosions, non-convergence) | Fire-Flyer | hardware | invisible in the Xid taxonomy | Caveats: 'Authors report SDC not caught by ECC (computational and GPU-memory errors) that caused gradnorm spikes, loss explosions, and non-convergence' |
| NVLink errors (Xid 145, 149) | DGX-B200 (Kang et al. 504xB200) | hardware | 5 of 17 (29.4%) | Table row: 'Most prevalent category; contrast: Minder's top category was ECC at 38.9%' |
| ECC errors (Xid 94) | DGX-B200 (Kang et al. 504xB200) | hardware | 2 of 17 (11.8%) | Table row: 'Uncorrectable GPU memory ECC; small sample due to short observation window' |
| GPU card dropout (Xid 79) | DGX-B200 (Kang et al. 504xB200) | hardware | 2 of 17 (11.8%) | Table row: 'GPU falls off the bus' |
| GPU execution errors (Xid 119) | DGX-B200 (Kang et al. 504xB200) | hardware | 1 of 17 (5.9%) | Table row: 'GSP RPC timeout class execution error' |
| Machine unreachable | DGX-B200 (Kang et al. 504xB200) | hardware | 2 of 17 (11.8%) | Table row: 'Whole node unresponsive; no Xid recorded' |
| Others (performance degradation) | DGX-B200 (Kang et al. 504xB200) | unknown | 5 of 17 (29.4%) | Table row: 'Degradation events without a specific Xid signature' |
| GPU hardware failures (broader event count) | DGX-B200 (Kang et al. 504xB200) | hardware | 13 of 21 failures (10 with Xid detection, 3 without) | Table row: "'21 failures across 14 cluster downtimes' = 13 GPU hardware + 4 fail-slow + 4 unknown" |
| Fail-slow events | DGX-B200 (Kang et al. 504xB200) | hardware | 4 of 21 | Table row: 'Slowdowns rather than crashes; motivates multi-signal detection since no single metric dominates' |
| Failures of unknown cause | DGX-B200 (Kang et al. 504xB200) | unknown | 4 of 21 | Table row: 'Root cause never established' |
| Checkpoint I/O bottleneck (NFS RPC slot saturation) | DGX-B200 (Kang et al. 504xB200) | storage/IO | 523 checkpoint events / 55 days; loads use ~10% (peak 14.7%) of 1,500 GB/s NFS max | Table row: '128-slot NFS RPC layer saturates (RPC slot wait = 92.2% of 1,621 ms per-request save latency); mean checkpoint LOAD = 33 min' |
| Immediate crashes (bucket 1: BIOS/power/thermal faults, uncorrectable ECC, silent data corruption/NaNs, network link flapping) | NVIDIA DGX Cloud blog | hardware | no fractions given | Table row: 'BIOS/power/thermal faults, uncorrectable ECC, silent data corruption (NaNs in intermediates), network link flapping' |
| Hangs in communication libraries (bucket 2: PyTorch NCCL watchdog errors, Transformer Engine communication hangs) | NVIDIA DGX Cloud blog | software | no fractions given | Table row: 'PyTorch NCCL watchdog errors and Transformer Engine communication hangs from cascading data-transfer dependencies' |
| Speed regressions (bucket 3: transient slowdowns and persistent stragglers) | NVIDIA DGX Cloud blog | hardware | no fractions given | Table row: 'Transient slowdowns and persistent bottlenecks (stragglers)' |
| UB timeout | NVIDIA DGX Cloud blog (Fig. 1, 6K-GPU Nemotron run) | hardware | types listed, no counts published | Figure 1 failure list row: 'UB timeout; GPU falling off the bus; uncorrectable ECC; ...' |
| GPU falling off the bus | NVIDIA DGX Cloud blog (Fig. 1, 6K-GPU Nemotron run) | hardware | no counts published | Named in the Figure 1 failure list from a 6K-GPU Nemotron run |
| Uncorrectable ECC | NVIDIA DGX Cloud blog (Fig. 1, 6K-GPU Nemotron run) | hardware | no counts published | Named in the Figure 1 failure list from a 6K-GPU Nemotron run |
| Node failure (Slurm-reported) | NVIDIA DGX Cloud blog (Fig. 1, 6K-GPU Nemotron run) | hardware | no counts published | Figure 1 list: 'node failure (Slurm-reported)' |
| Bus error (root-caused to slow filesystem) | NVIDIA DGX Cloud blog (Fig. 1, 6K-GPU Nemotron run) | storage/IO | no counts published | Figure 1 list: 'bus error (root-caused to slow filesystem)' |
| Unhandled CUDA error in NCCL | NVIDIA DGX Cloud blog (Fig. 1, 6K-GPU Nemotron run) | software | no counts published | Named in the Figure 1 failure list from a 6K-GPU Nemotron run |
| Network error (NCCL) | NVIDIA DGX Cloud blog (Fig. 1, 6K-GPU Nemotron run) | network | no counts published | Named in the Figure 1 failure list from a 6K-GPU Nemotron run |
| NCCL system error | NVIDIA DGX Cloud blog (Fig. 1, 6K-GPU Nemotron run) | software | no counts published | Named in the Figure 1 failure list from a 6K-GPU Nemotron run |
| Illegal memory access | NVIDIA DGX Cloud blog (Fig. 1, 6K-GPU Nemotron run) | user/app | no counts published | Named in the Figure 1 failure list from a 6K-GPU Nemotron run |
| NaN in gradients | NVIDIA DGX Cloud blog (Fig. 1, 6K-GPU Nemotron run) | user/app | no counts published | Named in the Figure 1 failure list from a 6K-GPU Nemotron run |
| PCIe downgrading (excluded from taxonomy) | DGX-B200 (Kang et al. 504xB200) | hardware | explicitly excluded, needs separate monitoring | Caveats: 'taxonomy scope is Xid-detectable GPU failures only, explicitly excluding PCIe downgrading, NIC dropout, AOC errors, and CUDA runtime errors' |
| NIC dropout (excluded from taxonomy) | DGX-B200 (Kang et al. 504xB200) | network | explicitly excluded | Caveats: named among categories excluded from the Xid-detectable taxonomy |
| AOC errors (excluded from taxonomy) | DGX-B200 (Kang et al. 504xB200) | network | explicitly excluded | Caveats: named among categories excluded from the Xid-detectable taxonomy |
| CUDA runtime errors (excluded from taxonomy) | DGX-B200 (Kang et al. 504xB200) | software | explicitly excluded | Caveats: named among categories excluded from the Xid-detectable taxonomy |
| CPU out of memory | Philly (Jeon et al. ATC'19) | user/app | 12,076 trials (most frequent); 6.62% of total RTF | Table row: 'Buckets AE+U; one user's repetition factor 185.7' |
| Incorrect inputs | Philly (Jeon et al. ATC'19) | storage/IO | 9,690 trials; 30.43% of total RTF (largest) | Table row: 'model/input files on external HDFS cannot be read - bad path, inconsistent format, or corrupted data' |
| Semantic error | Philly (Jeon et al. ATC'19) | user/app | 2,943 trials; 9.22% of total RTF, 17.06% of RTF×GPU-demand | Table row: 'library version mismatch / dependency setup errors; disproportionately hits large multi-GPU jobs late' |
| Core dump | Philly (Jeon et al. ATC'19) | user/app | 2,912 trials; 3.35% of total RTF | Table row: 'Buckets AE+U' |
| Invalid mem access | Philly (Jeon et al. ATC'19) | user/app | 2,602 trials; 3.82% of total RTF | Table row: 'invalid pointer or race while copying data; seen in both CPU memory and GPU-accessible memory' |
| Model ckpt error | Philly (Jeon et al. ATC'19) | storage/IO | 1,995 trials; 21.73% of total RTF (largest single time-to-failure share) | Table row: 'checkpoint creation fails after epochs complete, usually transient HDFS error or HDFS name-node recovery' |
| CUDA failure | Philly (Jeon et al. ATC'19) | software | 1,484 trials; 0.62% of total RTF | Table row: 'Bucket AE; concentrated in 2-4 GPU jobs (1,153 of 1,484)' |
| Syntax error | Philly (Jeon et al. ATC'19) | user/app | 1,132 trials; 0.19% of total RTF | Table row: 'fails almost immediately at program start; simple syntax checking would prevent many' |
| Traceback from crash | Philly (Jeon et al. ATC'19) | user/app | 777 trials; 2.34% of total RTF | Table row: 'implicit signature used when the root-cause signature is not explicit in logs' |
| MPI error | Philly (Jeon et al. ATC'19) | network | 634 trials; 3.70% of total RTF | Table row: 'Bucket IF' |
| GPU out of memory | Philly (Jeon et al. ATC'19) | software | 487 trials; 1.08% of total RTF | Table row: 'Bucket AE' |
| MPI runtime failure | Philly (Jeon et al. ATC'19) | network | 478 trials; 14.63% of total RTF; longest RTF in table (95%ile 18,090.88 min) | Table row: 'failed network connection to peer MPI process or internal MPI daemon failure' |
| Permission error | Philly (Jeon et al. ATC'19) | user/app | 299 trials; 0.07% of total RTF | Table row: 'Bucket U' |
| Import error | Philly (Jeon et al. ATC'19) | user/app | 148 trials; 0.06% of total RTF | Table row: 'Buckets IF+U' |
| Job preempted | Philly (Jeon et al. ATC'19) | software | 147 trials; 1.66% of total RTF | Table row: 'YARN reclaims in-use GPUs to schedule another job' |
| CUDA init failed | Philly (Jeon et al. ATC'19) | software | 141 trials; 0.03% of total RTF | Table row: 'Bucket AE' |
| Model diverged | Philly (Jeon et al. ATC'19) | user/app | 84 trials; 0.01% of total RTF | Table row: 'Bucket U' |
| CUDA ver. mismatch | Philly (Jeon et al. ATC'19) | software | 49 trials; ~0.00% of total RTF | Table row: 'Bucket AE; 47 of 49 in >4-GPU jobs' |
| GPU ECC error | Philly (Jeon et al. ATC'19) | hardware | 10 trials; 0.03% of total RTF | Table row: 'the only clearly hardware-rooted category in the table - hardware faults are a negligible share' |
| Output node error | Philly (Jeon et al. ATC'19) | user/app | 3 trials | Table row: 'Bucket U' |
| Cannot load libs | Philly (Jeon et al. ATC'19) | software | 1 trial | Table row: 'Bucket AE' |
| No signature | Philly (Jeon et al. ATC'19) | unknown | 1,684 trials (4.2% of total failures) | Table row: 'Log signature matched none of the >230 classifier rules' |
| Killed (job state, user-terminated) | Philly (Jeon et al. ATC'19) | user/app | 12,996 jobs = 13.5%, using 37.69% of GPU time | Headline: 'Killed 12,996 = 13.5% using 37.69%'; caveats: 'Killed jobs are user-terminated and lumped with unsuccessful... though kills are not all failures' |
| Unsuccessful (job state, after fixed-count retries exhausted) | Philly (Jeon et al. ATC'19) | unknown | 16,568 jobs = 17.2%, using 17.76% of GPU time | Headline Table 6 split; system prose: 'jobs auto-retried a fixed number of times before being marked unsuccessful' |
| Network timeouts (retry-worthy error class) | Philly (Jeon et al. ATC'19) | network |  | Recovery notes: 'e.g., stop retrying incorrect inputs but keep retrying network timeouts' |
| Defective nodes overall (fail proactive validation) | SuperBench | hardware | 10.36% of nodes (24k+ A100 GPUs / 3k+ VMs, 90-day build-out) | Table row: 'Defective nodes overall (fail proactive validation) ... 10.36% of nodes filtered as defects' (line 289) |
| IB HCA loopback (InfiniBand NIC defect) | SuperBench | network | 6.04% of nodes defective; repeatability 99.96% | Table row: 'Largest single defect source — InfiniBand host channel adapter loopback bandwidth below spec' (line 290) |
| H2D/D2H memory bandwidth (host-to-device/device-to-host) | SuperBench | hardware | 2.03%; repeatability 99.68% | Table row: 'PCIe/copy-path bandwidth degradation between CPU host memory and GPU' (line 291) |
| BERT models (end-to-end DL benchmark) | SuperBench | hardware | 1.59%; repeatability 99.39% | Table row: 'End-to-end model-training regression catching defects the micro-benchmarks miss' (line 292) |
| CPU latency | SuperBench | hardware | 1.33%; repeatability 99.60% | Table row: 'CPU/memory latency out of expected range' (line 293) |
| IB single-node all-reduce | SuperBench | network | 1.10%; repeatability 99.90% | Table row: 'NCCL all-reduce over IB within a node below expected throughput' (line 294) |
| ResNet models | SuperBench | hardware | 0.73%; repeatability 99.21% | Table row: 'End-to-end model benchmark regression' (line 295) |
| GPT-2 models | SuperBench | hardware | 0.53%; repeatability 99.19% | Table row: 'End-to-end model benchmark regression' (line 296) |
| LSTM models | SuperBench | hardware | 0.46%; repeatability 99.66% | Table row: 'End-to-end model benchmark regression' (line 297) |
| DenseNet models | SuperBench | hardware | 0.40%; repeatability 97.70% | Table row: 'End-to-end model benchmark regression (lowest repeatability in the table)' (line 298) |
| MatMul/all-reduce overlap (computation-communication overlap) | SuperBench | hardware | 0.33%; repeatability 97.88% | Table row: 'Gray failure appearing only when compute and communication run concurrently ... invisible to isolated tests' (line 299) |
| NVLink all-reduce | SuperBench | network | 0.30%; repeatability 99.89% | Table row: 'Intra-node NVLink collective bandwidth degradation' (line 300) |
| GPU GEMM | SuperBench | hardware | 0.23%; repeatability 99.44% | Table row: 'Raw GPU compute (matrix-multiply FLOPS) below spec — notably the SMALLEST defect category' (line 301) |
| Gray failure: GPU memory row remapping | SuperBench | hardware | 3.19% of nodes had 1-10 correctable errors remapped (5.6% regress); 0.18% had >10 remapped (83.3% regress) | Table row: 'Hardware redundancy (spare rows) masks ECC errors but past a threshold causes hidden end-to-end performance regression' (line 302); recovery notes: 'treat >10 remapped  |
| Gray failure: broken redundant IB links | SuperBench | network | not quantified (qualitative) | Table row: 'Partial loss of redundant IB links still routes traffic but congests all-to-all collectives, causing throughput regression' (line 303) |
| Incident duration (fleet incidents, 1-month snapshot) | SuperBench | unknown | 38.1% of incidents >1 day to resolve; 10.3% >2 weeks; 61.9% same day | Table row: 'Customer-impacting incidents on GPU nodes; paper notes >8 distinct node components can cause performance issues' (line 304) |
| Repeat-offender node degradation | SuperBench | hardware | per-node MTBI decays from 719.4 h (1st incident) to 151.7 h (20th) | Table row: 'Nodes that had incidents keep having them faster — repaired/returned nodes are progressively less reliable' (line 305) |
| COMPLETED (SLURM exit state) | SURF-Lisa | user/app | 76% of generic vs 63% of ML submissions | Table row: 'Successful termination; majority of jobs complete, but ML completes notably less often' (line 318) |
| FAILED (SLURM exit state) | SURF-Lisa | user/app | 14% of generic vs 17% of ML submissions | Table row: 'Application-level failure (non-zero exit) ... 85% of failed jobs die within 6 min' (line 319) |
| CANCELLED (SLURM exit state) | SURF-Lisa | user/app | ~4% of generic vs ~13% of ML submissions | Table row: 'User/admin cancellation — the biggest generic-vs-ML difference in the exit-state mix' (line 320) |
| TIMEOUT (SLURM exit state) | SURF-Lisa | user/app | 26-27% of cumulative runtime for both job types | Table row: 'Walltime-limit kills; small in job count but consume the largest failure share of runtime and energy' (line 321) |
| OUT_OF_MEMORY (SLURM exit state) | SURF-Lisa | user/app | small residual share; concurrent-job correlation 0.53 generic vs -0.00 ML | Table row: 'OOM kills; concurrent generic jobs on the same node OOM together (Pearson 0.53)' (line 322) |
| NODE_FAIL (SLURM exit state) | SURF-Lisa | hardware | 2.5% of generic vs 0.2% of ML job runtime; correlation 0.94/0.75 | Table row: 'Node hardware/system failure terminating the job; rare by count but the most strongly correlated state' (line 323) |
| Unsuccessful terminations (all non-COMPLETED states, energy view) | SURF-Lisa | user/app | ~50% of total cluster energy | Table row: 'Failures + timeouts + OOM + cancels + node-fails collectively burn about half the cluster-wide energy' (line 324) |
| GPU thermal limiting | SURF-Lisa | hardware | GPU temperature utilization >90% about 17% of the time; reaches 100% regularly | Table row: 'ML power draw pushes GPU racks past rack air-cooling capacity ... throttling risk, not job-kill per se' (line 325) |
| Correlated same-state termination of concurrent jobs | SURF-Lisa | unknown | diagonal Pearson correlations: NODE_FAIL 0.94/0.75, FAILED 0.74/0.37, TIMEOUT 0.58/0.58, OOM 0.53/-0.00, CANCELLED 0.52/0.74, COMPLETED 0.39/0.61 | Table row (Fig. 10): 'Concurrent jobs on the same node ... tend to end in the same exit state' (line 326) |
| Hardware | LANL | hardware | 30% to >60% of failures depending on system type; largest downtime share; mean repair 342 min | Table row: 'single largest category ... Root-cause info spans 99 distinct hardware subcategories' (line 338) |
| Memory failures (most common low-level hardware cause) | LANL | hardware | >10% of ALL failures in every system; >25% in types F and H | Hardware row detail: 'memory is the single most common low-level cause overall' (line 338) |
| CPU-related failures (type E CPU design flaw) | LANL | hardware | >50% of system E failures | Hardware row detail: 'system E had >50% CPU-related failures due to a design flaw in the type E CPU' (line 338) |
| Software | LANL | software | 5% to 24% of failures depending on system type; mean repair 369 min, C^2=293 | Table row: 'second largest; ... second largest downtime share' (line 339) |
| Parallel file system failures | LANL | software | most common software failure in system F | Software row detail: 'Most common software failure varies by system: parallel file system (system F)' (line 339) |
| Scheduler software failures | LANL | software | most common software failure in system H | Software row detail: 'scheduler software (system H)' (line 339) |
| Operating system failures | LANL | software | most common software failure in system E | Software row detail: 'operating system (system E)' (line 339) |
| Unknown (undetermined root cause) | LANL | unknown | 20-30% of failures in most systems (<5% for type E); <5% of downtime except D and G | Table row: 'Root cause left Unknown when the admin could not identify it ... >90% unknown early in type G' (line 340) |
| Human error | LANL | user/app | small single-digit share; mean repair 163 min (shortest) | Table row: 'Operator/administrator error; notably lower share than Gray's 10-15% or Oppenheimer's 14-30%' (line 341) |
| Network failure | LANL | network | small single-digit share; mean repair 247 min | Table row: 'Much lower than the 20-40% reported for internet services / Windows NT studies' (line 342) |
| Environment | LANL | facility | small single-digit share; mean repair 572 min (~10 h, the longest) | Table row: 'Power outages and A/C failures (only 2 subcategories); long but predictable repairs' (line 343) |
| Power outages | LANL | facility | one of 2 Environment subcategories | Environment row detail: 'Power outages and A/C failures (only 2 subcategories)' (line 343) |
| A/C failures | LANL | facility | one of 2 Environment subcategories | Environment row detail: 'Power outages and A/C failures (only 2 subcategories)' (line 343) |
| All failures (aggregate repair) | LANL | unknown | mean 355 min (~6 h), median 54 min, C^2=187 | Table row: 'Aggregate dominated by hardware+software since those are the most frequent categories' (line 344) |
| Correlated simultaneous multi-node failures | LANL | unknown | >30% of system-wide inter-arrival times were zero early in system 20's life | Recovery notes: 'indicating tightly correlated simultaneous multi-node failures' (line 346) |
| Hardware failures (DSN'14 failure-report taxonomy) | BlueWaters | hardware | 42% (42.1%) of all failures; only 23% of total repair time | Table row: 'Frequent but fast to repair; CPU/DIMM (Opteron, DIMM) dominate hardware causes' (line 357) |
| Software failures (DSN'14) | BlueWaters | software | 20% of all failures; 53% of node repair hours | Table row: 'Lustre file system and resource-management software are the most representative software causes' (line 358) |
| Other categories: network, environment, heartbeat/unknown (DSN'14) | BlueWaters | unknown | remaining ~38% of failures (per-category split not verifiable) | Table row: 'report taxonomy also covers network, environment, and heartbeat-only events (node stopped responding, no root cause)' (line 359) |
| System-wide outages (SWOs) | BlueWaters | storage/IO | 39 SWOs in 261 days (~1 per 160 h); 29/39 (74.4%) involved Lustre; 42% of those from inadequate automated failover | Table row: 'Lustre + failover-procedure inadequacy dominate whole-system downtime' (line 360) |
| Memory errors vs Chipkill/ECC coverage (uncorrectable multi-bit errors) | BlueWaters | hardware | up to 250 errors/h sustained; 99.997% coverage; only 28 uncorrectable multi-bit errors escaped | Table row: 'x8/x4 Chipkill + ECC + parity on CPU memory absorb almost everything; the 28 escapes are the residual crash risk' (line 361) |
| GPU (XK) vs CPU (XE) node failures | BlueWaters | hardware | XK MNBF 63,598 node-h vs XE 128,832 node-h (~2x); platform MTBI XE 8.6 h, XK 25.1 h | Table row: 'GDDR5 has ECC only (no Chipkill) ... weak GPU error detection means errors propagate to apps undetected' (line 362) |
| Application exit status: user | BlueWaters | user/app | 18.75% of 5M runs (vs success 66.47%) | Exit-status breakdown row (DSN'15 LogDiver): 'success 66.47%; user 18.75%; user/system 8.53%; walltime 4.71%; system 1.53%' (line 363) |
| Application exit status: user/system | BlueWaters | user/app | 8.53% of runs | Exit-status breakdown row: ''user/system' = e.g. exceptions during Gemini rerouting' (line 363) |
| Application exit status: walltime | BlueWaters | user/app | 4.71% of runs | Exit-status breakdown row (line 363); caveats: system-induced hangs 'get logged as walltime terminations and are undercounted as system failures' (line 370) |
| Application exit status: system | BlueWaters | user/app | 1.53% of runs but ~9% of production node-hours; XE 1.36% vs XK 1.83% | Exit-status breakdown row: ''system' = hardware/software/config/network at system or node level (MTBI ~15 min across all app interrupts)' (line 363) |
| Failover-correlated application failures | BlueWaters | software | 37% of system-caused app failures within +/-15 min of a failover; 392 failovers, >75% succeeded | Table row: 'Failover (Lustre OSS, Gemini) works but stresses apps' (line 364) |
| Lustre OSS LBUG (I/O stall leading to walltime kill) | BlueWaters | storage/IO |  | Failover row detail: 'example: OSS LBUG -> 3.6 h I/O stall -> app killed at walltime, unable to checkpoint because FS unavailable' (line 364) |
| Subsystem interrupt rates (scratch/project/home Lustre, LNet, Gemini HSN) | BlueWaters | storage/IO | MTBI: scratch FS 35.4 h, project 263.1 h, home 343.2 h; LNet 359.8 h; Gemini HSN 857.7 h | Table row (DSN'15 Table VI): 'Scratch Lustre is the least reliable subsystem by an order of magnitude vs interconnect' (line 365) |
| Event-log view: software vs hardware logged problems (Gainaru et al.) | BlueWaters | software | software 65.7% vs hardware 34.3% of logged problems; 13.5% of failure types hit >1 node | Table row: 'Different counting basis (log events, not repair reports) but same ranking: Lustre tops software, Opteron/DIMM top hardware' (line 366) |
| GPU-stack death undetected by heartbeat | BlueWaters | hardware |  | Recovery notes: 'nodes answer heartbeats while the GPU stack is dead'; caveats: 'heartbeat-based detection misses GPU-stack death' (lines 368, 370) |
| System-induced hangs (MPI deadlock, long failovers) logged as walltime | BlueWaters | software | undercounted as system failures | Caveats: 'system-induced hangs (MPI deadlock, long failovers) get logged as walltime terminations and are undercounted' (line 370) |
| Ambiguous exit code 143/SIGTERM (user kill vs system kill) | BlueWaters | user/app |  | Caveats: '>256 app exit codes are ambiguous (e.g., 143/SIGTERM can be user kill or system kill; LogDiver disambiguates by matching error logs)' (line 370) |
| Single Bit Error (SBE) - corrected by SECDED ECC (no Xid) | Titan | hardware | hundreds/day system-wide; <5% of cards ever saw one; <=2% of app runs hit SBEs | Table row: 'most SBEs land in the L2 cache ... SBE offender nodes run ~3.3 C hotter' (line 378) |
| Double Bit Error (DBE) - detected but not corrected by SECDED ECC (Xid 48) | Titan | hardware | MTBF ~160 h (~1/week); 86% in device memory, 14% in register file | Table row: 'Soft error from cosmic rays/voltage fluctuation ... always crashes the application' (line 379) |
| Off the Bus (OTB) - GPU loses connection to host CPU (no Xid) | Titan | hardware | dominant GPU failure before Dec 2013 (peak ~26/month); nearly negligible after fix | Table row: 'System-integration defect (PCIe/SXM mechanical connector) ... resolved by soldering/rework; re-emerged in 2016' (line 380) |
| ECC dynamic page retirement (Xid 63/64) | Titan | hardware | from Jan 2014; after a DBE: 18 within 10 min, 1 in 10 min-6 h, 17 after >6 h | Table row: 'Triggered by 1 DBE or 2 SBEs in the same page; retires degrading pages via InfoROM' (line 381) |
| GPU board resistor failure (silver sulfide corrosion) -> DBE/OTB storm | Titan | hardware | ~11,000 of 18,688 GPUs (~59%) replaced; peak 813 DBE/OTB events in 2016-Q4; old batch 5,320 vs replacement 127 events | Table row: 'root cause was a resistor on the GPU circuit board (not the GPU chip) corroded by silver sulfide from ambient air' (line 382) |
| Graphics Engine Exception (Xid 13) | Titan | user/app | most frequent Xid (~40-200 events/month); highly bursty | Table row: 'Mostly user application bugs ... but one confirmed case was actually hardware - source attribution is unreliable' (line 383) |
| GPU memory page fault (Xid 31) | Titan | user/app | bursty, up to ~90/month in bursts, mostly 2013 | Table row: 'Illegal address touched by app or driver; user-application-related, bursty like Xid 13' (line 384) |
| GPU stopped processing (Xid 43) | Titan | software | up to ~37/month; not bursty | Table row: driver-related Xids; 'Xid 13 is likely followed by Xid 43' (line 385) |
| Graphics engine fault during context switch (Xid 44) | Titan | software | ~5-17/month | Table row: 'The more frequent driver-related Xids ... Xid 44 ~5-17/mo' (line 385) |
| Preemptive cleanup (Xid 45) | Titan | software |  | Table row: 'a DBE (Xid 48) is likely followed by Xid 45 and Xid 63' (line 385) |
| Internal micro-controller halt (Xid 59) | Titan | software | Xid 59/62 up to ~23/month combined | Table row: 'Internal micro-controller halt (Xid 59, 62) ... Driver/firmware errors' (line 385) |
| Internal micro-controller halt (Xid 62, also thermal) | Titan | software | Xid 59/62 up to ~23/month combined | Table row: 'Driver/firmware errors (Xid 62 also thermal)' (line 385) |
| Invalid or corrupted push buffer stream (Xid 32) | Titan | software | <10 occurrences over ~2-year production period | Table row: 'Rare/never-seen software-firmware Xids ... Xid 32 and 38: <10 occurrences' (line 386) |
| Driver firmware error (Xid 38) | Titan | software | <10 occurrences over ~2-year production period | Table row: 'Xid 32 and 38: <10 occurrences over the entire ~2-year production period' (line 386) |
| Video processor exception (Xid 42) | Titan | software | never observed | Table row: 'Xid 42: never observed' (line 386) |
| Display engine error (Xid 56) | Titan | hardware | hardware-side rarity | Table row: 'Also cataloged hardware-side rarities: display engine error (Xid 56)' (line 386) |
| Error programming video memory interface (Xid 57) | Titan | hardware | hardware-side rarity | Table row: 'error programming video memory interface (Xid 57)' (line 386) |
| Unstable video memory interface (Xid 58) | Titan | hardware | hardware-side rarity | Table row: 'unstable video memory interface (Xid 58)' (line 386) |
| Video processor exception (Xid 65) | Titan | hardware | hardware-side rarity | Table row: 'video processor exception (Xid 65)' (line 386) |
| GPU hardware failure requiring replacement (DBE or OTB event, survival analysis) | Titan | hardware | time-to-failure clustered ~2.8 years; system MTBF fell from >33 h to 2.7 h (2016-Q4); new-partition 96 h vs old 7.9 h (2018-Q4) | Table row: 'NO bathtub curve ... survival ordered cage 0 > 1 > 2; cage-2 hazard ratio ~20x cage 0' (line 387) |
| Normal (exit code 0) | Mira | user/app | 73.79% of all jobs | Line 400 Table IV baseline row: 'Normal termination, exit code 0' |
| Timeout | Mira | user/app | 14.62% of all jobs; 55.8% of abnormally-terminated jobs; 32.86% of core-hours | Line 401: 'Killed for exceeding requested wall time' |
| Bug | Mira | user/app | 7.35% (text: 7.25%) | Line 402: 'Serious termination signals: SIGABRT ... and SIGSEGV' |
| SIGABRT (abort/double-free) | Mira | user/app |  | Line 402, named within Bug row detail as a termination signal |
| SIGSEGV (segfault) | Mira | user/app |  | Line 402, named within Bug row detail as a termination signal |
| Kill (SIGKILL, signal 9) | Mira | user/app | 2.84% | Line 403: 'SIGKILL (signal 9) mid-execution ... mostly user/admin kills' |
| IO | Mira | user/app | 0.94% | Line 404: 'I/O-related user mistakes on files stored on I/O nodes ... misoperations, NOT file-system faults' |
| IO error messages: 'no such file or directory' / 'permission denied' / 'is a directory' | Mira | user/app |  | Line 404, the three named error strings inside the IO row |
| RAS (tasks killed by system's RAS fatal event) | Mira | hardware | 0.17% of all jobs (~0.6% of failed jobs) | Line 405: 'genuine system-reliability failures; best-fit: Weibull' |
| Unknown | Mira | unknown | 0.13% | Line 406: 'Abnormal termination with unknown reason (e.g., missing messages)' |
| SIGILL (signal 4, illegal instruction) | Mira | user/app | 0.065% | Line 407: 'mismatched CPU architecture or permission issue' |
| SIGTRAP (signal 5) | Mira | user/app | 0.062% | Line 408: 'caught exceptions due to possible bugs during debugging' |
| SIGFPE (signal 8) | Mira | user/app | 0.014% | Line 409: 'erroneous arithmetic operation such as division by zero' |
| RAS category: Blue Gene/Q compute card (node errors) | Mira | hardware | 78.16% of system-reliability-based job failures | Line 410, Table XVII row |
| node-error msg ID 00080014 | Mira | hardware | 26.37% | Line 410: 'Dominated by node-error msg IDs 00080014 (26.37%)' |
| node-error msg ID 0008000B | Mira | hardware | 14.04% | Line 410: '... and 0008000B (14.04%)' |
| FIRMWARE (component attribution) | Mira | hardware | 62.1% by component | Line 410: 'by component, FIRMWARE is 62.1%' |
| Machine Controller on Service Node (component attribution) | Mira | hardware | 21.53% by component | Line 410: 'Machine Controller on Service Node 21.53%' |
| RAS category: Software_Error | Mira | software | 16.22% | Line 411: 'Errors in system software, e.g., kernels' |
| Kernel Panic (msg ID 000A000D) | Mira | software | 11.39% | Line 411: 'Kernel Panic 11.39% ... (msg ID 000A000D = 11.39%)' |
| Compute Node Kernel | Mira | software | 4.52% by component | Line 411: 'Compute Node Kernel 4.52% by component' |
| RAS category: Message Unit (MU) | Mira | network | 2.81% | Line 412: 'MU moves data between memory and the 5D torus network — i.e., network-related errors' |
| RAS category: Generic Card/Board | Mira | hardware | 2.65% | Line 413: 'Generic card/board hardware faults' |
| RAS category: Bulk Power Supply | Mira | facility | 0.16% | Line 414: 'Power-supply faults' |
| Memory Unit (component attribution) | Mira | hardware | 0.32% | Line 414: 'components also include Memory Unit 0.32%' |
| Control System on Service Node (component attribution) | Mira | hardware | 0.16% | Line 414: '... and Control System on Service Node 0.16%' |
| completed (F-DATA exit state, ec==0) | F-DATA | user/app | >21M of ~24M jobs (~89.6%) | Line 427: 'Exit code 0; F-DATA's taxonomy is strictly binary' |
| failed / presumably failed (F-DATA exit state, ec in 1-255) | F-DATA | unknown | ~2.5M of ~24M jobs (~10.4%) | Line 428: 'Any non-zero exit code (1-255); no root-cause classes' |
| Completed (M100 Slurm ES label) | F-DATA | user/app | 79% | Line 429: 'Job completed execution without errors' |
| Failed (M100 Slurm ES label) | F-DATA | user/app | 10% | Line 430: 'Job terminated for an unknown reason' — the endogenous failure class targeted |
| Cancelled (M100 Slurm ES label) | F-DATA | user/app | 8% | Line 431: 'Job did not start execution due to an error in submission'; removed before training |
| Timeout (M100 Slurm ES label) | F-DATA | user/app | 2% | Line 432: 'Job terminated due to reaching the time limit' |
| Out of memory (M100 Slurm ES label) | F-DATA | user/app | 0.6% | Line 433: 'Job terminated due to more memory access than allocated' |
| Preempted (M100 Slurm ES label) | F-DATA | software | 0.1% | Line 434: 'A higher-priority job delayed the job execution' (scheduler policy, not a fault) |
| Node fail (M100 Slurm ES label) | F-DATA | hardware | 0.01% | Line 435: 'Job terminated due to a failure in an allocated node'; removed before training |
| EC=1 (M100 relabelled exit-code class) | F-DATA | user/app | 9% of jobs | Line 436: relabelled from raw exit code after discarding Slurm ES labels |
| EC>1 (M100 relabelled exit-code class) | F-DATA | user/app | 2% of jobs | Line 436: 'all non-zero ECs grouped into one failed class' |
| exogenous failures (compute-node problems, networking issues, workload-manager downtime) | F-DATA | unknown | no shares given | Line 437: 'Exogenous = external factors (compute-node problems, networking issues, workload-manager downtime)' |
| endogenous failures (wrongly configured submission scripts, software bugs) | F-DATA | unknown | no shares given | Line 437: 'endogenous = internal reasons ... The prediction work targets only endogenous failures' |
| node anomaly (label=1): any Nagios subsystem in CRITICAL state, node unavailable to run jobs | M100 | unknown | 4,292 of ~12.16M 15-min node-samples = 0.035% | Line 450: 'The papers' ONLY labeled failure class - binary availability proxy' |
| removed from production / drained (nagiosdrained flag) | M100 | facility | 15,795 samples flagged; only 12 coincide with anomaly=1 | Line 451: 'Node manually placed offline by an operator'; rejected as anomaly label |
| system-wide: at least one active anomaly (unavailable node) somewhere in the 980-node system | M100 | unknown | 14.4% of observation period | Line 452: 'Rare per-node events still translate into frequent whole-system degradation' |
| Nagios host states: 0=UP, 1=DOWN, 2=UNREACHABLE (state_type 0=SOFT / 1=HARD) | M100 | unknown | encoding only, no per-state shares published | Line 453: 'From ExaData Nagios plugin doc ... sampled per node and service every 15 min' |
| Nagios service states: 0=OK, 1=WARNING, 2=CRITICAL, 3=UNKNOWN | M100 | unknown | encoding only, no per-state shares published | Line 454: 'CRITICAL on any service is what RUAD/GRAAFE collapse into node anomaly=1' |
| Nagios scheduler/system-software checks: batchs::client, batchs::client::state, batchs::client::serverrespond, batchs::manager::state, ssh::daemon, sys::sssd::events, sys::gpfs::st | M100 | software | no per-service failure counts reported | Line 455: 'Batch (Slurm) client/server health, SSH, SSSD, GPFS daemon, firewall, xCAT sync' |
| Nagios storage/filesystem checks: filesys::local::mount, filesys::local::avail, filesys::shared::mount, filesys::dres::mount, filesys::eurofusion::mount, file::integrity, dev::raid | M100 | storage/IO | no per-service failure counts reported | Line 456: 'Local and shared (GPFS/DRES/EUROfusion) mount availability ... RAID controller status, NFS export readiness' |
| Nagios network checks: alive::ping, net::ib::status, dev::swc::hwcheck, dev::swc::isl, dev::swc::mlxhealth/mlxsensors, dev::swc::cumulushealth/cumulusensors, dev::swc::confcheck | M100 | network | no per-service failure counts reported | Line 457: 'ICMP reachability, InfiniBand HCA readiness, Mellanox/Cumulus switch health + sensors, inter-switch links, switch config drift' |
| Nagios hardware/node checks: bmc::events, sys::rvitals, memory::phys::total, nvidia::configuration, nvidia::memory::retirement, nvidia::memory::replace | M100 | hardware | no per-service failure counts reported | Line 458: 'BMC critical events, BMC sensor thresholds, physical memory availability, V100 GPU configuration and degraded-GPU-memory retirement/replacement states' |
| Nagios cluster/facility summaries: cluster::status::availability, cluster::status::criticality, cluster::status::wattage, crm::status/resources (Pacemaker/Corosync), galera::*, ser | M100 | facility | no per-service failure counts reported | Line 459: 'Whole-platform available/critical node ratios, IT power envelope, HA cluster and DB replica status, certificates, grid/transfer services' |
| [Frontier] Transient errors (performance failures or network socket binding errors) | Frontier-TSUBAME | software | 19 in June 2023 | Line 472: 'Non-persistent test failures caught by the 1000-node backfill screen ... largest category by count' |
| [Frontier] High-bandwidth memory faults requiring repair | Frontier-TSUBAME | hardware | 2 in June 2023 | Line 473: 'HBM faults on MI250X: one failed lammps-nompi, one failed hpl-mpi+amg; both drained immediately' |
| [Frontier] Correctable high-bandwidth memory fault | Frontier-TSUBAME | hardware | 1 in June 2023 | Line 474: 'Failed lammps-nompi once, then recovered correctly ... returned to users' |
| [Frontier] Defective hardware not detected by existing device health checks | Frontier-TSUBAME | hardware | 2 in June 2023 | Line 475: 'One node failed only hpl-mpi; the other failed only rocPRIM+amg — both invisible to automated health checks' |
| [Frontier] drain reason 'checknode(1) Failed Node Screen' | Frontier-TSUBAME | hardware |  | Line 486 recovery notes: 'else drain reason checknode(1) Failed Node Screen until triage' |
| [Frontier] system-level errors, e.g. sbcast failures | Frontier-TSUBAME | software |  | Line 488 caveats: 'system-level errors (e.g., sbcast failures) confound automation' |
| [Tsubame-2] GPU | Frontier-TSUBAME | hardware | 44.37% of 897 failures | Line 476: 'Dominant Tsubame-2 category; GPU failure MTBF 21.94 h; ~70% of GPU-failure events involved 2-3 GPUs' |
| [Tsubame-2] FAN | Frontier-TSUBAME | hardware | ~11.3% | Line 477: 'Second-largest Tsubame-2 category (cooling fans)' |
| [Tsubame-2] Network | Frontier-TSUBAME | network | ~8.7% | Line 478: 'Third-largest Tsubame-2 category' |
| [Tsubame-2] Virtual Machine (VM) | Frontier-TSUBAME | software | ~7.7% | Line 479: 'VM-related failures' |
| [Tsubame-2] Boot | Frontier-TSUBAME | hardware | ~0.3-4% | Line 480 full Table II taxonomy list |
| [Tsubame-2] SSD | Frontier-TSUBAME | hardware | ~4% of failures, ~290 h (~12 days) recovery | Line 480: 'SSD ~4% of failures but ~290 h (~12 days) recovery' |
| [Tsubame-2] PSU | Frontier-TSUBAME | hardware | ~0.3-4% | Line 480 full Table II taxonomy list |
| [Tsubame-2] OtherHW | Frontier-TSUBAME | hardware | ~0.3-4% | Line 480 full Table II taxonomy list |
| [Tsubame-2] System Board | Frontier-TSUBAME | hardware | ~0.3-4% | Line 480 full Table II taxonomy list |
| [Tsubame-2] (InfiniBand) IB | Frontier-TSUBAME | network | ~2% | Line 478: 'separate smaller (InfiniBand) IB category ~2%' |
| [Tsubame-2] Disk | Frontier-TSUBAME | hardware | ~0.3-4% | Line 480 full Table II taxonomy list |
| [Tsubame-2] CPU | Frontier-TSUBAME | hardware | 1.78% | Line 480: 'GPU failures 25x more frequent than CPU'; CPU = 1.78% stated in text |
| [Tsubame-2] Down | Frontier-TSUBAME | hardware | ~0.3-4% | Line 480 full Table II taxonomy list |
| [Tsubame-2] PBS | Frontier-TSUBAME | software | ~0.3-4% | Line 480 full Table II taxonomy list |
| [Tsubame-2] Memory | Frontier-TSUBAME | hardware | ~0.3-4% | Line 480 full Table II taxonomy list |
| [Tsubame-2] Rack | Frontier-TSUBAME | hardware | ~0.3-4% | Line 480 full Table II taxonomy list |
| [Tsubame-2] OtherSW | Frontier-TSUBAME | software | ~0.3-4% | Line 480 full Table II taxonomy list |
| [Tsubame-3] software | Frontier-TSUBAME | software | 50.59% of 338 failures | Line 481: 'Dominant Tsubame-3 category, attributed partly to new AI/ML workloads' |
| [Tsubame-3] GPU Driver-related problems (software root locus) | Frontier-TSUBAME | software | 42.7% of 171 software root loci | Line 481: 'of 171 software root loci: GPU Driver-related problems 42.7%' |
| [Tsubame-3] unknown (software root locus) | Frontier-TSUBAME | software | 19.3% of software root loci | Line 481; caveat line 488: '~20% of Tsubame-3 software failures have unknown, non-reproducible cause' |
| [Tsubame-3] hang by kernel panic | Frontier-TSUBAME | software | 14.0% of software root loci | Line 481: 'hang by kernel panic 14.0%' |
| [Tsubame-3] XFS software bug | Frontier-TSUBAME | software | 8.2% of software root loci | Line 481: 'XFS software bug 8.2%' |
| [Tsubame-3] Lustre client problems | Frontier-TSUBAME | software | 2.9% of software root loci | Line 481: 'Lustre client problems 2.9%' |
| [Tsubame-3] ext4 bug | Frontier-TSUBAME | software | 2.3% of software root loci | Line 481: 'ext4 bug 2.3%' |
| [Tsubame-3] SGE OOM | Frontier-TSUBAME | software | 1.8% of software root loci | Line 481: 'SGE OOM 1.8%' |
| [Tsubame-3] kernel bug / kernel panic / OOM / memory swap / node hang / hfi errors | Frontier-TSUBAME | software | ~0.6-1.2% each of software root loci | Line 481: 'plus kernel bug/panic/OOM/memory swap/node hang/hfi errors at ~0.6-1.2% each' |
| [Tsubame-3] GPU | Frontier-TSUBAME | hardware | 27.81% | Line 482: 'Second-largest Tsubame-3 category; GPU MTBF improved to 226.48 h' |
| [Tsubame-3] GPU 'fallen off the bus' (multi-GPU failure mode) | Frontier-TSUBAME | hardware |  | Line 482: 'dominant multi-GPU modes were fallen off the bus, temperature-related failures, and simultaneous correlated reboots' |
| [Tsubame-3] temperature-related GPU failures (multi-GPU failure mode) | Frontier-TSUBAME | hardware |  | Line 482, listed among dominant multi-GPU modes |
| [Tsubame-3] simultaneous correlated GPU reboots (multi-GPU failure mode) | Frontier-TSUBAME | hardware |  | Line 482, listed among dominant multi-GPU modes |
| [Tsubame-3] Memory | Frontier-TSUBAME | hardware | ~0.3-3.6% | Line 483 full Table II taxonomy list |
| [Tsubame-3] CPU | Frontier-TSUBAME | hardware | 3.25%; CPU MTBF 1593.6 h | Line 483: 'CPU MTBF 1593.6 h vs 537.6 h on Tsubame-2' |
| [Tsubame-3] Disk | Frontier-TSUBAME | hardware | ~0.3-3.6% | Line 483 full Table II taxonomy list |
| [Tsubame-3] Omni-Path | Frontier-TSUBAME | hardware | ~0.3-3.6% | Line 483 full Table II taxonomy list |
| [Tsubame-3] SXM2-Board | Frontier-TSUBAME | hardware | ~0.3-3.6% | Line 483 full Table II taxonomy list |
| [Tsubame-3] IP Motherboard | Frontier-TSUBAME | hardware | ~0.3-3.6% | Line 483 full Table II taxonomy list |
| [Tsubame-3] Unknown | Frontier-TSUBAME | unknown | ~0.3-3.6% | Line 483 full Table II taxonomy list |
| [Tsubame-3] GPUDriver | Frontier-TSUBAME | software | ~0.3-3.6% | Line 483 full Table II taxonomy list |
| [Tsubame-3] Power-Board | Frontier-TSUBAME | hardware | ~1% of failures, up to 230 h (~10 days) recovery | Line 483: 'Power-Board ~1% of failures but up to 230 h (~10 days) recovery' |
| [Tsubame-3] Lustre | Frontier-TSUBAME | software | ~0.3-3.6% | Line 483 full Table II taxonomy list |
| [Tsubame-3] CRC | Frontier-TSUBAME | hardware | ~0.3-3.6% | Line 483 full Table II taxonomy list |
| [Tsubame-3] SXM2_Cable | Frontier-TSUBAME | hardware | ~0.3-3.6% | Line 483 full Table II taxonomy list |
| [Tsubame-3] LED Front Panel | Frontier-TSUBAME | hardware | ~0.3-3.6% | Line 483 full Table II taxonomy list ('Led Front Panel') |
| [Tsubame-3] Ribbon Cable | Frontier-TSUBAME | hardware | ~0.3-3.6% | Line 483 full Table II taxonomy list |
| [Lassen] no failure taxonomy reported (non-'complete' exit-status jobs excluded, not classified) | Frontier-TSUBAME | unknown | ~90.6% complete (1,467,555 of ~1.62M jobs); ~10% non-complete unclassified | Line 484: 'it never breaks down why the remaining ~10% of jobs did not complete' |
| Hardware (H) — all systems, Table 3 | Oliner-5logs | hardware | raw 174,586,516 (98.04%) -> filtered 1,999 (18.78%) | Line 497: 'dominance in raw counts is a redundant-reporting artifact (disk/parity storms)' |
| Software (S) — all systems, Table 3 | Oliner-5logs | software | raw 144,899 (0.08%) -> filtered 6,814 (64.01%) | Line 498: 'After de-duplication filtering, software is the most common estimated failure type' |
| Indeterminate (I) — all systems, Table 3 | Oliner-5logs | unknown | raw 3,350,044 (1.88%) -> filtered 1,832 (17.21%) | Line 499: 'Alerts that can originate from both hardware and software, or have unknown cause' |
| BG/L: KERNDTLB (H) | Oliner-5logs | hardware | raw 152,734 -> filtered 37 | Line 500: 'data TLB error interrupt' kernel messages |
| BG/L: KERNSTOR (H) | Oliner-5logs | hardware | raw 63,491 -> filtered 8 | Line 501: 'data storage interrupt' |
| BG/L: APPSEV (S) | Oliner-5logs | software | raw 49,651 -> filtered 138 | Line 502: 'ciod error reading message prefix after LOGIN_MESSAGE on CioStream' |
| BG/L: KERNMNTF (S) | Oliner-5logs | software | raw 31,531 -> filtered 105 | Line 503: 'Lustre mount FAILED' on I/O nodes |
| BG/L: KERNTERM (S) | Oliner-5logs | software | raw 23,338 -> filtered 99 | Line 504: 'rts: kernel terminated for reason 1004 / bad message header' |
| BG/L: KERNRTSP (S) | Oliner-5logs | software | raw 3,983 -> filtered 260 | Line 505: 'rts panic! - stopping execution' — largest BG/L category after filtering |
| BG/L: KERNREC | Oliner-5logs | software | raw 6,145 -> filtered 9 | Line 506, named in remaining-categories row |
| BG/L: APPREAD | Oliner-5logs | software | raw 5,983 -> filtered 11 | Line 506, named in remaining-categories row (ciod control-stream read failures) |
| BG/L: APPRES | Oliner-5logs | software | raw 2,370 -> filtered 13 | Line 506, named in remaining-categories row |
| BG/L: APPUNAV | Oliner-5logs | software | raw 2,048 -> filtered 3 | Line 506, named in remaining-categories row |
| BG/L: '31 Others' (tree-network packet errors, ciod control-stream read failures, node-map creation errors, machine check interrupts, etc.) | Oliner-5logs | software | raw 7,186 -> filtered 519 | Line 506: 'paper lists only the top 10 of BG/L's 41 observed categories' |
| Thunderbird: VAPI (I) | Oliner-5logs | network | raw 3,229,194 -> filtered 276 (99.4% of raw Tbird alerts) | Line 507: InfiniBand 'KERNEL_IB ... Fatal error (Local Catastrophic Error)'; one node produced 643,925 |
| Thunderbird: EXT_FS (H) | Oliner-5logs | storage/IO | raw 4,022 -> filtered 778 | Line 508: 'EXT3-fs error ... Detected aborted journal' — largest Tbird category after filtering |
| Thunderbird: CPU (S) | Oliner-5logs | software | raw 2,741 -> filtered 367 | Line 509: 'Losing some ticks... checking if CPU frequency changed' — Linux SMP kernel clock bug under heavy network load |
| Thunderbird: SCSI (H) | Oliner-5logs | storage/IO | raw 2,186 -> filtered 317 | Line 510: 'scsi0: rejecting I/O to offline device' |
| Thunderbird: ECC (H) | Oliner-5logs | hardware | raw 146 -> filtered 143 | Line 511: 'Critical memory-device events; interarrival ~exponential/lognormal — the one failure class that behaved as an independent physical process' |
| Thunderbird: MPT (I) | Oliner-5logs | storage/IO | raw 4,583 -> filtered 157 | Line 512: 'mptscsih: ioc0: attempting task abort!' |
| Thunderbird: PBS_CON (S) | Oliner-5logs | software | raw 5,318 -> filtered 16 | Line 513: 'PBS batch-system connection refused' |
| Thunderbird: PBS_BFD (S) | Oliner-5logs | software | raw 28 -> filtered 28 | Line 513: PBS 'bad file descriptor' |
| Thunderbird: CHK_DSK (S) | Oliner-5logs | software | raw 13 -> filtered 2 | Line 513: 'check-disks fault asserts' |
| Thunderbird: NMI (S) | Oliner-5logs | software | raw 8 -> filtered 4 | Line 513: NMI 'Dazed and confused' |
| Red Storm: BUS_PAR (H) | Oliner-5logs | storage/IO | raw 1,550,217 -> filtered 5 (93% of raw Red Storm alerts; 98.69% of CRIT alerts) | Line 514: DDN 'Verify Host 2 bus parity error' |
| Red Storm: HBEAT (I) | Oliner-5logs | hardware | raw 94,784 -> filtered 266 | Line 515: 'ec_heartbeat_stop ... node heartbeat fault' from the RAS network |
| Red Storm: PTL_EXP (I) | Oliner-5logs | network | raw 11,047 -> filtered 421 | Line 516: 'LustreError: @@@ timeout (sent at [time], 300s ago)' Portals/Lustre timeouts — largest Red Storm category after filtering |
| Red Storm: CMD_ABORT (H) | Oliner-5logs | storage/IO | raw 1,686 -> filtered 497 | Line 517: DMT_310 'Command Aborted: SCSI cmd' on DDN controllers |
| Red Storm: DSK_FAIL (H) | Oliner-5logs | storage/IO | raw 54 -> filtered 54 | Line 518: DMT_DINT 'Failing Disk' — 1:1 raw:filtered; DDN has 'a great variety of alert patterns that all mean disk failure' |
| Red Storm: ADDR_ERR | Oliner-5logs | unknown | raw 6,763 -> filtered 1 | Line 519: DDN address errors |
| Red Storm: PTL_ERR | Oliner-5logs | unknown | raw 631 -> filtered 54 | Line 519: Lustre errors |
| Red Storm: TOAST | Oliner-5logs | unknown | raw 186 -> filtered 9 | Line 519: 'PANIC_SP WE ARE TOASTED!' |
| Red Storm: EW (expired watchdog) | Oliner-5logs | unknown | raw 163 -> filtered 58 | Line 519: 'expired/triggered watchdogs' |
| Red Storm: WT (triggered watchdog) | Oliner-5logs | unknown | raw 107 -> filtered 45 | Line 519: 'expired/triggered watchdogs' |
| Red Storm: RBB (request buffers busy) | Oliner-5logs | unknown | raw 105 -> filtered 19 | Line 519: 'request-buffers-busy' |
| Red Storm: OST (failed OST transaction commit) | Oliner-5logs | unknown | raw 1 -> filtered 1 | Line 519: 'failed OST transaction commit' |
| Spirit: EXT_CCISS (H) | Oliner-5logs | storage/IO | raw 103,818,910 -> filtered 29 | Line 520: 'cciss: cmd ... has CHECK CONDITION' disk-controller storms; node sn373 logged 89,632,571 messages |
| Spirit: EXT_FS (H) | Oliner-5logs | storage/IO | raw 68,986,084 -> filtered 14 | Line 521: 'EXT3-fs error ... IO failure' |
| Spirit: PBS_CHK (S) | Oliner-5logs | software | raw 8,388 -> filtered 4,119 | Line 522: 'pbs_mom: task_check, cannot tm_reply' — job-fatal PBS bug; largest single filtered category in the whole study |
| Spirit: GM_LANAI (S) | Oliner-5logs | software | raw 1,256 -> filtered 117 | Line 523: Myrinet GM 'LANai is not running' |
| Spirit: PBS_CON (S) | Oliner-5logs | software | raw 817 -> filtered 25 | Line 523: PBS connection errors |
| Spirit: GM_MAP (S) | Oliner-5logs | software | raw 596 -> filtered 180 | Line 523: 'gm_mapper assertion failures' |
| Spirit: PBS_BFD (S) | Oliner-5logs | software | raw 346 -> filtered 296 | Line 523: PBS file-descriptor errors |
| Spirit: GM_PAR (S) | Oliner-5logs | software | raw 166 -> filtered 95 | Line 523: 'NIC SRAM parity errors' |
| Liberty: PBS_CHK (S) | Oliner-5logs | software | raw 2,231 -> filtered 920; estimated to have killed up to 1,336 jobs | Line 524: 'Same PBS task_check bug: MPI rank-0 mom died, message repeated up to 74x per job' |
| Liberty: PBS_BFD (S) | Oliner-5logs | software | raw 115 -> filtered 94 | Line 525 tail row |
| Liberty: PBS_CON (S) | Oliner-5logs | software | raw 47 -> filtered 5 | Line 525 tail row |
| Liberty: GM_PAR (S) | Oliner-5logs | software | raw 44 -> filtered 19 | Line 525: 'Myrinet GM firmware parity panics'; GM_PAR and GM_LANAI correlated but neither reliably precedes the other |
| Liberty: GM_LANAI (S) | Oliner-5logs | software | raw 13 -> filtered 10 | Line 525: 'LANai-not-running' |
| Liberty: GM_MAP (S) | Oliner-5logs | software | raw 2 -> filtered 2 | Line 525: 'mapper assertions' |
| silent failures (believed rare) | Oliner-5logs | unknown | believed rare | Line 527 recovery notes: 'most failures leave a log signature, silent failures believed rare' |
| Failed jobs (binary SGE accounting label) | Tachyon (Park et al. 2024) | user/app | 8.6% of 89,393 jobs (~7,7xx jobs); successful 91.4% | Table row: 'Failed jobs (binary SGE accounting label)... jobs are labeled success vs failure from the SGE accounting file'; no exit-status taxonomy published |
| Runtime skew of failed jobs (Observation 2) | Tachyon (Park et al. 2024) | user/app | failed jobs = 8.6% of jobs but 37.5% of cumulative runtime; avg CPU time 344,925 s vs 51,631 s (~6.7x) | Table row: 'Failures are disproportionately expensive: long-running/large jobs fail more' |
| Failed jobs use more CPU cores (Observation 1) | Tachyon (Park et al. 2024) | user/app | qualitative (distribution comparison) | Table row: 'Failed jobs request/use more cores than successful ones - scale correlates with failure' |
| Inter-failure interval: heavy-tailed Weibull, decreasing hazard (Observations 3-5) | Tachyon (Park et al. 2024) | unknown | mean interval 1,007 s; 80% below mean; ~52% of inter-arrivals <10 s; Weibull shape <1; CV 2.76 | Table row: 'Failures arrive in bursts (temporal clustering) with decreasing failure rate... contradicts the Poisson/exponential failure model' |
| Attribution: job/user resource usage, not compute node (Observation 6 + IV analysis) | Tachyon (Park et al. 2024) | user/app | only 2.7% of users (10/361-366) and 6.5% of groups (12/183) show a clear success-or-failure tendency | Table row: decisive predictors are per-job resource-usage counters (ru_utime, ru_stime, ru_nvcsw, ru_minflt, ru_nivcsw, ru_majflt, cpu, io, owner, group, qname, granted_pe), not th |
| Meta - Device Errors (defect category 3.1) | SDC-trio (Dixit/Meta 2021) | hardware | no fraction given (one of 4 defect categories; all lead to SDC) | Table row: 'Manufacturing/design corner-case defects: blocks stuck under particular power states, signal-arrival uncertainty causing erroneous bit-flips (timing path errors), uneve |
| Meta - Early Life Failures (3.2) | SDC-trio (Dixit/Meta 2021) | hardware | no fraction given | Table row: 'pass manufacturing test patterns but exhibit failure symptoms only after weeks/months of field workloads' |
| Meta - Degradation (3.3) | SDC-trio (Dixit/Meta 2021) | hardware | no fraction given; 'uncommon in comparison to early life failures' | Table row: 'Wear with usage; frequently-used computational blocks degrade faster (analogy: Rowhammer on DDR4)' |
| Meta - End-of-Life Wear-out (3.4) | SDC-trio (Dixit/Meta 2021) | hardware | no fraction given | Table row: bathtub-curve tail; case study: defective Core 59 computed Int(1.1^53)=0 in Scala math.pow causing missing rows/data loss |
| Google - CEE symptom class 1: wrong answers detected nearly immediately | SDC-trio (Hochschild/Google 2021) | hardware | no fractions; classes listed 'in increasing order of risk' | Table row: 'Caught by self-checking, exceptions, or segmentation faults, allowing automated retries' |
| Google - CEE symptom class 2: machine checks | SDC-trio (Hochschild/Google 2021) | hardware | no fraction; 'more disruptive' | Table row: 'Hardware-detected machine-check errors' |
| Google - CEE symptom class 3: wrong answers detected too late to retry | SDC-trio (Hochschild/Google 2021) | hardware | no fraction | Table row: 'Detected only after the computation can no longer be retried; corruption may already have propagated' |
| Google - CEE symptom class 4: wrong answers never detected | SDC-trio (Hochschild/Google 2021) | hardware | no fraction; highest risk | Table row: observed examples include lock-semantics violations; load/store/vector/coherence data corruption; self-inverting AES mis-computation; GC corruption losing live storage d |
| Google - mercurial-core characterization | SDC-trio (Hochschild/Google 2021) | hardware | a few mercurial cores per several thousand machines; ~half of suspect cores proven mercurial | Table row: 'Failures mostly non-deterministic at variable rate; faulty cores fail repeatedly and intermittently and often get worse with time' |
| Alibaba - Computation-type SDCs | SDC-trio (Wang/Alibaba SOSP'23) | hardware | 19 of 27 extensively-tested faulty processors | Table row: 'Defective arithmetic operations: arithmetic logic computation, vector operations, floating-point calculation'; faulty features VecUnit ~0.44, FPU ~0.33, Cache ~0.18, Tr |
| Alibaba - Consistency-type SDCs | SDC-trio (Wang/Alibaba SOSP'23) | hardware | 8 of 27 extensively-tested faulty processors | Table row: 'Defective consistency-guarantee features: cache coherency and transactional memory; only detectable with multi-threaded tests' |
| Alibaba - failure rate by test timing (Table 1) | SDC-trio (Wang/Alibaba SOSP'23) | hardware | Factory 0.776/10k; Datacenter delivery 0.18/10k; Re-install 2.306/10k; Regular production tests 0.348/10k; Total 3.61/10k | Table row: 'Pre-production testing (3.262/10k) catches 90.36% of faulty processors; the rest escape into production' |
| Alibaba - defect scope within processor (Obs. 4) | SDC-trio (Wang/Alibaba SOSP'23) | hardware | ~half of faulty processors: exactly one defective physical core; other half: all physical cores affected | Table row: 'Single-core defects sit in per-core components... all-core defects sit in shared components (e.g., CPU cache)' |
| Alibaba - bitflip characterization (Obs. 6-8) | SDC-trio (Wang/Alibaba SOSP'23) | hardware | 51.08% of bitflips are 0-to-1; 99.9% of float64 precision losses <0.02%; 40.2% of int32 losses >100%; mostly 1 flipped bit but 2+ bits occur | Table row: 'All tested datatypes affected (int, float, byte, binary); bitflips manifest at fixed positions; breaks IID and single-bit assumptions' |
| Alibaba - reproducibility classes: 'apparent' vs 'tricky' SDCs (Obs. 9-10) | SDC-trio (Wang/Alibaba SOSP'23) | hardware | frequency spans 0.01 to hundreds of errors/minute; 51.2% of settings >1/min ('apparent'); remainder 'tricky' | Table row: ''Tricky' SDCs trigger only above a temperature threshold (e.g., MIX1 testcase C only above 59C) with frequency growing exponentially with temperature' |
| Multi-bit SDC flips defeating standard ECC (recovery-notes prose) | SDC-trio (Wang/Alibaba SOSP'23) | hardware |  | Recovery notes: 'standard ECC only corrects single-bit flips but multi-bit SDCs occur; ML-prediction ranges defeated by tiny FP precision losses; parity computed after a wrong resu |
| Slurm terminal-state taxonomy: COMPLETED / CANCELLED / FAILED / TIMEOUT / NODE_FAIL | Helios (Hu et al. SC'21) | user/app | TIMEOUT and NODE_FAIL 'very rare', folded into FAILED; stats collapse to 3 bins | Table row: 'Taxonomy = Slurm terminal-state labels, NOT root causes. Five states as named: COMPLETED, CANCELLED, FAILED, TIMEOUT, NODE_FAIL' |
| FAILED (GPU jobs, Fig. 7a) | Helios (Hu et al. SC'21) | user/app | 15.5% of GPU jobs (part of 37.6% unsuccessful) | Table row: 'Completed 62.4%, Canceled 22.1%, Failed 15.5%'; FAILED defined as 'terminated due to internal or external errors' |
| CANCELLED (GPU jobs, Fig. 7a) | Helios (Hu et al. SC'21) | user/app | 22.1% of GPU jobs | Table row: CANCELLED = terminated by the user; much cancellation is 'feedback-driven exploration' (early-stops of converged or poor runs) |
| CPU jobs Failed/Canceled (Fig. 7a) | Helios (Hu et al. SC'21) | user/app | Failed 6.1%, Canceled 3.0%, Completed 90.9% | Table row: 'CPU jobs (preprocessing, decompression, etc.) fail far less than GPU jobs' |
| GPU time wasted by final status (Fig. 1b) | Helios (Hu et al. SC'21) | user/app | Helios GPU time: Completed 51.3%, Canceled 39.4%, Failed 9.3% (Philly: 31.3%/32.6%/36.1%) | Table row: 'Nearly half of all Helios GPU time goes to jobs that do not end COMPLETED' |
| Failure/completion vs job scale (Fig. 7b) | Helios (Hu et al. SC'21) | user/app | jobs with >=64 GPUs: fewer than a quarter complete, ~70% canceled | Table row: 'Completion ratio decreases monotonically with GPU count (exception: 2-GPU jobs)' |
| User errors: script configuration, syntax/semantic errors (cause attribution) | Helios (Hu et al. SC'21) | user/app | no quantified breakdown; 'majority of failures' | Table row: 'The majority of failures are incurred by user errors, such as script configuration, syntax/semantic errors in the program' |
| Other causes named without numbers: timeout, node failure, incorrect inputs, runtime failure | Helios (Hu et al. SC'21) | user/app | unquantified | Table row: 'Other causes listed without numbers: timeout, node failure, incorrect inputs, runtime failure, etc.'; root-cause analysis explicitly deferred to Microsoft Philly refs |
| User-level failure behavior (Fig. 9b) | Helios (Hu et al. SC'21) | user/app | users' GPU-job completion rates 'generally low' across the population | Table row: failure 'reflects the users' overall behaviors instead of some individual ones' - endemic to DL workflow |
| NODE_FAIL (hardware/node failures) | Helios (Hu et al. SC'21) | hardware | 'Very rare' - no count published; merged into FAILED | Table row: 'NODE_FAIL exists as a label but is never quantified separately'; defined as node crash |
| TIMEOUT (exceeded execution time limit) | Helios (Hu et al. SC'21) | user/app | 'very rare', regarded as failed in the study | Row 1 detail: 'TIMEOUT = exceeded execution time limit'; 'timeout and node fail are very rare, and will be regarded as failed in this study' |
| SUSPENDED (one stray record) | Helios (Hu et al. SC'21) | user/app | 1 record in Uranus, ignored | Row 1 detail: 'One stray SUSPENDED record in Uranus was ignored' |
| Trace outcome labels: FINISH / EVICT / KILL / FAIL / LOST | Borg traces (Chen ISSRE'14; Tirmazi EuroSys'20) | user/app | these 4 termination events + LOST are all the trace exposes; no cause field | Table row: Tirmazi Sec 5.2 definitions; 'Google states only EVICT is infrastructure-caused' |
| KILL (user/dependency cancellation) | Borg traces | user/app | 2011: 40.7% of job terminations; 2019 cell g: 85% of ended jobs; 13.62% of 2019 collection events | Table row: 'canceled by user via RPC or automatically as child of a terminated parent job'; 87% of jobs WITH a parent experience a KILL vs 41% without |
| FAIL (task/job's own software error: segfault, exceeding requested resources, memory leak, misconfiguration, exceptions) | Borg traces | user/app | 2011: 1.7% of job terminations (avg 14.6 job failures/hr, >10,000/month); 2019: ~1% of ended jobs, 0.89% of collection events | Table row: 'unexpected termination from the task's own problem (segfault, exceeding requested resources, memory leak, misconfiguration)'; failed jobs consume 2.5x CPU and 6.6x memo |
| EVICT (infrastructure-caused: preemption, overcommit OOM kill, hardware failure, forced OS upgrade) | Borg traces | software | 2019: 3.2% of 24.8M collections see >=1 instance eviction; 96.6% of those non-production; production tier <0.2% | Table row: 'de-scheduled by infrastructure (rare hardware failure, forced OS upgrade ~1/month/machine, preemption by higher-priority instance, or OOM kill when machine overcommitte |
| LOST (missing termination record) | Borg traces | unknown | 'Very rare'; ~0.0% of 2019 collection events; <0.05% of 2011 records | Table row: 'Purely a data-quality label, not a failure mode'; ~0.013% of task events have non-empty missing-info field |
| Node/machine failure (machine REMOVE events - conflated with maintenance) | Borg traces | hardware | cluster availability 99.82%; 59.1% of 12.5k machines never removed in 29 days; >99% have <6 add/remove cycles | Table row: 'trace cannot distinguish node failure from planned maintenance'; failed-task ratio vs machine cycles correlation -0.52 (rejuvenated machines fail less) |
| Unsuccessful jobs overall (failed + killed/aborted), cross-trace comparison | Borg traces (Amvrosiadis et al. Obs. 8) | user/app | Google 2011: ~40-43% of jobs unsuccessful, consuming ~33% of CPU time - 1.4-6.8x LANL Mustang (~10%), Trinity (~26%), HedgeFund (~29%) | Table row: 'Almost all unsuccessful Google jobs are aborted/killed rather than FAIL'; Tirmazi pushes back that kills are user/dependency-triggered |
| Failed (job-level final status) | Alibaba PAI v2020 (Weng NSDI'22 + trace CSVs) | unknown | 256,555 of 1,055,501 jobs = 24.3% of all jobs; 25.9% of finished jobs (Terminated 69.4%, Running 6.0%, Waiting 0.3%) | Table row: 'pure outcome label with NO cause attribution'; schema documents exactly four statuses Running/Terminated/Failed/Waiting |
| Failed (task-level final status) | Alibaba PAI v2020 | unknown | 256,762 of 1,261,050 tasks = 20.4%; instance-weighted 14.7%; GPU-requesting tasks fail 24.4% vs 1.8% CPU-only | Table row: 'tasks requesting GPUs fail at 24.4%... vs only 1.8% for CPU-only tasks - an order-of-magnitude gap' |
| Short-job failure pattern (early-abort signature) | Alibaba PAI v2020 | user/app | median Failed duration 220 s vs 663 s Terminated; 26.8% of Failed <1 min, 67.4% <10 min, 80.8% <30 min; U-shaped: 6.0% of <1 min jobs failed, 1.5% for 1-24 h, 12.0% for >24 h | Table row: 'the classic early-abort signature (import errors, config/OOM at startup) also seen in Microsoft Philly'; computed on the 10% of Failed jobs with timestamps |
| Recurring-job failures (repeatedly-failing pipelines) | Alibaba PAI v2020 | user/app | 52.6% of Failed jobs from groups submitted 50+ times; 75.1% from groups 5+; 58,016 groups (74,668 jobs) failed on EVERY finished run | Table row: 'the bulk of failures are the same job failing over and over (repeatedly-failing production/batch pipelines)' |
| Waiting (never scheduled) | Alibaba PAI v2020 | user/app | 0.35% of jobs / 0.29% of tasks; instance-weighted 1.2% | Table row: 'Jobs stuck queued at trace end'; ~9% of short instances spend >50% of completion time queued; P90 queueing delay 497 s for high-GPU tasks |
| Indistinguishable candidate causes named in caveats: user code error, OOM, preemption/eviction, hardware fault | Alibaba PAI v2020 | unknown | not recorded in trace | Caveat 1: 'no distinction between user code error, OOM, preemption/eviction, or hardware fault'; caveat 5: early user cancellations may also land in Terminated |
| Success (exit status 0) | FRESCO/DSN2020 | user/app | System A 86.1% of jobs (48.4% node-seconds); System B 84.4% (44.4%); non-shared multi-node only 61.8%/64.0% | Table row 'Success (exit status 0)'; five-category exit-code taxonomy (Success, Walltime, User, System, User/System) |
| Walltime (hit wallclock limit) | FRESCO/DSN2020 | user/app | A: 4.0% of jobs / 33.4% node-seconds; B: 8.0% / 43.4% | Table row 'Walltime (hit wallclock limit)'; excluded from failure-rate analysis since checkpointed work may not be lost |
| User failures (misconfigured job script/compile/env, ctrl-C, command errors, missing module/file/directory, wrong permissions) | FRESCO/DSN2020 | user/app | A: 3.3% of jobs = 33% of failures; B: 3.6% = 48% of failures | Table row 'User failures' — most common failure category on System B |
| System failures (hardware or system-software errors terminate the application) | FRESCO/DSN2020 | software | A: 5.3% of jobs = 53% of A's failed jobs; B: 0.3% = 4% | Table row 'System failures'; 13X gap attributed to B's chipkill ECC + dedicated ops staff |
| User/System (indeterminate) failures | FRESCO/DSN2020 | unknown | A: 1.3% of jobs; B: ~1.1% | Table row 'User/System (indeterminate) failures' — e.g. SIGTERM can come from user or scheduler |
| Overall job failure rate (all non-success excl. walltime) | FRESCO/DSN2020 | unknown | A: ~9.9% of jobs (13.9% incl. walltime); B: ~7.6% (15.6%) | Table row 'Overall job failure rate' |
| Exit code 107 'transport endpoint is not connected' (remote NFS/parallel-filesystem unreachable) | FRESCO/DSN2020 | software / storage | 33% of ALL system-related job failures on System A | System-failures row detail: '33% of ALL system-related job failures across the study are exit code 107'; headline: '33% of A's system failures traced to one exit code (107, NFS unr |
| Exit code 137 out-of-memory (OOM kill) | FRESCO/DSN2020 | user/app | Pearson r=0.83/0.84 (A) and 0.57 (B) with tail memory usage | 'Exit code 137 = out-of-memory (OOM kill), the other named system-failure signature'; Memory/OOM correlation (exit 137) table row; OOM occurs even with >10GB free (wrong memory bou |
| Burst-failure root cause: remote file system failure | FRESCO/DSN2020 | storage/IO | 2 of 26 exit-107 burst-failure clusters | DBSCAN clustering of exit-107 jobs found 26 burst clusters; 'root causes: remote file system failure (2 clusters)' |
| Burst-failure root cause: network failure | FRESCO/DSN2020 | network | 4 of 26 clusters | 'network failure (4)' in the exit-107 DBSCAN cluster root causes |
| Burst-failure root cause: network + NFS congestion | FRESCO/DSN2020 | network/storage | 20 of 26 clusters | 'network+NFS congestion (20)' in the exit-107 DBSCAN cluster root causes |
| Startup failures (jobs dying in under 1 minute) | FRESCO/DSN2020 | user/app | 34% (A) / 45% (B) of failed jobs | '34% (A) / 45% (B) of failed jobs die in under 1 minute (startup failures), causing scheduling/initiation overhead waste' |
| SIGTERM (indeterminate user-or-system kill signal) | FRESCO/DSN2020 | unknown |  | 'SIGTERM can come from the user or from the scheduler killing a job on a failing node' (User/System row and caveats) |
| Local IO bottleneck failures (disk bottlenecks / faulty drivers restricting IO rate) | FRESCO/DSN2020 | storage/IO | failure-rate peak at ~6 MB/s (non-shared) and ~3 MB/s (shared) vs 100 MB/s rated | Table row 'Local IO correlation': 'a good number of jobs fail from disk bottlenecks or faulty drivers restricting IO rate' |
| Remote IO / parallel-filesystem contention failures (congestion, poor connectivity, co-located-job contention) | FRESCO/DSN2020 | storage/IO | B multi-node failure peak near 46 MB/s per node vs 1.1 TB/s rated | Table row 'Remote IO / parallel filesystem correlation'; Observation O5 on contention |
| Job size/duration (node-seconds) failure correlation | FRESCO/DSN2020 | user/app | B: failure rate increases linearly with runtime/node-seconds; A: opposite (negative slope) | Table row 'Job size/duration (node-seconds) correlation' (Observation O2) |
| Node unavailability / continuous downtime | FRESCO/DSN2020 | hardware | 95th-pct continuous downtime 24h (A) vs 20h (B); 95th-pct uptime 31 vs 92 days | Table row 'Node availability (from node-health data)' |
| TORQUE event codes A=abort, D=delete, E=exit (plus raw Exit_status) | FRESCO/DSN2020 | unknown |  | Caveats: repository exposes raw TORQUE Exit_status ('0 is success, others encode different error conditions') plus event codes (A=abort, D=delete, E=exit, etc.) |
| PEARC 2025 unified job states: COMPLETED, FAILED, ABORTED (and Slurm states for Anvil) | FRESCO/PEARC2025 | unknown | no per-state counts published (paywalled) | Caveats: 'maps PBS/TORQUE + Slurm exit codes to unified states (COMPLETED, FAILED, ABORTED, ...) across all 20.9M jobs' |
| Mature jobs (completed with zero exit code = Slurm COMPLETED) | MIT-SC/HPCA22 | user/app | 59.8% of jobs; 39.0% of GPU-hours | Table row 'Mature jobs (completed with zero exit code = Slurm COMPLETED)' (HPCA'22 Fig. 15) |
| Exploratory jobs (terminated early by the user = CANCELLED-like) | MIT-SC/HPCA22 | user/app | 17.7% of jobs; 34.4% of GPU-hours | Table row; hyper-parameter-tuning runs killed by users once training loss shows the config is suboptimal |
| Development jobs (debugging runs, runtime failures = FAILED-like, non-zero exit) | MIT-SC/HPCA22 | user/app | 19.0% of jobs; 8.4% of GPU-hours | Table row; jobs 'run until they encounter a failure or timeout'; median SM utilization 0% |
| IDE/interactive jobs (run until wall-clock limit = TIMEOUT-like) | MIT-SC/HPCA22 | user/app | 3.5% of jobs; 18.2% of GPU-hours | Table row; Jupyter/interactive sessions terminating at the 12 h or 24 h timeout limit |
| Hardware-caused job failures | MIT-SC/HPCA22 | hardware | <0.5% of job failures | Table row quoting 'Hardware reliability... accounts for less than 0.5% job failures'; 'GPU hardware reliability is currently not a concern' |
| Slurm outcome labels in slurm-log.csv (state, exit_code, derived_ec, derived_es, kill_requid) | MIT-SC dataset paper | unknown | no distribution published | Table row: schema documents 'state -- Final job state (completed, failed, etc.)', exit_code, derived exit code/state, kill_requid; CANCELLED/FAILED/TIMEOUT/OUT_OF_MEMORY shares mus |
| OUT_OF_MEMORY (Slurm state, shares unreported) | MIT-SC (caveats) | unknown | not reported anywhere | Caveats: 'No OUT_OF_MEMORY or NODE_FAIL shares are reported anywhere' |
| NODE_FAIL (Slurm state, shares unreported) | MIT-SC (caveats) | unknown | not reported anywhere | Caveats: 'No OUT_OF_MEMORY or NODE_FAIL shares are reported anywhere' |
| Fail-slow / less-reliable hardware | MIT-SC (recovery notes) | hardware |  | Recovery notes: techniques should 'minimize the impact of less-reliable or fail-slow hardware' |
| SWF outcome labels only, no cause taxonomy (status field = entire taxonomy) | PWA/SWF | unknown | 100% of failure records are cause-free | Table row 'IMPORTANT: outcome labels only, NO cause taxonomy'; no hardware/software/network/storage attribution anywhere in the format |
| status 1 = completed ('job completed successfully', exit code 0) | PWA/SWF | user/app | 86.3% of jobs (2,593,472 of 3,005,000); 80.5% of consumed core-seconds | Table row 'status 1 = completed' |
| status 0 = failed ('started to run but suffered some problem or exception condition') | PWA/SWF | user/app or system - indistinguishable | 8.4% of jobs; 13.3% of core-seconds; per-log range 0-88.8% | Table row 'status 0 = failed'; 35-45% of core-seconds on CM5/CTC/KTH/O2K went to failed jobs |
| status 5 = cancelled ('killed by the user, possibly before starting') | PWA/SWF | user/app | 5.3% of jobs; 6.2% of core-seconds; per-log range 0-30.5% | Table row 'status 5 = cancelled'; RICC anomaly: cancelled jobs recorded as consuming processor time |
| status 2/3/4 = partial-execution codes (continued / last-partial-completed / last-partial-failed) | PWA/SWF | unknown | 0 occurrences in all 16 logs checked | '2/3/4=partial-execution codes (continued / last-partial-completed / last-partial-failed; 0 occurrences in all 16 logs I checked)' |
| status -1 = unknown / status not credible | PWA/SWF | unknown | 3.6% of all jobs; 2 of 16 logs 100% unknown | Table row 'status -1 = unknown'; NASA iPSC and ANL Intrepid carry no outcome information; HPC2N 99.8%-completed not credible |
| Site coding artifact: failed vs cancelled is a logging convention, not behavior | PWA/SWF | unknown | 5 of 16 logs use ONLY status 0; 4 use ONLY status 5; 2 have no status | Table row; SWF doc: the distinction 'is not necessarily accurate, as the distinction typically does not appear in the original logs' |
| System kills for exceeding runtime limits (land in either failed or cancelled) | PWA/SWF (caveats) | unknown |  | Caveats: 'jobs killed by the system for exceeding runtime limits may land in either code' |
| Unrepresentative bring-up failures (LLNL uBGL outlier) | PWA/SWF | facility/system bring-up | 90.0% of jobs non-successful (101,331 of 112,611); 99,401 failed within 5 seconds | Table row; 'the machine was new and unstable at the time this log was recorded' |
| Missing downtime/failure data: maintenance, software failures, hardware failures (unlogged, jobs truncated/resubmitted) | PWA/SWF | hardware/software/facility - unlogged | not quantifiable from SWF | Table row citing paper Sec 3.7: interruptions absent from logs; affected jobs 'may be truncated and re-submitted later' |
| HPC1 replacement: Hard drive | CFDR/FAST07 Table 3 | hardware | 30.6% of hardware replacements | HPC1 component replacement shares row, categories AS NAMED in service records |
| HPC1 replacement: Memory | CFDR/FAST07 Table 3 | hardware | 28.5% | HPC1 replacement shares row; DIMM replacement rate ~= disk replacement rate when normalized |
| HPC1 replacement: Misc/Unknown | CFDR/FAST07 Table 3 | hardware | 14.4% | HPC1 replacement shares row |
| HPC1 replacement: CPU | CFDR/FAST07 Table 3 | hardware | 12.4% | HPC1 replacement shares row; CPU replaced ~2.5x less often than a disk |
| HPC1 replacement: PCI motherboard | CFDR/FAST07 Table 3 | hardware | 4.9% | HPC1 replacement shares row |
| HPC1 replacement: Controller | CFDR/FAST07 Table 3 | hardware | 2.9% | HPC1 replacement shares row |
| HPC1 replacement: QSW (Quadrics switch) | CFDR/FAST07 Table 3 | hardware | 1.7% | HPC1 replacement shares row |
| HPC1 replacement: Power supply | CFDR/FAST07 Table 3 | hardware | 1.6% | HPC1 replacement shares row |
| HPC1 replacement: MLB | CFDR/FAST07 Table 3 | hardware | 1.0% | HPC1 replacement shares row |
| HPC1 replacement: SCSI BP | CFDR/FAST07 Table 3 | hardware | 0.3% | HPC1 replacement shares row |
| HPC1 node-outage root cause: CPU | CFDR/FAST07 Table 2 | hardware | 44% of hardware-attributed node outages | Node-outage root cause by hardware component row |
| HPC1 node-outage root cause: Memory | CFDR/FAST07 Table 2 | hardware | 29% | Node-outage root cause row |
| HPC1 node-outage root cause: Hard drive | CFDR/FAST07 Table 2 | hardware | 16% | Node-outage root cause row; ~90% of disk-attributed problems led to actual replacement |
| HPC1 node-outage root cause: PCI motherboard | CFDR/FAST07 Table 2 | hardware | 9% | Node-outage root cause row |
| HPC1 node-outage root cause: Power supply | CFDR/FAST07 Table 2 | hardware | 2% | Node-outage root cause row |
| Parity errors cleared by reboot (CPU/memory outages) | CFDR/FAST07 | hardware |  | Severity caveat: 'many CPU/memory outages were parity errors cleared by reboot' |
| COM1 replacement: Power supply | CFDR/FAST07 (COM1) | hardware | 34.8% | COM1 (ISP, 26,734 SCSI disks) replacement shares row |
| COM1 replacement: Memory | CFDR/FAST07 (COM1) | hardware | 20.1% | COM1 replacement shares row |
| COM1 replacement: Hard drive | CFDR/FAST07 (COM1) | hardware | 18.1% | COM1 replacement shares row; disks runner-up behind power supplies |
| COM1 replacement: Case | CFDR/FAST07 (COM1) | hardware | 11.4% | COM1 replacement shares row |
| COM1 replacement: Fan | CFDR/FAST07 (COM1) | hardware | 8.0% | COM1 replacement shares row |
| COM1 replacement: CPU | CFDR/FAST07 (COM1) | hardware | 2.0% | COM1 replacement shares row |
| COM1 replacement: NIC card | CFDR/FAST07 (COM1) | hardware | 1.2% | COM1 replacement shares row |
| COM1 replacement: SCSI board | CFDR/FAST07 (COM1) | hardware | 0.6% | COM1 replacement shares row |
| COM1 replacement: LV power board | CFDR/FAST07 (COM1) | hardware | 0.6% | COM1 replacement shares row |
| COM1 replacement: CPU heatsink | CFDR/FAST07 (COM1) | hardware | 0.6% | COM1 replacement shares row |
| COM2 replacement: Hard drive ('Replace hard drive') | CFDR/FAST07 (COM2) | hardware | 49.1% | COM2 (ISP warranty log) replacement shares row; repair codes AS NAMED |
| COM2 replacement: Motherboard | CFDR/FAST07 (COM2) | hardware | 23.4% | COM2 replacement shares row |
| COM2 replacement: Power supply | CFDR/FAST07 (COM2) | hardware | 10.1% | COM2 replacement shares row |
| COM2 replacement: RAID card | CFDR/FAST07 (COM2) | hardware | 4.1% | COM2 replacement shares row |
| COM2 replacement: Memory | CFDR/FAST07 (COM2) | hardware | 3.4% | COM2 replacement shares row |
| COM2 replacement: SCSI cable | CFDR/FAST07 (COM2) | hardware | 2.2% | COM2 replacement shares row |
| COM2 replacement: Fan | CFDR/FAST07 (COM2) | hardware | 2.2% | COM2 replacement shares row |
| COM2 replacement: CPU | CFDR/FAST07 (COM2) | hardware | 2.2% | COM2 replacement shares row |
| COM2 replacement: CD-ROM | CFDR/FAST07 (COM2) | hardware | 0.6% | COM2 replacement shares row |
| COM2 replacement: RAID controller | CFDR/FAST07 (COM2) | hardware | 0.6% | COM2 replacement shares row |
| Annual disk replacement rate (ARR) vs datasheet AFR | CFDR/FAST07 Table 1 | storage/IO | HPC2 1.1%; HPC3 3.7%/3.0%/3.3% (SCSI/metadata/SATA); COM1 2.8%; COM2 3.1%; COM3 3.6-24.1%; weighted avg 3.01% vs datasheet AFR 0.58-0.88% | Table row 'Annual disk replacement rates (ARR) vs datasheet AFR'; ~3.4x datasheet |
| Seaborg disk failures (ARR) | CFDR/NERSC LBNL-934480 | storage/IO | ~1.5%/yr (4,280 disks) | NERSC component failures row: 'Seaborg disk ARR ~1.5%/yr' |
| HPSS tape drive failures (ARR) | CFDR/NERSC LBNL-934480 | storage/IO | 15-20%/yr vs ~3% implied by datasheet MTBF 290,000 hr | NERSC row: 'HPSS tape drive ARR 15-20%/yr' |
| HPSS disk failures (ARR, known undercount) | CFDR/NERSC LBNL-934480 | storage/IO | <1% (floor; records 'inadequate') | NERSC row: 'HPSS disk ARR <1% (known undercount)' |
| Software failure (dominant cause of Seaborg unavailability) | CFDR/NERSC LBNL-934480 | software | dominant cause of unavailability | NERSC row detail: 'software failure was the dominant cause of unavailability' |
| File-system failures (leading component category, via VSD/I/O nodes) | CFDR/NERSC LBNL-934480 | storage/IO | leading component category | 'file-system failures were the leading component category (many component failures manifest as file-system failure via VSD/I/O nodes)' |
| SP Switch failures (hardware + CSS software) | CFDR/NERSC LBNL-934480 | network | a large downtime fraction | 'SP Switch (hardware+CSS software) a large downtime fraction' |
| 2004 OS upgrade outage (large one-off) | CFDR/NERSC LBNL-934480 | software |  | 'large one-off outages from a 2004 OS upgrade and a 2006 security incident' |
| 2006 security incident outage (large one-off) | CFDR/NERSC LBNL-934480 | software/security |  | 'large one-off outages from a 2004 OS upgrade and a 2006 security incident' |
| Power outages (HPSS) | CFDR/NERSC LBNL-934480 | facility | comparable to unscheduled SW+HW downtime | 'power outages comparable to unscheduled SW+HW' |
| Tape cartridge media errors (most common tape-drive failure cause) | CFDR/NERSC LBNL-934480 | storage/IO | most common tape-drive failure cause | 'most common tape-drive failures caused by tape cartridges (media error)' |
| Infant mortality of new batches + aging (Seaborg disks and HPSS tape drives) | CFDR/NERSC LBNL-934480 | storage/IO | 2003 spike, dip 2004, rising 2005-06 | 'Failure-vs-age trend... shows infant mortality of new batches plus aging' |
| PNNL MPP2 hardware failure records (failed component + failure description + repair action; no published breakdown) | CFDR/PNNL MPP2 | hardware | NO published component-share breakdown | Table row: per-record schema = timestamp, hardware identifier, failed component, failure description, repair action taken; raw download gated behind CFDR registration |
| LANL root-cause category: Human | CFDR/LANL (JPCS'07 Fig. 1) | human | part of remainder after Hardware >50% and Software ~20% | Six root-cause categories AS NAMED: Human, Environment (power/AC), Network, Software, Hardware, Unknown |
| LANL root-cause category: Environment (power/AC) | CFDR/LANL (JPCS'07 Fig. 1) | facility | part of remainder | Six root-cause categories AS NAMED in LANL 22-system/23,000-failure log |
| LANL root-cause category: Network | CFDR/LANL (JPCS'07 Fig. 1) | network | part of remainder | Six root-cause categories AS NAMED |
| LANL root-cause category: Software | CFDR/LANL (JPCS'07 Fig. 1) | software | ~20% of node outages | 'Hardware >50% of node outages, Software ~20%' |
| LANL root-cause category: Hardware | CFDR/LANL (JPCS'07 Fig. 1) | hardware | >50% of node outages | 'Hardware >50% of node outages'; ~0.1 failures/socket/yr, linear with socket count |
| LANL root-cause category: Unknown | CFDR/LANL (JPCS'07 Fig. 1) | unknown | unknown fraction significant | 'remainder Network / Environment / Human / Unknown (unknown fraction significant)' |
| Correlated disk failures (second drive failure during RAID reconstruction) | CFDR/FAST07 (headline + recovery notes) | storage/IO | P(second failure within 1 hr) 4x exponential prediction; 2x within 10 hr | 'RAID implication: P(second drive failure within 1 hr) is 4x the exponential prediction'; Weibull shape 0.71-0.76, decreasing hazard, autocorrelation to ~100 weeks |
| No-problem-found (NPF) returned drives | CFDR/FAST07 (caveats) | storage/IO | 43% of returned drives had no problem found | Caveat (1): 'a disk vendor reported 43% of returned drives had no problem found'; also NERSC tape drives returned to service after vendor finds no fault (NPF) |
| Bad-batch SATA media errors from lubricant breakdown / high head fly height (HPC3) | CFDR/FAST07 (caveats) | storage/IO | all 11,000 SATA drives swapped Oct 2006; recorded as warranty replacement, NOT failures | Caveat (4): 'HPC3's 11,000 SATA drives were all swapped in Oct 2006 for media errors from lubricant breakdown/high head fly height' |
| Binary drive 'failure' label (dataset outcome column, failure=1) | Backblaze Drive Stats | storage/IO | 2025 annual AFR 1.36%; lifetime 1.30%; Q4 2025 1.13% | Table row 'Binary drive failure label'; NO root-cause taxonomy (no head crash vs electronics vs firmware breakdown); failed = removed because it totally stopped working or showed e |
| Reactive failure (drive dead: won't spin up/connect, won't respond to console/system commands, won't sync or stay synced in RAID, RAID reports drive can't be read or written) | Backblaze Drive Stats | storage/IO | reactive-vs-proactive split not published | Table row 'Reactive failure (drive dead)' listing Backblaze's stated criteria |
| Proactive failure (impending-failure replacement via SMART thresholds / FSCK file-system checks) | Backblaze Drive Stats | storage/IO | share not published separately; triggered when any of 5 critical SMART raw values > 0 | Table row 'Proactive failure'; drive pulled via CVT migration/cloning before it dies; deliberate removals do NOT count |
| SMART-signaled failures (>=1 of 5 critical attributes > 0) | Backblaze Drive Stats | storage/IO | 76.7% of failed drives vs 4.2% base rate in healthy drives | Table row 'SMART-signaled failures (predictive-attribute coverage)' |
| Failures with NO SMART warning | Backblaze Drive Stats | storage/IO | 23.3% of failures | '23.3% of failures had NO SMART warning at all'; recovery notes: ~1 in 4 drive failures arrives unpredicted |
| SMART 5 (Reallocated Sectors Count) as failure predictor | Backblaze Drive Stats | storage/IO |  | Named among 'the five predictor attributes Backblaze names' |
| SMART 187 (Reported Uncorrectable Errors) as failure predictor | Backblaze Drive Stats | storage/IO | cleanest signal | 'SMART 187 is the cleanest signal (drives with zero uncorrectable errors hardly ever fail...)' |
| SMART 188 (Command Timeout) as failure predictor | Backblaze Drive Stats | storage/IO |  | Named among the five critical predictor attributes |
| SMART 197 (Current Pending Sector Count) as failure predictor | Backblaze Drive Stats | storage/IO |  | Named among the five critical predictor attributes |
| SMART 198 (Offline/Uncorrectable Sector Count) as failure predictor | Backblaze Drive Stats | storage/IO |  | Named among the five critical predictor attributes |
| Model/vintage AFR variance (e.g. HGST HUH728080ALE600 10.29%, Seagate ST10000NM0086 5.23%, Toshiba MG08ACA16TEY 4.14%, historic Seagate ST3000DM001 >25-30%) | Backblaze Drive Stats | storage/IO | AFR spans 0% to 10.29% across models in 2025 (~7.5x fleet average); historic vintages >25-30% | Table row 'Model/vintage AFR variance (best vs worst models, 2025)'; model/vintage is a 1-2 order-of-magnitude reliability factor |
| MMU Error (Xid 31) | Delta (Cui/Cao SC'25) | hardware | A100: 8,863 (60% of A100 critical errors); H100: 1,737 (95% of H100 critical errors); job-failure probability 90.48% A100 / 73.80% H100 | Table row: 'MMU Error (Xid 31) ... Dominant critical error on both GPUs by count; mostly application-induced illegal memory access' |
| GSP Error (Xid 119/120, GSP RPC timeout) | Delta (Cui/Cao SC'25) | hardware | A100: 3,857; H100: 3; job-failure probability 100% on A100 | Table row: 'GPU System Processor hangs; requires GPU reset/node reboot. Nearly eliminated on H100' |
| NVLink Error (Xid 74) | Delta (Cui/Cao SC'25) | network | A100: 1,922; H100: 0; job-failure probability 53.75% (A100) | Table row: 'Interconnect errors; absent on the GH200 H100 nodes studied' |
| PMU SPI Error (Xid 122/123) | Delta (Cui/Cao SC'25) | hardware | A100: 77; H100: 0; job-failure probability 97.56% (A100) | Table row: 'Power-management unit communication failure; failure mechanism not fully documented by NVIDIA' |
| Double-Bit ECC / DBE (Xid 48) | Delta (Cui/Cao SC'25) | hardware | A100: 1; H100: 17; job-failure probability 100% (H100) | Table row: 'Uncorrectable memory error; triggers row remapping' |
| Consecutive SBEs (degraded correctable errors) | Delta (Cui/Cao SC'25) | hardware | A100: 33; H100: 7 | Table row: 'Repeated single-bit errors on same location treated as uncorrectable-class; individual SBEs are NOT logged' |
| Row Remapping Event (Xid 63) | Delta (Cui/Cao SC'25) | hardware | A100: 34; H100: 16 | Table row: 'Recovery action logged as error; remapping succeeds in only 59% of H100 uncorrectable-memory cases' |
| Row Remapping Failure (Xid 64) | Delta (Cui/Cao SC'25) | hardware | A100: 0; H100: 8; job-failure probability 100% (H100) | Table row: 'Spare-row exhaustion (512-row cap) — authors argue mechanism is insufficient for H100's 96GB' |
| Contained Memory Error (Xid 94) | Delta (Cui/Cao SC'25) | hardware | A100: 13; H100: 14; job-failure probability 100% for affected process (both) | Table row: 'Error contained to the offending process, which is terminated; rest of node survives' |
| Uncontained Memory Error (Xid 95) | Delta (Cui/Cao SC'25) | hardware | A100: 11; H100: 19; containment fails in 8% of H100 memory-error cases | Table row: 'Described as highly bursty and persistent; requires node reboot' |
| GPU Fallen Off Bus (Xid 79) | Delta (Cui/Cao SC'25) | hardware | A100: 10; H100: 0 | Table row: 'PCIe detachment; node reboot required' |
| Node lockups (unlogged failures) | Delta (Cui/Cao SC'25) | unknown | 27 A100 (0.18% of A100 errors), 9 H100 (0.49%) | Table row: 'Driver dies before logging Xid; a known undercount source acknowledged by authors' |
| Single-bit errors (SBEs, auto-corrected, unlogged) | Delta (Cui/Cao SC'25) | hardware | not logged (no correctable-error counts exist in the dataset) | Recovery notes: 'ECC is SECDED; individual SBEs auto-correct and are unlogged'; caveat (6): 'correctable SBEs are not logged at all' |
| Storage failures (missing-log source) | Delta (Cui/Cao SC'25) |  |  | Caveat (3): 'missing logs from storage failures and node lockups where the driver dies before logging ... mean error counts are lower bounds' |
| Single-Bit Errors (SBEs) | Ampere-mem (Zhu et al. arXiv:2508.03513) | hardware | Delta: 173,936 SBEs, 0.53/GPU/day, 43 GPUs (5.06%); Perlmutter: 7,010,888 SBEs, 2.83/GPU/day, 344 GPUs (4.52%); Polaris: not recorded | Table row: 'Correctable by SECDED ECC; transparent to applications. Highly bursty: 94.31% of SBE interarrival times on Delta are under 1 hour' |
| Double-Bit Errors (DBEs) | Ampere-mem (Zhu et al. arXiv:2508.03513) | hardware | Delta: 9 (0.000027/GPU/day, 2 GPUs); Polaris: 39,837 (0.069/GPU/day, 68 GPUs); Perlmutter: 17,926 (0.0082/GPU/day, 35 GPUs); <0.53% of GPUs affected | Table row: 'Detected but uncorrectable by ECC ... every DBE is application-fatal' |
| Database storage error (monitoring-side data-gap cause) | Ampere-mem (Zhu et al. arXiv:2508.03513) |  | 4 missing days on Delta, several missing months on Perlmutter | Caveat (3): 'data gaps — 4 missing days on Delta and several missing months on Perlmutter from a database storage error' |
| Illegal Address (illegal Load/Store address) | Beam-DUE (dos Santos et al. TNS/NSREC, arXiv:2108.00554) | hardware | Dominant DUE source with ECC OFF; <8% of DUEs on Kepler / <2% on Volta with ECC ON (ECC removes up to 92%/98%) | Table row: 'Neutron-induced bit flips ... corrupt the memory address held for a Load/Store; the corrupted access violates the memory policy and the CUDA runtime kills the kernel' |
| Misaligned Address | Beam-DUE (dos Santos et al. TNS/NSREC, arXiv:2108.00554) | hardware | tracked as separate bar of the Illegal/Misaligned pair in Fig. 3 | Table detail: "Fig. 3 tracks 'Illegal Addr.' and 'Misaligned Addr.' as separate bars of this pair"; Sec. III taxonomy lists 'Illegal or Misaligned Address' |
| ECC Uncorrectable (double-bit error detected by SECDED) | Beam-DUE (dos Santos et al. TNS/NSREC, arXiv:2108.00554) | hardware | Absent ECC OFF; major DUE share ECC ON; single largest category on Volta ECC-ON GEMM (~45-70% of DUEs); grows linearly with precision | Table row: 'SECDED detects but cannot correct multi-bit flips and crashes the application ... ECC suppresses SDCs and Illegal Address DUEs but converts them into ECC-Uncorrectable  |
| Launch Failure | Beam-DUE (dos Santos et al. TNS/NSREC, arXiv:2108.00554) | software | Second most frequent traceable source; roughly 20-50% of DUEs in Kepler ECC-ON and Volta configurations | Table row: 'CPU tries to launch a kernel and fails: GPU left in an inconsistent state ... The TNS version calls these interface errors' |
| System Crash (watchdog-triggered; source untraceable) | Beam-DUE (dos Santos et al. TNS/NSREC, arXiv:2108.00554) | unknown | Roughly 15-40% of DUEs across benchmarks; near-total for a few Kepler ECC-OFF codes | Table row: "Host-OS exception or hung kernel prevents the logging API from returning, so the cause 'could not be traced or is generally unknown'" |
| Memory Allocation (CUDA cannot allocate memory) | Beam-DUE (dos Santos et al. TNS/NSREC, arXiv:2108.00554) | software | Negligible except BFS (~60%+ of BFS ECC-ON DUEs on Kepler) | Table row: 'BFS manages memory inefficiently ... most of its DUEs come from memory errors' |
| Illegal Instruction | Beam-DUE (dos Santos et al. TNS/NSREC, arXiv:2108.00554) | hardware | Small share, single-digit % in a few Fig. 3 bars | Table row: 'An illegal instruction is executed, leaving the process in an inconsistent status — instruction-word or PC corruption' |
| Devices Unavailable | Beam-DUE (dos Santos et al. TNS/NSREC, arXiv:2108.00554) | software | part of 'Other' group, <3% of DUEs combined | Table 'Other' row: "Devices Unavailable (GPU 'falsely full'/not released)" |
| Invalid Value | Beam-DUE (dos Santos et al. TNS/NSREC, arXiv:2108.00554) | software | part of 'Other' group, <3% of DUEs combined | Table 'Other' row: 'Invalid Value (kernel params out of range, e.g., too many threads)' |
| No Device / Invalid Device | Beam-DUE (dos Santos et al. TNS/NSREC, arXiv:2108.00554) | software | part of 'Other' group, <3% of DUEs combined | Table 'Other' row lists 'Invalid Device / No Device' in the Sec. III CUDA-runtime taxonomy |
| Initialization Error | Beam-DUE (dos Santos et al. TNS/NSREC, arXiv:2108.00554) | software | part of 'Other' group, <3% of DUEs combined | Table 'Other' row: 'Initialization Error (driver fails to init)' |
| Hardware Stack Error | Beam-DUE (dos Santos et al. TNS/NSREC, arXiv:2108.00554) | software | part of 'Other' group, <3% of DUEs combined | Table 'Other' row: 'Hardware Stack Error (call-stack corruption / stack-size limit)' |
| Invalid PC | Beam-DUE (dos Santos et al. TNS/NSREC, arXiv:2108.00554) | software | part of 'Other' group, <3% of DUEs combined | Table 'Other' row lists 'Invalid PC' in the Sec. III CUDA-runtime taxonomy |
| Invalid Address Space | Beam-DUE (dos Santos et al. TNS/NSREC, arXiv:2108.00554) | software | part of 'Other' group, <3% of DUEs combined | Table 'Other' row: 'Invalid Address Space (instruction operates in wrong memory space)' |
| SDC (Silent Data Corruption) | Beam-DUE (dos Santos et al. TNS/NSREC, arXiv:2108.00554) |  | ECC OFF: SDC FIT > DUE FIT (1.2x Kepler, 4.1x Volta); ECC ON flips it (DUE 2.2x/2.7x SDC); ECC cuts Kepler SDC FIT up to 21x | Headline numbers: 'ECC OFF: SDC FIT > DUE FIT on average (1.2x on Kepler, 4.1x on Volta)' — SDC is the companion outcome class to DUE throughout |
| (scope-note table row) raw labels only: exit status/completion codes, RAS_EVENT severities INFO/WARN/FATAL, THETA_HARDWARE_ERROR — no curated cause taxonomy in the DataPort dataset | ALCF-catalog (DataPort + Di et al. DSN 2019) | unknown | n/a | First table row: 'IMPORTANT SCOPE NOTE: the DataPort dataset itself exposes only raw labels, not a curated cause taxonomy' |
| Normal (exit code 0) | ALCF-catalog (Di et al. DSN 2019, Mira) | n/a | 73.79% of all task terminations; contributed 58% of core-hours | Table row: 'Normal (exit code 0) ... ~3/4 of jobs exited normally' |
| Timeout | ALCF-catalog (Di et al. DSN 2019, Mira) | user/app | 14.62% of all terminations; 55.8% of abnormal jobs; wasted 32.86% of total core-hours | Table row: 'Execution time exceeded requested wall time. Dominant failure mode ... Best-fit interruption-interval distribution: Erlang/exponential' |
| Bug | ALCF-catalog (Di et al. DSN 2019, Mira) | user/app | 7.25% of all terminations (Table IV row ~7.35%) | Table row: 'Serious termination signals: SIGABRT ... and SIGSEGV ... Best-fit failure-length distribution: Pareto' |
| SIGABRT (abort: assertion, double-free) | ALCF-catalog (Di et al. DSN 2019, Mira) | user/app | component of the Bug category (7.25%) | Bug row detail: 'SIGABRT (abort assertion, double-free)' |
| SIGSEGV (segfault) | ALCF-catalog (Di et al. DSN 2019, Mira) | user/app | component of the Bug category (7.25%) | Bug row detail: 'SIGSEGV (segfault)' |
| Kill (signal 9, user/operator) | ALCF-catalog (Di et al. DSN 2019, Mira) | user/app | 2.84% of all terminations | Table row: 'Killed mid-execution with signal 9, not due to bug or wall-time — user/operator kills' |
| IO (user file-management mistakes) | ALCF-catalog (Di et al. DSN 2019, Mira) | user/app | 0.94% of all terminations | Table row: 'User mistakes managing files, not file-system faults ... Best-fit: inverse Gaussian' |
| errno 2 No such file or directory | ALCF-catalog (Di et al. DSN 2019, Mira) | user/app | example within IO category (0.94%) | IO row detail: "e.g. 'errno 2 No such file or directory'" |
| errno 21 Is a directory | ALCF-catalog (Di et al. DSN 2019, Mira) | user/app | example within IO category (0.94%) | IO row detail: "'errno 21 Is a directory'" |
| errno 13 Permission denied | ALCF-catalog (Di et al. DSN 2019, Mira) | user/app | example within IO category (0.94%) | IO row detail: "'errno 13 Permission denied' on load" |
| RAS (system reliability) | ALCF-catalog (Di et al. DSN 2019, Mira) | hardware | 0.17% of all terminations = ~0.6% of failed jobs | Table row: 'Tasks killed by fatal RAS events — the ONLY system-attributed category ... Best-fit: Weibull' |
| Unknown | ALCF-catalog (Di et al. DSN 2019, Mira) | unknown | 0.15% of all terminations | Table row: 'Terminated with unknown reason, e.g. missing messages' |
| SIGILL (signal 4, illegal instruction) | ALCF-catalog (Di et al. DSN 2019, Mira) | user/app | 0.065% of all terminations | Table row: 'Signals 4/5/8: illegal instruction (mismatched CPU arch or permission issue)' |
| SIGTRAP (signal 5, caught exceptions) | ALCF-catalog (Di et al. DSN 2019, Mira) | user/app | 0.062% of all terminations | Table row: 'caught exceptions (possible bugs during debugging)' |
| SIGFPE (signal 8, erroneous arithmetic) | ALCF-catalog (Di et al. DSN 2019, Mira) | user/app | 0.014% of all terminations | Table row: 'erroneous arithmetic (divide by zero)' |
| Blue Gene/Q compute card (RAS category) | ALCF-catalog (Di et al. DSN 2019, Mira) | hardware | 78.16% of system-reliability job failures (Table XVII) | RAS-breakdown row: 'Blue Gene/Q compute card 78.16%' |
| Software_Error (RAS category) | ALCF-catalog (Di et al. DSN 2019, Mira) | hardware | 16.22% of system-reliability job failures | RAS-breakdown row: 'Software_Error 16.22%' |
| Message Unit (MU, network) (RAS category) | ALCF-catalog (Di et al. DSN 2019, Mira) | hardware | 2.81% of system-reliability job failures | RAS-breakdown row: 'Message Unit (MU, network) 2.81%' |
| Generic Card/Board (RAS category) | ALCF-catalog (Di et al. DSN 2019, Mira) | hardware | 2.65% of system-reliability job failures | RAS-breakdown row: 'Generic Card/Board 2.65%' |
| Bulk Power Supply (RAS category) | ALCF-catalog (Di et al. DSN 2019, Mira) | hardware | 0.16% of system-reliability job failures | RAS-breakdown row: 'Bulk Power Supply 0.16%' |
| FIRMWARE (RAS component) | ALCF-catalog (Di et al. DSN 2019, Mira) | hardware | 62.1% by component | RAS-breakdown detail: 'FIRMWARE 62.1% ... Firmware named the major root cause of job-terminating system events' |
| Machine Controller on Service Node (RAS component) | ALCF-catalog (Di et al. DSN 2019, Mira) | hardware | 21.53% by component | RAS-breakdown detail: 'Machine Controller on Service Node 21.53%' |
| Kernel Panic (RAS component) | ALCF-catalog (Di et al. DSN 2019, Mira) | hardware | 11.39% by component | RAS-breakdown detail: 'Kernel Panic 11.39%'; message ID 000A000D (kernel panic) 11.39% |
| Compute Node Kernel (RAS component) | ALCF-catalog (Di et al. DSN 2019, Mira) | hardware | 4.52% by component | RAS-breakdown detail: 'Compute Node Kernel 4.52%' |
| Memory Unit (RAS component) | ALCF-catalog (Di et al. DSN 2019, Mira) | hardware | 0.32% by component | RAS-breakdown detail: 'Memory Unit 0.32%' |
| Control System on Service Node (RAS component) | ALCF-catalog (Di et al. DSN 2019, Mira) | hardware | 0.16% by component | RAS-breakdown detail: 'Control System on Service Node 0.16%' |
| RAS message ID 00080014 (node error) | ALCF-catalog (Di et al. DSN 2019, Mira) | hardware | 26.37% of RAS-failed jobs | RAS-breakdown detail: 'top IDs: 00080014 (node error) 26.37%' |
| RAS message ID 0008000B (node error) | ALCF-catalog (Di et al. DSN 2019, Mira) | hardware | 14.04% of RAS-failed jobs | RAS-breakdown detail: '0008000B (node error) 14.04%' |
| RAS message ID 000A000D (kernel panic) | ALCF-catalog (Di et al. DSN 2019, Mira) | hardware | 11.39% of RAS-failed jobs | RAS-breakdown detail: '000A000D (kernel panic) 11.39%' |
| RAS message ID 00040106 | ALCF-catalog (Di et al. DSN 2019, Mira) | hardware | 11.23% of RAS-failed jobs | RAS-breakdown detail: '00040106 11.23% — Pareto-like 75/25 rule' |
| COMPLETED (baseline) | Eagle-Kestrel (OEDI 5860 + 8643) | user/app | Eagle 67.00% of jobs / 41.49% of node-hours; Kestrel 66.21% / 41.03% | Table row: 'Roughly one third of all jobs on both systems do NOT complete cleanly' |
| CANCELLED | Eagle-Kestrel (OEDI 5860 + 8643) | user/app | Eagle 16.44% of jobs / 9.19% of node-hours; Kestrel 14.53% / 7.97% | Table row: "Datasets collapse 'CANCELLED by <uid>' to CANCELLED" |
| CANCELLED by 0 (root/admin, system-initiated) | Eagle-Kestrel (OEDI 8643, Kestrel) |  | 54,289 Kestrel jobs | CANCELLED row detail: "54,289 jobs were 'CANCELLED by 0' (root/admin), i.e. a small system-initiated component hides inside this user-dominated category" |
| FAILED (non-zero exit code) | Eagle-Kestrel (OEDI 5860 + 8643) | user/app | Eagle 8.84% of jobs / 4.08% of node-hours; Kestrel 12.90% / 3.90% | Table row: "Largest explicit failure label. No cause attribution whatsoever: Slurm's FAILED covers application bugs, bad inputs, environment/software errors alike" |
| TIMEOUT (walltime kill) | Eagle-Kestrel (OEDI 5860 + 8643) | user/app | Eagle 7.28% of jobs / 43.47% of node-hours; Kestrel 5.30% / 43.52% | Table row: 'The dominant consumer of node-time on both systems ... some users intentionally allow their jobs to time out' |
| OUT_OF_MEMORY | Eagle-Kestrel (OEDI 5860 + 8643) | user/app | Eagle 0.185% of jobs / 0.034% of node-hours; Kestrel 0.416% / 0.089% | Table row: 'OOM-killer terminations; small by count and negligible by node-time ... Doubled in share on Kestrel' |
| NODE_FAIL | Eagle-Kestrel (OEDI 5860 + 8643) | hardware | Eagle 0.110% of jobs (12,088) / 1.62% of node-hours; Kestrel 0.342% (36,070) / 3.50% | Table row: 'The only label unambiguously attributable to the system rather than the user ... node failures disproportionately kill large/long jobs' |
| DEADLINE (Kestrel only) | Eagle-Kestrel (OEDI 8643, Kestrel) | software | Kestrel 0.304% of jobs (32,071) / ~0% of node-hours | Table row: 'Scheduler deadline terminations; absent from the Eagle trace' |
| PENDING / RUNNING (censoring artifact) | Eagle-Kestrel (OEDI 5860 + 8643) | unknown | Eagle 0.133% + 0.008%; Kestrel 1 job | Table row: 'End-of-trace snapshot states, not outcomes; must be excluded from failure-rate denominators' |
| Unsuccessful jobs (umbrella = failed + aborted) | ATLAS-TwoSigma | unknown | TwoSigma ~27-30% of jobs and ~half of all CPU time (figure-read); Google 1.4-6.8x higher fraction than every other trace; Mustang ~10%; OpenTrinity ~25-30% | Table row: 'Unsuccessful jobs (umbrella = failed + aborted), as named by the authors' — defined as jobs ending 'due to events whose occurrence was not intended by users or system a |
| Failed jobs | ATLAS-TwoSigma | unknown | TwoSigma: 100% of unsuccessful jobs carry the 'failed' mark; no root-cause split available | Table row: 'no event type other than failure is recorded'; authors do not distinguish failed jobs by root cause (software vs hardware) because 'this information is not reliably ava |
| Aborted jobs (user kills / evictions / unknown exit at Google; intentional cancellations at LANL) | ATLAS-TwoSigma | user/app | Google: 'almost all unsuccessful jobs... were aborted'; TwoSigma: indistinguishable (folded into failed); LANL: recorded as CANCELLED | Table row: Google trace docs say aborts may come from the user, the scheduler, or death of a dependency |
| Timeout jobs (job killed at user-specified time limit, LANL only) | ATLAS-TwoSigma | user/app | 49-55% of ALL CPU time at LANL goes to jobs that time out (49% on Mustang); TwoSigma has NO timeouts (no time limits) | Table row: 'Timeout jobs (LANL only — job killed at user-specified time limit)'; reported separately from unsuccessful |
| Mustang outcome labels: COMPLETED / CANCELLED / TIMEOUT (no FAILED or NODE_FAIL status exists) | ATLAS-TwoSigma | unknown | no per-label distribution published in the FAQ; hardware/software failures hide inside CANCELLED | Table row: Mustang FAQ says cancellations are 'triggered by a user or as the result of a failure in software or hardware' — indistinguishable |
| Dependency-driven batch cancellations (Mustang) | ATLAS-TwoSigma | unknown |  | Row detail: batch cancellations (identical timestamp+duration across jobs) come from dependency chains where one job's failure auto-cancels dependents — 'the trace's only run-lengt |
| Success-rate vs CPU-hours decline (proxy for hardware-MTBF-driven failure) | ATLAS-TwoSigma | unknown | TwoSigma success rate falls from ~70% (<1 CPU-hr) to ~35% (>10^4 CPU-hr); Google falls to <10%; LANL stays ~85-95% | Table row: 'Success-rate vs CPU-hours trend (proxy for hardware-MTBF-driven failure)' [Fig. 9, figure-read] |
| Re-submission behavior (nearest thing to failure run lengths) | ATLAS-TwoSigma | user/app | 83-93% of jobs submitted exactly once (all traces); unsuccessful jobs re-submitted more than successful ones — the one failure trend consistent across all four traces | Table row: 'Re-submission behavior (nearest thing to failure run lengths)' |
| JOBEND / JOBFAIL / JOBCANCEL (Moab workload-trace event labels) | ATLAS-TwoSigma | unknown | appear in NONE of the published docs or papers; no share reportable | Caveats prose: 'The requested JOBEND/JOBFAIL/JOBCANCEL labels appear in NONE of the published docs or papers — that is Moab workload-trace event vocabulary... plausibly the raw log |
| NODE_FAIL (Slurm state, explicitly absent from Mustang) | ATLAS-TwoSigma | unknown | does not exist as a Mustang status | Table row: 'only 3; no FAILED or NODE_FAIL status exists' |
| Fail-stop symptom: I/O failure (drive fails to perform read/write request) | SNIA-storage (ATC'22 Alibaba NVMe) | storage/IO | 49.55% of ticketed NVMe fail-stops; ARR contribution 0.40% | Table row citing ATC'22 Table 3 taxonomy AS NAMED: I/O, Link, Lost, Boot, Thres.; now dominant in NVMe vs SATA where 'Lost' dominated |
| Fail-stop symptom: Boot failure (drive fails to initiate/mount) | SNIA-storage (ATC'22 Alibaba NVMe) | storage/IO | 19.59% of ticketed NVMe fail-stops; ARR 0.16% | Table row: with I/O failure, main culprit of elevated ARR of the novel 'NEW' NAND architecture family (II-E) |
| Fail-stop symptom: Threshold (SMART attribute over pre-defined threshold) | SNIA-storage (ATC'22 Alibaba NVMe) | storage/IO | 14.15% of ticketed fail-stops; ARR 0.11% | Table row citing ATC'22 Table 3 |
| Fail-stop symptom: Link failure (PCIe connection error / abnormal bandwidth) | SNIA-storage (ATC'22 Alibaba NVMe) | storage/IO | 11.07% of ticketed fail-stops; ARR 0.09% | Table row citing ATC'22 Table 3 |
| Fail-stop symptom: Lost (functioning drive becomes unfound) | SNIA-storage (ATC'22 Alibaba NVMe) | storage/IO | 5.65% of ticketed fail-stops (vs 53.7% in SATA SSD) | Table row: 'biggest taxonomy shift from SATA to NVMe' |
| Fail-slow (gray failure): drive functioning but >=2x slower than intra-node peers | SNIA-storage (ATC'22/Perseus FAST'23) | storage/IO | 1.41% of NVMe SSDs in 4 months (5-min definition), 6.05x the HDD rate (0.20%); 0.52% vs 0.01% at 60-min definition (51x); 48.0 vs 2.45 events/1K drives/hour | Table row: ATC'22 Finding 4; fail-slow NVMe degrades to SATA-SSD-level latency; does NOT correlate with SMART (Finding 9) |
| Fail-slow -> fail-stop transition | SNIA-storage (ATC'22 Alibaba NVMe) | storage/IO | only 0.22% of fail-slow drives (10/4584) later failed; mean transition 73 days | Row detail (Finding 10) and headline: 'fail-slow->fail-stop transition only 0.22% of fail-slow drives (mean 73 days)' |
| Fail-slow root cause: ill-implemented software scheduling | SNIA-storage (Perseus FAST'23) | software | 252/315 verified fail-slow drives (80%): 216 SSDs + 36 HDDs | Table row citing Perseus FAST'23 Sec. 6; both cases fixed by scheduler/assignment changes, not hardware replacement |
| OS scheduler preempting CPU cores assigned to open-channel SSD FTL (software-scheduling Case 1) | SNIA-storage (Perseus FAST'23) | software | 216 SSDs (always disk1/disk2 slowest) | Row detail: 'Case 1: OS scheduler preempting CPU cores assigned to open-channel SSD FTL' |
| Thread_ID = Disk_ID mod #Drives collision, two HDDs sharing one I/O thread (software-scheduling Case 2) | SNIA-storage (Perseus FAST'23) | software | 36 HDDs | Row detail: 'Case 2: Thread_ID = Disk_ID mod #Drives collision after a drive goes offline' |
| Fail-slow root cause: hardware defects | SNIA-storage (Perseus FAST'23) | hardware | 63/315 verified fail-slow drives (20%): 21 SSDs + 42 HDDs | Table row: 'Fail-slow root cause: hardware defects' |
| Bad capacitors (DRAM-cache capacitors forcing direct-to-NAND ACK) | SNIA-storage (Perseus FAST'23 + ATC'22 RMA) | hardware | 4 SSDs of 15 vendor-diagnosed (Perseus); 33 of ATC'22's 100 slowest RMA'd SSDs | Row detail: 'bad capacitors 4 SSDs'; 'ATC'22 RMA'd its 100 slowest SSDs... 33 bad capacitors' |
| Stuck read-only mode (SSD) | SNIA-storage (Perseus FAST'23) | hardware | 2 SSDs of 15 vendor-diagnosed | Row detail: 'stuck read-only mode 2 SSDs' |
| Bad sectors (HDD) | SNIA-storage (Perseus FAST'23) | hardware | 3 HDDs of 15 vendor-diagnosed | Row detail: 'bad sectors 3 HDDs' |
| Rotor eccentricity (HDD) | SNIA-storage (Perseus FAST'23) | hardware | 2 HDDs of 15 vendor-diagnosed | Row detail: 'rotor eccentricity 2 HDDs' |
| Bad chips (RMA'd slow SSDs) | SNIA-storage (ATC'22 Alibaba NVMe) | hardware | 46 of 100 slowest RMA'd SSDs (avg event latency 4.4ms) | Row detail: 'ATC'22 RMA'd its 100 slowest SSDs...: 33 bad capacitors, 46 bad chips, 21 root cause unresolved' |
| Root cause unresolved (RMA'd slow SSDs) | SNIA-storage (ATC'22 Alibaba NVMe) | hardware | 21 of 100 slowest RMA'd SSDs | Row detail: '21 root cause unresolved' |
| Fail-slow root cause: environmental factors | SNIA-storage (Perseus FAST'23) | facility | 4 of 15 vendor-diagnosed drives | Table row citing Perseus FAST'23 Sec. 6.3 |
| Temperature throttling (HDD) | SNIA-storage (Perseus FAST'23) | facility | 1 HDD of the 4 environmental cases | Table row: 'temperature throttling 1 HDD' |
| Insufficient power supply (HDD) | SNIA-storage (Perseus FAST'23) | facility | 3 HDDs of the 4 environmental cases | Table row: 'insufficient power supply 3 HDDs' |
| Correlated failures: intra-node and intra-rack fail-stop clusters | SNIA-storage (FAST'21 + ATC'22) | storage/IO | SATA fleet: 12.9% of SSD failures intra-node, 18.3% intra-rack (30-min definition); 10.0%/14.4% within 1 minute; NVMe fleet: up to 14.69x (intra-node) / 1.78x (intra-rack) higher t | Table row citing FAST'21 Findings 1-3; failure group sizes reach 11 (node) / 89 (rack), exceeding Rep(2)/Rep(3) tolerance |
| Fail-stop overall rate (ARR/AFR) | SNIA-storage (ATC'22 + FAST'21 + PAKDD) | hardware | NVMe mean ARR 0.98%, median 0.69% (per-model 0.26-3.27%); SATA SSD AFR 1.16% overall (MLC 0.55%, 3D-TLC 3.29-3.92%); PAKDD HDD AFR 0.90% (A1) / 1.01% (A2) | Table row: 'Fail-stop overall rate (ARR/AFR)' citing ATC'22 Table 2/3 and FAST'21 Table 3; NVMe infant mortality NOT observed |
| WAF<=1 'rare-but-deadly' write-compression drive population | SNIA-storage (ATC'22 Alibaba NVMe) | hardware | WAF<=1 drives show 2.19x higher ARR, up to 6.18x in model III-B | Row detail (Finding 2): 'WAF<=1 drives show 2.19x higher ARR... rare-but-deadly write-compression population'; recovery notes: monitor/relocate rare WAF<=1 drives via simple SMART  |
| Coarse outcome labels only: PAKDD binary fail/healthy with fault_time (anonymized fault_tag) and DSN'21 ssd_smart_logs failure label (model, disk_id, fault time) | SNIA-storage (PAKDD 2020 + DSN'21) | storage/IO | no cause taxonomy — only failure occurrence labels from trouble tickets; best 30-day PAKDD prediction F1 = 0.4903 | Table row: 'Coarse outcome labels only (prediction datasets)'; caveats: 'these two datasets expose OUTCOME labels only, no failure-cause taxonomy' |
| S187 uncorrectable errors (SMART attribute, weak correlated-failure indicator) | SNIA-storage (FAST'21) | storage/IO | max SRCC 0.23 — best of the SMART attributes, still poor | Row detail: 'SMART attributes are poor indicators of correlated failures (max SRCC 0.23, S187 uncorrectable errors)' |
| Shared-component fault (e.g., HBA) slowing ALL drives in a node | SNIA-storage (Perseus FAST'23 caveat) | hardware | evades Perseus detection (peer comparison assumes fail-slow is rare) | Caveats prose: 'a shared component fault (e.g. HBA) slowing ALL drives in a node evades detection' |
| COMPLETED | AcmeTrace (Seren+Kalos) | scheduler job state |  | Slurm-style `state` field with values COMPLETED, CANCELLED, FAILED, TIMEOUT, NODE_FAIL |
| CANCELLED | AcmeTrace (Seren+Kalos) | scheduler job state |  | state field values COMPLETED, CANCELLED, FAILED, TIMEOUT, NODE_FAIL |
| FAILED | AcmeTrace (Seren+Kalos) | scheduler job state |  | state field values ... FAILED ... so failed vs. node-failed vs. timed-out jobs are distinguishable |
| TIMEOUT | AcmeTrace (Seren+Kalos) | scheduler job state | rare | docs note TIMEOUT/NODE_FAIL are rare and counted as failed |
| NODE_FAIL | AcmeTrace / Helios (HeliosData) | scheduler job state (infrastructure) | very rare | Helios: distinguishes application/user-job failure (FAILED) from infrastructure/hardware failure (NODE_FAIL) |
| OUT_OF_MEMORY | PM100 | scheduler job state |  | job_state — final Slurm job state enum (e.g., COMPLETED, FAILED, CANCELLED, TIMEOUT, NODE_FAIL, OUT_OF_MEMORY) |
| PREEMPTED | Revisiting Reliability (Meta RSC-1/RSC-2) | scheduler job state |  | maps to Slurm job-exit states (FAILED with non-zero exit code, NODE_FAIL, OUT_OF_MEMORY, TIMEOUT, PREEMPTED, REQUEUED, CANCELLED, COMPLETED) |
| REQUEUED | Revisiting Reliability (Meta RSC-1/RSC-2) | scheduler job state |  | Slurm job-exit states ... PREEMPTED, REQUEUED, CANCELLED, COMPLETED |
| fail_time / stop_time | AcmeTrace (Kalos) | scheduler trace field |  | Kalos additionally exposes a `fail_time` timestamp for when failure occurred |
| Infrastructure | Acme LLM cluster trace (paper Table 3) | root-cause class | dominant in pretraining | 3 top-level categories — Infrastructure, Framework, Script; Infrastructure = compute/storage hardware, mid-run, dominant in pretraining |
| Framework | Acme LLM cluster trace (paper Table 3) | root-cause class (software framework) |  | Framework (RuntimeError/ValueError/AttributeError tensor-op errors, early in run) |
| Script | Acme LLM cluster trace (paper Table 3) | root-cause class (user) | majority | Script (user/programming errors, the majority) |
| NVLinkError | Acme LLM cluster trace | infrastructure |  | Infrastructure = NVLinkError, CUDAError, NodeFailure, ECCError, NetworkError, Conne[...] |
| CUDAError | Acme LLM cluster trace | infrastructure |  | Infrastructure = NVLinkError, CUDAError, NodeFailure, ECCError, NetworkError |
| NodeFailure | Acme LLM cluster trace | infrastructure |  | Infrastructure = ... NodeFailure ... |
| ECCError | Acme LLM cluster trace | infrastructure |  | Infrastructure = ... ECCError ... |
| NetworkError | Acme LLM cluster trace | infrastructure |  | Infrastructure = ... NetworkError, Conne[...] (line truncated in file) |
| RuntimeError | AcmeTrace (Seren+Kalos) | framework/software |  | Framework (RuntimeError/ValueError/AttributeError tensor-op errors, early in run) |
| ValueError | AcmeTrace (Seren+Kalos) | framework/software |  | Framework (RuntimeError/ValueError/AttributeError tensor-op errors) |
| AttributeError | AcmeTrace (Seren+Kalos) | framework/software |  | Framework (RuntimeError/ValueError/AttributeError tensor-op errors) |
| NCCLRemoteError | AcmeTrace failure/RAS subset | infrastructure/comm |  | named root causes like CUDAError, ECCError, NVLinkError, NCCLRemoteError, S3StorageError, RuntimeError |
| S3StorageError | AcmeTrace failure/RAS subset | storage |  | named root causes like ... S3StorageError ... |
| Failed (status: Running/Terminated/Failed/Waiting) | Alibaba cluster-trace-gpu-v2020 | job/task/instance outcome |  | status field with values Running, Terminated, Failed, Waiting — only 'Terminated' means successful completion |
| Terminated (= successful completion) | Alibaba cluster-trace-gpu-v2020 | job/task/instance outcome |  | only 'Terminated' denotes successful completion and 'Failed' is an explicit failure label |
| Failed (Kubernetes pod phase) | Alibaba cluster-trace-gpu-v2023 | pod lifecycle |  | the Kubernetes pod phase field, which can be 'Failed' — an unqualified terminal state with no reason |
| Interrupted | Alibaba cluster-trace-v2017 | instance outcome |  | batch_instance status: Ready / Waiting / Running / Terminated / Failed / Cancelled / Interrupted |
| softerror | Alibaba cluster-trace-v2017 | machine event |  | server_event event type includes 'add', 'softerror' (temporary unavailability), and 'harderror' |
| harderror | Alibaba cluster-trace-v2017 | machine event (hardware) |  | 'harderror' (hardware failure) in server_event |
| NIC-ToR link failure | Alibaba HPN (SIGCOMM 2024) | network | ~0.057%/month | ~0.057% of NIC-ToR links fail per month |
| ToR switch critical error/crash | Alibaba HPN (SIGCOMM 2024) | network | ~0.051%/month | ~0.051% of ToR switches hit critical error/crash per month |
| Xid 74 (NVLink errors) | Fire-Flyer 2 AI-HPC (DeepSeek) | GPU hardware (Xid) | 42.57% | Xid 74 (NVLink errors) = 42.57%, attributed to NVLink Bridge connector fault rate |
| Xid 43 (illegal/out-of-bounds memory access) | Fire-Flyer 2 AI-HPC (DeepSeek) | software/user-code (Xid) | 33.48% | Xid 43 (illegal/out-of-bounds memory access, software/user-code) = 33.48% |
| Xid 13/31/43/45 (software errors group) | Fire-Flyer 2 AI-HPC (DeepSeek) | software (Xid) |  | software-related codes Xid 13/31/43/45 grouped as software errors |
| Xid 63/64/94/95 (GPU memory ECC: row-remap failure, contained/uncontained ECC) | Fire-Flyer 2 AI-HPC (DeepSeek) | GPU memory hardware (Xid) | ≈2% | GPU memory ECC codes Xid 63/64/94/95 (row-remap failure, contained/uncontained ECC) ≈ 2% |
| XID 79 GPU card dropout | From Detection to Recovery (504 GPUs) | GPU hardware (Xid) | 2 of 10 XID GPU failures | XID 79 GPU card dropout (2) |
| XID 94 ECC error | From Detection to Recovery (504 GPUs) | GPU memory (Xid) | 3 of 10 | XID 94 ECC error (3); ECC root-cause narrative = NFS GETATTR surge |
| XID 145/149 NVLink errors | From Detection to Recovery (504 GPUs) | GPU interconnect (Xid) | 6 of 10 | XID 145/149 NVLink errors (6) |
| XID 119 GSP RPC timeout | From Detection to Recovery (504 GPUs) | GPU firmware (Xid) | 1 of 10 | XID 119 GSP RPC timeout (1) |
| NVLink errors (Minder taxonomy) | From Detection to Recovery / ByteDance Minder | hardware category | 29.4% | categorized against ByteDance Minder's taxonomy ... with per-category percentages (e.g. NVLink 29.4%) |
| ECC errors (Minder taxonomy) | From Detection to Recovery / ByteDance Minder | hardware category |  | Minder's taxonomy (NVLink errors, ECC errors, GPU card dropout, GPU execution errors, machine unreachable, performance degradation) |
| GPU execution errors | From Detection to Recovery / ByteDance Minder | GPU |  | Minder taxonomy category: GPU execution errors |
| machine unreachable | From Detection to Recovery / ByteDance Minder | node/network |  | Minder taxonomy category: machine unreachable |
| performance degradation | From Detection to Recovery / ByteDance Minder | gray failure |  | Minder taxonomy category: performance degradation |
| Xid 31 (MMU error) | Story of Two GPUs (Delta H100/A100 artifact) | GPU (Xid) |  | categorizes GPU ERROR TYPE via NVIDIA Xid codes: Xid 31 (MMU error), 48 (double-bit ECC/DBE)... |
| Xid 48 (double-bit ECC/DBE) | Story of Two GPUs (Delta artifact) | GPU memory (Xid) |  | Xid 48 (double-bit ECC/DBE) in the regex-parsed Xid list |
| Xid 63/64 (row-remap event/failure) | Story of Two GPUs (Delta artifact) | GPU memory (Xid) |  | 63/64 (row-remap event/failure) |
| Xid 79 (GPU fallen off bus) | Story of Two GPUs (Delta artifact) | GPU/PCIe (Xid) |  | 79 (GPU fallen off bus) |
| Xid 94/95 (contained/uncontained memory error) | Story of Two GPUs (Delta artifact) | GPU memory (Xid) |  | 94/95 (contained/uncontained memory error) |
| Xid 119/120 (GSP error) | Story of Two GPUs (Delta artifact) | GPU firmware (Xid) |  | 119/120 (GSP error) |
| Xid 122/123 (PMU SPI error) | Story of Two GPUs (Delta artifact) | GPU firmware (Xid) |  | 122/123 (PMU SPI error) |
| GPU-Failed (derived job label) | Story of Two GPUs (Delta artifact) | derived job label |  | a job is tagged GPU-failed when a Xid error occurred within a ~20-second window before job termination |
| faulty GPU | Llama 3 405B Table 5 | hardware component | of 419 interruptions | each of the 419 unexpected interruptions is bucketed by failing hardware component (faulty GPU, HBM3, SRAM, GPU processor, network switch/cable, CPU, SDC, host maintenance, etc.) |
| HBM3 | Llama 3 405B Table 5 | GPU memory hardware |  | bucketed by failing hardware component ... HBM3 ... |
| SRAM | Llama 3 405B Table 5 | hardware |  | bucketed by failing hardware component ... SRAM ... |
| GPU system processor | Llama 3 405B Reliability Breakdown | GPU hardware |  | failure LABELS by category (faulty GPU, HBM3, SRAM, GPU system processor, NIC/network switch/cable, CPU, host maintenance, software bug, silent data corruption) |
| NIC/network switch/cable | Llama 3 405B Reliability Breakdown | network hardware |  | category list includes NIC/network switch/cable |
| CPU | Llama 3 405B Table 5 | hardware |  | bucketed by failing hardware component ... CPU ... |
| silent data corruption (SDC) | Llama 3 405B Table 5 | hardware (silent) |  | components include ... SDC ...; also distinguishes confirmed-hardware vs suspected-hardware |
| host maintenance | Llama 3 405B Table 5 | operational |  | categories include host maintenance; distinguishes planned vs unexpected interruptions |
| software bug | Llama 3 405B Reliability Breakdown | software |  | categories ... software bug, silent data corruption |
| explicit failures | MegaScale / ByteRobust | taxonomy tier |  | (1) explicit failures — detected via error messages, logs, or exit codes (e.g., CUDA errors, ECC/GPU faults) |
| implicit/gray failures | MegaScale / ByteRobust | taxonomy tier |  | (2) implicit/gray failures — hangs, throughput degradation, anomalous loss with no error thrown |
| manual restarts | MegaScale / ByteRobust | operational |  | (3) manual restarts — third incident class in ByteRobust's split |
| RNIC/RDMA bandwidth degradation | MegaScale (NSDI'24) | network | 'over 100' recovery events total | names failure CATEGORIES it detects/recovers from (RNIC/RDMA bandwidth degradation, link flapping, PCIe config issues, ...) |
| link flapping | MegaScale (NSDI'24) | network |  | failure categories ... link flapping ... |
| PCIe config issues | MegaScale (NSDI'24) | hardware/config |  | failure categories ... PCIe config issues ... |
| GPU NCCL all-to-all/all-reduce test failures | MegaScale (NSDI'24) | comm/health-check |  | failure categories ... GPU NCCL all-to-all/all-reduce test failures ... |
| segmentation faults | MegaScale (NSDI'24) | software |  | failure categories ... CUDA errors, segmentation faults, ECC/hardware faults |
| performance stragglers | MegaScale (NSDI'24) | gray failure | ~10% slower | performance stragglers ~10% slower / MFU decline |
| user program errors (OOM in user code) | Revisiting Reliability (Meta RSC-1/RSC-2) | taxonomy tier (user) |  | three-tier failure taxonomy: (1) user program errors (e.g., OOM in user code), (2) system-software faults, (3) hardware failures |
| system-software faults (drivers, filesystem, cluster services) | Revisiting Reliability (Meta RSC-1/RSC-2) | taxonomy tier (system software) |  | System Software domain: GPU driver/firmware, OS, PyTorch, filesystem mounts, NCCL timeouts, system services |
| hardware failures (GPUs, network, memory) | Revisiting Reliability (Meta RSC-1/RSC-2) | taxonomy tier (hardware) |  | Hardware Infrastructure: GPU unavailable, GPU memory/ECC errors, NVLink errors, PCIe errors, InfiniBand/Ethernet link errors, main-memory errors |
| NCCL timeouts | Revisiting Reliability (Meta RSC-1/RSC-2) | system software/comm |  | System Software domain list includes NCCL timeouts |
| GPU XID events (node health checks) | Meta ML Research Cluster Reliability Data | health-check signal |  | uses periodic node health checks (GPU XID events, mount/service checks) as fault signals |
| GPU unavailable | Revisiting Reliability (Meta RSC-1/RSC-2) | hardware |  | Hardware Infrastructure list: GPU unavailable, GPU memory/ECC errors ... |
| PCIe errors | Revisiting Reliability (Meta RSC-1/RSC-2) | hardware |  | Hardware Infrastructure list includes PCIe errors |
| InfiniBand/Ethernet link errors | Revisiting Reliability (Meta RSC-1/RSC-2) | network hardware |  | Hardware Infrastructure list includes InfiniBand/Ethernet link errors |
| main-memory errors | Revisiting Reliability (Meta RSC-1/RSC-2) | hardware |  | Hardware Infrastructure list includes main-memory errors |
| Pass | Microsoft Philly Trace | job outcome |  | status field with exactly one of Pass, Killed, or Failed |
| Killed | Microsoft Philly Trace | job outcome |  | status field with exactly one of Pass, Killed, or Failed |
| Failed (Philly status) | Microsoft Philly Trace | job outcome |  | status field ... Pass, Killed, or Failed; retries visible as repeated attempts |
| 20 failure categories across 4 dimensions (e.g., GPU/CPU out-of-memory, syntax/semantic errors, runtime) | Philly Trace (Jeon et al. ATC'19 / ICSE'20) | paper taxonomy (infrastructure/AI-engine/user layers) | 4,960 failed jobs | 4,960 failed jobs classified into 20 failure categories across 4 dimensions ... root causes manually analyzed for ~400 |
| uncorrectable ECC error | NVIDIA DGX Cloud (Nemotron) | GPU memory hardware | ~38.9% | Failure classes named include: uncorrectable ECC error ... ECC ~38.9% |
| GPU falling off the bus | NVIDIA DGX Cloud (Nemotron) | GPU/PCIe hardware |  | failure classes ... GPU falling off the bus ... |
| UB (unhealthy/bus) timeout | NVIDIA DGX Cloud (Nemotron) | hardware/bus |  | failure classes ... UB (unhealthy/bus) timeout ... |
| PCIe-related faults | NVIDIA DGX Cloud (Nemotron) | hardware | ~6.6% | PCIe ~6.6% ... of failures (blog figure) |
| NIC/network error (reported by NCCL) | NVIDIA DGX Cloud (Nemotron) | network | ~5.7% | NIC/network error (reported by NCCL) ... NIC ~5.7% |
| NCCL system error | NVIDIA DGX Cloud (Nemotron) | comm library |  | failure classes ... NCCL system error ... |
| unhandled CUDA error | NVIDIA DGX Cloud (Nemotron) | software/GPU |  | failure classes ... unhandled CUDA error, illegal memory access ... |
| illegal memory access | NVIDIA DGX Cloud (Nemotron) | software/GPU |  | failure classes ... illegal memory access ... |
| node failure (reported by Slurm) | NVIDIA DGX Cloud (Nemotron) | node/scheduler |  | failure classes ... node failure (reported by Slurm) ... |
| bus error (root-caused to slow filesystem) | NVIDIA DGX Cloud (Nemotron) | storage-induced |  | bus error (root-caused to slow filesystem) |
| NaN in gradients | NVIDIA DGX Cloud (Nemotron) | training/numerical |  | failure classes ... and NaN in gradients |
| loss divergences / NaN/underflow | OPT-175B Training Logbook | training/numerical (narrative) | ~90-110 interruptions total | loss divergences / numerical-instability spikes, NaN/underflow named in prose; ~35 manual + 70+ automatic restarts |
| hardware failures (dead/faulty GPUs, ECC errors, nodes failing health/infra checks) | OPT-175B Training Logbook | hardware (narrative) | ~110 hardware failures | hardware failures (dead/faulty GPUs, ECC errors, nodes failing health/infra checks, machines going down ~daily); 100+ hosts cycled out |
| SBE (single-bit error, correctable) | Nie et al. HPCA 2016 / Titan GPU field data | GPU ECC hardware |  | error-TYPE-labeled count: SBE (single-bit, correctable — do not crash jobs) vs DBE |
| DBE (double-bit error, uncorrectable) | Titan GPU Failure/Lifetime Data (ORNL) | GPU ECC hardware | ~86% memory, rest register file (per TitanGPULife) | DBE = Double-Bit Error (an uncorrectable ECC memory error); dead_dbe status column |
| OTB (Off-The-Bus) | Titan GPU Failure/Lifetime Data (ORNL) | GPU/PCIe hardware |  | OTB = 'Off-The-Bus' (loss of the host CPU's PCIe connection to the GPU); dead_otb indicator |
| dead / dead_dbe / dead_otb / out | GPU Lifetimes on Titan (TitanGPULife) | survival-analysis event labels |  | Per-GPU death indicators are provided (dead, dead_otb, dead_dbe) plus catch-all 'out' for other terminations |
| illegal address access | Experimental Findings on Sources of DUEs in GPUs | GPU DUE source class | ECC cuts illegal-address DUEs ~92% Kepler / ~98% Volta | Every DUE is attributed to a source: illegal address access, interface (bus/link) error, or kernel launch failure |
| interface (bus/link) error | Experimental Findings on Sources of DUEs in GPUs | GPU DUE source class |  | DUE sources: illegal address access, interface (bus/link) error, kernel launch failure |
| kernel launch failure | Experimental Findings on Sources of DUEs in GPUs | GPU DUE source class |  | DUE sources ... kernel launch failure |
| DBE event vs normal-operation snapshot | OLCF Summit GPU Snapshots | GPU hardware label |  | Each record is tagged as either a DBE (double-bit/uncorrectable memory-corruption) event or a normal-operation snapshot; exposes NVIDIA XID codes, node reboot logs, job-scheduler t |
| DEBUG/TRACE/INFO/WARNING/ERROR/FATAL severity | Blue Gene/P Intrepid RAS + Job Logs | RAS severity | 33,370 FATAL of 2.08M | Failures are labeled via the SEVERITY field: DEBUG, TRACE, INFO, WARNING, ERROR, FATAL (only INFO/WARNING/ERROR/FATAL appear); FATAL = 33,370 records, 549 after dedup |
| ERRCODE (e.g. DetectedClockCardErrors) | Blue Gene/P Intrepid RAS | RAS error code | 82 types | ERRCODE gives fine-grained fault type (e.g. 'DetectedClockCardErrors'), spanning 82 ERRCODE types across 6 components among FATAL events |
| CATEGORY + COMPONENT + MSG_ID (hardware, software, coolant/environment, network) | Blue Gene/Q Mira RAS Logs (LogAider) | RAS category |  | typed by CATEGORY + COMPONENT + MSG_ID, which map to IBM BG/Q RAS message classes (hardware component, software, coolant/environment, network); CTLACTION records automated response |
| RAS_EVENT CATEGORY (compute card, DDR memory, link, PCI, Ethernet, InfiniBand, power module, coolant, Software_Error, ELF_Image, Job, Proc...) | ALCF Public Data reports (Mira RAS_EVENT) | RAS category |  | CATEGORY (the entity that hit the error: compute card, DDR memory, link, PCI, Ethernet, InfiniBand, power module, coolant, Software_Error, ELF_Image, Job, Proc...) with SEVERITY FA |
| THETA_HARDWARE_ERROR | ALCF Public Data Catalog (IEEE DataPort) | hardware error log table |  | failure-relevant tables (THETA_HARDWARE_ERROR hardware error logs, RAS_EVENT, DIM_MACHINE_STATUS node health) |
| KERNDTLB | Loghub BGL / HPC4 Oliner-Stearley | alert category (kernel/DTLB) |  | BGL categories such as KERNDTLB, APPREAD, KERNMC memory/DTLB/machine-check tags |
| APPREAD | HPC4 / Oliner-Stearley DSN'07 (BGL) | alert category (application) |  | alert-category tags e.g. KERNDTLB, APPREAD, KERNMC |
| KERNMC | HPC4 / Oliner-Stearley DSN'07 (BGL) | alert category (machine check) |  | KERNMC machine-check tag |
| APPSEV | Loghub HPC RAS collection (BGL) | alert category |  | human-curated alert category CODES (e.g., KERNDTLB, APPSEV, KERNMNTF, KERNTERM) |
| KERNMNTF | Loghub HPC RAS collection (BGL) | alert category |  | alert codes ... KERNMNTF ... |
| KERNTERM | Loghub HPC RAS collection (BGL) | alert category |  | alert codes ... KERNTERM ... |
| R_HDW_BAD | Loghub Sandia/LLNL logs (Thunderbird/Spirit/Liberty) | alert category (hardware) | BGL: ~348,460 alert lines of 4.75M ≈ 7.3% | alert-category tag (e.g. KERNELDTLB, KERNMC, APPREAD, R_HDW_BAD) |
| '-' non-alert vs alert tag | Loghub / HPC4 alert-annotated logs | binary alert label |  | the first column is an alert-category tag: '-' marks a non-alert (benign) message; any other value marks an alert |
| Hardware | LANL failure data (22 systems, 1996-2005) | root-cause category | ~53% | HIGH-LEVEL category (one of six: Hardware, Software, Network, Environment, Human, plus Unknown); ~53% Hardware |
| Software | LANL failure data (22 systems) | root-cause category | ~22% | ~22% Software of admin-attended node outages |
| Network | LANL failure data (22 systems) | root-cause category |  | categories Hardware, Software, Network, Environment, Human, Unknown |
| Environment (power/AC) | LANL failure data / CFDR | root-cause category |  | Environment (power/AC) among the five high-level classes |
| Human error | LANL failure data / CFDR | root-cause category |  | five high-level classes — Hardware, Software, Network, Environment, and Human error |
| Undetermined/Unknown | LANL failure data (22 systems) | root-cause category | significant | plus Unknown/Undetermined in practice; Unknown share is significant |
| Cooling Fan (sub-cause under Hardware) | LANL failure data (22 systems) | root-cause sub-category |  | a DETAILED sub-cause (e.g. 'Cooling Fan' under Hardware, 'OS Software' under Software) |
| OS Software (sub-cause under Software) | LANL failure data (22 systems) | root-cause sub-category |  | sub-cause 'OS Software' under Software |
| internal failures (application bugs, node system/kernel bugs, node hardware) | Desh/Doomsday Cray XC corpus | derived node-failure bucket |  | bucketed (Table III) into internal failures (application bugs, node system/kernel bugs, node hardware), external failures, and normal shutdowns |
| external failures (blade/cabinet controller, filesystem/network-server, router/other hardware) | Desh/Doomsday Cray XC corpus | derived node-failure bucket |  | external failures (blade/cabinet controller, filesystem/network-server, router/other hardware) |
| normal shutdowns (bulk/maintenance/periodic reboots) | Desh/Doomsday Cray XC corpus | derived bucket (non-failure) |  | normal shutdowns (bulk/maintenance/periodic reboots) — excluded as non-anomalies |
| system-caused vs user-caused application failures | Blue Waters LogDiver (NCSA) | attribution split | ~1.53% system-caused | ~1.53% of applications failed due to system-related issues; XK (GPU) applications more failure-prone than XE |
| failed component + repair action | PNNL MPP2 Hardware Failure Log (CFDR) | hardware maintenance record |  | explicit 'failed component' field plus free-text description and 'repair action' field (disk, memory, NIC, node board replaced/reseated) |
| repair code naming the failed part (disks, memory, motherboards) | COM2 (CFDR warranty log) | hardware replacement |  | hardware failure/replacement event tagged with a repair code that names the failed part (disks, memory, motherboards, etc.) |
| failure symptom / diagnosis / repair narrative | COM1 (CFDR) | hardware repair record (free text) |  | human-recorded failure SYMPTOMS plus the diagnostic and repair steps taken |
| disk replacement event | HPC1/HPC2/HPC3 (CFDR) | disk hardware |  | labels hardware REPLACEMENTS ... 'replacement' does NOT necessarily mean an actual disk failure (no-trouble-found returns included) |
| failure column (0/1, last operational day) | Backblaze Drive Stats (SMART) | disk binary label + SMART attributes |  | `failure` column is 0 on every normal day and set to 1 on the LAST day the drive was operational before removal; raw SMART attributes are the only cause signal |
| power outage / switch failure / global-FS failure / drive failure | NERSC I/O Failure Database (CFDR Remedy tickets) | trouble-ticket cause |  | qualitative root-cause information (power outage, switch failure, global-FS failure, drive failure, etc.) with affected subsystem (storage/network/compute/FS) |
| node internal disk failure | USRC System 20 (MX20) | disk hardware | 14 records | 'System 20 Node Internal Disk Failure Info' (LA-UR-06-6079, 14 records) labels internal disk failure on a node |
| SWF Status (0=failed, 1=completed, 5=cancelled, 2-4 partial/checkpointed, -1 unknown) | Parallel Workloads Archive / Grid Workloads Archive | job outcome code |  | SWF field 11 (Status): 0 = job failed, 1 = completed successfully, 5 = cancelled; 2-4 partial/checkpoint, -1 unknown |
| EVICT | Google Borg trace 2011/2019 | task/job event type (2) |  | EVICT (descheduled — preemption by higher priority, OOM eviction, machine going away/overcommit, disk failure) |
| FAIL | Google Borg trace 2011/2019 | task/job event type |  | FAIL (task/job died due to a task/machine failure), event type 3 |
| KILL | Google Borg trace 2011/2019 | task/job event type |  | KILL (stopped by user/driver/dependent job), event type 5 |
| LOST | Google Borg trace 2011/2019 | task/job event type |  | LOST (record missing — outcome uncertain), event type 6 |
| FINISH | Google Borg trace 2011/2019 | task/job event type |  | FINISH = normal completion, event type 4 |
| machine REMOVE/ADD/UPDATE | Google Borg trace 2011 | machine event |  | machine_events carries ADD(0)/REMOVE(1)/UPDATE(2), where REMOVE marks a machine going out of service (failure or decommission) |
| Completed / Cancelled / Timeout | LANL Mustang trace (ATLAS) | scheduler job outcome |  | job_status has only THREE terminal values: Completed, Cancelled, Timeout — NO distinct FAILED or NODE_FAIL status |
| JOBSTART / JOBEND / JOBFAIL / JOBCANCEL | LANL Trinity trace (ATLAS) | scheduler event |  | object_event field distinguishes JOBSTART / JOBEND / JOBFAIL / JOBCANCEL |
| job_event_state (Completed, Running, Vacated, Hold) | LANL Trinity trace (ATLAS) | scheduler state |  | job_event_state records terminal states (Completed, Running, Vacated, Hold) |
| completion_code (UNIX errno-style, e.g. 12 = ENOMEM) | LANL Trinity trace (ATLAS) | exit/errno code |  | completion_code field carries a UNIX errno-style reason for failed jobs (e.g. '12' = ENOMEM / out of memory) |
| EXIT_STATUS / EXIT_CODE (DIM_JOB_COMPOSITE) | ALCF Public Data (Polaris/Theta/Mira job logs) | scheduler exit code |  | DIM_JOB_COMPOSITE exposes EXIT_STATUS (Unix process exit status) and EXIT_CODE (Unix exit code of the job executable); Polaris = PBS-reported exit status |
| Cobalt job states (exited, killed, dep_fail) | Theta job + Darshan I/O logs (ALCF) | Cobalt scheduler state |  | Cobalt job states distinguish outcomes (e.g., exited, killed, dep_fail) |
| Timeout / Bug (SIGABRT/SIGSEGV) / Kill (SIGKILL) / IO / RAS / SIGILL-SIGTRAP-SIGFPE | Mira 2K-day Multi-Source Job Failure Logs (DSN'19) | derived job-failure taxonomy |  | derived job-failure taxonomy joining Cobalt exit status with task-execution signals: Timeout, Bug (SIGABRT/SIGSEGV), Kill (SIGKILL/signal 9), IO (I/O-node/file failures), RAS (jobs |
| exit_signal + err_text | Mira 2K-day Multi-Source Job Failure Logs | task-execution log fields |  | POSIX-style exit_signal values plus human-readable err_text describing the fault (signal 9/11/etc. with the failing MPI rank) |
| ec exit code [0-255] + exit state (completed/failed) | F-DATA (Fugaku) | scheduler exit code |  | exit code `ec` in [0-255] straight from the scheduler; derived `exit state` = completed (0) or failed (non-zero) |
| TORQUE 'E' (job exited) record + exit-status/exit-code fields | FRESCO (Conte/Stampede) | PBS/TORQUE accounting |  | job-status record marker ('E' = job exited, successfully or not) and TORQUE exit-status/exit-code fields; Anvil v3 exposes Slurm exit codes and states |
| state_reason (Slurm job_state_reason enum) | PM100 | scheduler reason code |  | state_reason — Slurm job_state_reason enum giving the reason a job is pending or failed (partial root-cause signal) |
| derived_ec (highest exit code across job steps) | PM100 | exit code |  | derived_ec — highest exit code across all job steps (exposes exit codes) |
| ExitCode + State (sacct) | MIT Supercloud | scheduler accounting |  | slurm-log.csv carries standard sacct fields, including an ExitCode column and a job State column (COMPLETED, FAILED, CANCELLED, TIMEOUT, NODE_FAIL, OUT_OF_MEMORY) |
| successful vs failed (scheduler termination status) | Tachyon (KISTI Tachyon-II) | scheduler job outcome |  | jobs classed as successful vs. failed from the terminal state (analogous to Slurm COMPLETED vs FAILED/CANCELLED) |
| cpuoccupy | HPAS-injected datasets (E2EWatch / Sandia Eclipse / ALBADross / Proctor) | injected performance anomaly |  | Label set = {normal, cpuoccupy (CPU-intensive/contention), cachecopy, membw, memleak} |
| cachecopy | HPAS-injected datasets (E2EWatch / Sandia Eclipse) | injected performance anomaly |  | cachecopy (cache/L3 contention) among injected anomaly classes |
| dcopy | ALBADross Eclipse dataset | injected performance anomaly |  | HPAS tools seen in results: cpuoccupy, cachecopy/dcopy = cache contention, membw, memleak, dial |
| membw | HPAS-injected datasets (E2EWatch / Sandia Eclipse) | injected performance anomaly |  | membw (memory-bandwidth contention), injection configs documented (e.g. -s 4K/8K/32K) |
| memleak | HPAS-injected datasets (Prodigy / E2EWatch / Sandia Eclipse) | injected performance anomaly |  | Prodigy: single fault type 'memleak' (memory leak, injected via HPAS); binary_anom 0/1 |
| memeater | Proctor/Voltrino + Antarex (FINJ) | injected fault program |  | memleak / memeater (memory exhaustion/leak) among injected classes; also a FINJ fault program |
| netoccupy | Proctor / Voltrino Performance Anomaly Dataset | injected performance anomaly |  | netoccupy (network contention) plus a healthy/anomaly-free baseline class |
| dial | Antarex HPC Fault Dataset (FINJ) / ALBADross | injected fault program (ALU/arithmetic interference) |  | named fault programs: leak, memeater, ddot, dial, cpufreq, pagefail ... ioerr, copy |
| leak | Antarex HPC Fault Dataset (FINJ) | injected fault program |  | fault programs: leak, memeater, ddot, dial, cpufreq, pagefail (CPU/memory) and ioerr, copy (HDD) |
| ddot | Antarex HPC Fault Dataset (FINJ) | injected fault program |  | fault programs ... ddot ... |
| cpufreq | Antarex HPC Fault Dataset (FINJ) | injected fault program (misconfiguration) |  | fault programs ... cpufreq ... |
| pagefail | Antarex HPC Fault Dataset (FINJ) | injected fault program |  | fault programs ... pagefail (CPU/memory blocks) |
| ioerr | Antarex HPC Fault Dataset (FINJ) | injected fault program (I/O) |  | ioerr, copy (HDD blocks) — spanning hardware faults, misconfiguration, and performance anomalies |
| copy (HDD) | Antarex HPC Fault Dataset (FINJ) | injected fault program (I/O) |  | fault programs ... ioerr, copy (HDD blocks) |
| binary_anom (0 = healthy, 1 = anomalous) | Prodigy Eclipse Dataset | binary anomaly label | 80 of 160 anomalous | a single `binary_anom` column (0 = healthy, 1 = anomalous); 80/80 of 160 samples |
| Nagios anomaly label (normal vs anomalous: node down/unresponsive/maintenance) | M100 time-aggregated dataset | node health (Nagios) |  | label column of ANOMALY LABELS DERIVED FROM NAGIOS ... node down, unresponsive, or under maintenance, per 15-min window |
| Label (binary node failure, from CINECA Nagios) | ExaMon / Marconi snapshot | node health (Nagios) |  | binary 'Label' column marking presence/absence of a failure on the node, derived from the CINECA Nagios monitoring service |
| Nagios node offline/unavailable state | M100 ExaData (Marconi100) | node availability |  | what survives is essentially a node available/unavailable (offline) state signal, not a typed fault with cause |
| availability vs unavailability intervals | Failure Trace Archive (FTA) | resource availability |  | models failure as availability vs unavailability (up/down) intervals of nodes/components; unavailability conflates crash, reboot, partition, maintenance, churn |
| event reason codes: 'disk crash', 'CPU overheating' | FTA (schema; populated in lanl05) | component fault reason |  | the FTA schema supports 'event reason codes' (examples: disk crash, CPU overheating); lanl05 'contains a record for every failure ...' |
| event_type component codes (CPU, memory, hard disk) | Failure Trace Archive (FTA) | component attribution |  | the FORMAT can carry richer labels via event_type codes (which component: CPU, memory, hard disk) |
| free-text failure description + critical log-entry annotation | Cray XT logs (syslog/event/console) | vendor-diagnosed narrative |  | each dump ships a dedicated failure log with a description of the failure(s) plus annotation of WHICH log entry was critical in identifying the error |
| Cray severity flags (critical/warning; netwatch, pcimon) | Desh/Doomsday Cray XC corpus | RAS severity flag |  | logs contain Cray severity flags (critical/warning, e.g. netwatch, pcimon), but authors reject flag-based classification as unreliable |
| hardware root-cause job failure (~37%) | Unicron (Alibaba) | hardware | ~37% of failures; 43.4% job-failure rate | aggregate root-cause stats — 43.4% job-failure rate, ~37% hardware, ~73% restart-remediable |
| restart-remediable failure | Unicron (Alibaba) |  | ~73% | ~73% restart-remediable |
| XID-classified GPU failure | From Detection to Recovery (504x B200) | GPU hardware | 10 instances | 10 XID-classified GPU failures with precursor analysis, node-exclusion patterns |
| checkpoint-I/O event | From Detection to Recovery (504x B200) | I/O | 523 events | 523 checkpoint-I/O events |
| defective node (flagged defective) | SuperBench (Microsoft Azure A100 fleet) | node hardware | 10.36% of nodes | defect-node rate (10.36% flagged defective) |
| gray failure / degradation | SuperBench (Microsoft Azure A100 fleet) | hardware (partial/degraded) |  | gray-failure/degradation stats, MTBI gains |
| hardware root-cause LLM-training failure | L4 (Microsoft Platform-X) | hardware | dominant (of 428 failures) | root-cause distribution (hardware + user dominant) |
| user root-cause LLM-training failure | L4 (Microsoft Platform-X) | user/software | dominant (of 428 failures) | root-cause distribution (hardware + user dominant) |
| hardware-caused training interruption | Fault-Tolerant HSDP at 100,000 GPUs (Meta) | hardware | 78% of interruptions; 2.3 per 1,000 servers/day | 2.3 interruptions per 1,000 servers/day, 78% hardware-caused |
| runtime fault instance (faulty machine) | Minder (ByteDance) | machine/node | 150 instances / 9 months | 150 runtime fault instances over 9 months, up to ~10,000 Ampere GPUs |
| GPU hardware failure | BLOOM / BigScience training chronicles | GPU hardware | ~1–2 per week | dated narrative events (~1–2 GPU hardware failures/week ...) |
| dataloader deadlock | BLOOM / BigScience training chronicles | software |  | dataloader deadlock, disk-space outages, a loss spike |
| disk-space outage | BLOOM / BigScience training chronicles | storage |  | dataloader deadlock, disk-space outages, a loss spike |
| loss spike | BLOOM / BigScience training chronicles | training dynamics |  | dataloader deadlock, disk-space outages, a loss spike |
| hardware failure (dated) | GLM-130B training logs | hardware |  | dated hardware failures, NaN-loss/data issues, FP16 instabilities + interventions |
| NaN-loss / data issue | GLM-130B training logs | software/data |  | dated hardware failures, NaN-loss/data issues, FP16 instabilities |
| FP16 instability | GLM-130B training logs | numerics |  | FP16 instabilities + interventions |
| PCIe link-width degradation | Imbue 70B bare-metal report | hardware/interconnect | ~25% of hosts | PCIe link-width degradation on ~25% of hosts |
| ECC error | Imbue 70B bare-metal report | memory hardware |  | ECC/NVLink errors, firmware mismatches |
| NVLink error | Imbue 70B bare-metal report | GPU interconnect |  | ECC/NVLink errors, firmware mismatches |
| firmware mismatch | Imbue 70B bare-metal report | firmware |  | enumerated bring-up defects (... firmware mismatches) |
| loss-spike event (benign vs malignant) | LLM360 (Amber/CrystalCoder/K2) | training dynamics |  | loss-spike events (benign vs malignant, K2-Spike checkpoints) |
| fail-stop (TPU) | TPUv4 Resiliency at Scale (Google) | accelerator hardware |  | fail-stop + SDC handling at 10k-chip scale |
| SDC (TPU) | TPUv4 Resiliency at Scale (Google) | silent data corruption |  | fail-stop + SDC handling at 10k-chip scale |
| simulated precision-resilience fault | LLM-PRISM | SDC/numerics |  | precision resilience over 7,664 runs, simulated faults |
| SDC in LLM training | Exploring SDC as a Reliability Challenge in LLM Training | silent data corruption |  | public artifact at github.com/aaltenbernd/llm-sdc-training |
| gate-level GPU error pattern (SDC) | The Anatomy of SDC: GPU Error Pattern Study | GPU hardware / SDC |  | gate-level fault injection |
| mercurial-core SDC (CPU) | Silent Data Corruptions at Scale (Meta, Dixit 2021) | CPU silent data corruption |  | Mercurial-core SDC across 100k+ CPUs |
| CEE / mercurial core | Cores That Don't Count (Google) | CPU silent data corruption |  | CEE/mercurial-core taxonomy |
| production-CPU SDC | Understanding SDC in a Large Production CPU Population (Alibaba+Tsinghua) | CPU silent data corruption |  | SOSP 2023, >1M processors ... (The Alibaba SDC study) |
| vector-instruction SDC (vector-SDC suspect) | SEVI (ASPLOS) | CPU SIMD datapath | >2,500 suspects | >2,500 vector-SDC suspects ... hits the SIMD datapaths ML kernels use |
| DRAM correctable error (CE) | DRAM Errors in the Wild (Google) | DRAM |  | Canonical DRAM CE/UE baseline |
| DRAM uncorrectable error (UE) | DRAM Errors in the Wild (Google) | DRAM |  | Canonical DRAM CE/UE baseline |
| DDR3 fleet memory error | Revisiting Memory Errors in Large-Scale Production Data Centers (Facebook/Meza) | DRAM |  | Meza et al., DSN 2015, DDR3 fleet ... (The Meza DRAM study) |
| defective hardware (MI250X node-screening defect) | Detecting Defective Hardware in Exascale Supercomputers (Frontier, ORNL) | GPU/node hardware |  | Node-screening across 9,408 nodes / 37k+ MI250X. AMD-GPU exascale defect rates |
| GPU failure/repair (MTBF/MTTR) | Case Study with the Lassen Supercomputer (LLNL, V100) | GPU hardware |  | Sierra-class GPU failure/repair, MTBF/MTTR |
| cross-generation GPU failure/repair | Examining Failures and Repairs on Supercomputers (TSUBAME-2/3) | GPU hardware |  | Cross-generation GPU failure/repair trend |
| DRAM correctable-error logging jitter impact | Understanding the Effects of DRAM Correctable-Error Logging at Scale | DRAM/RAS logging |  | CE-logging/jitter impact (simulation) |
| per-job Slurm exit state (failure) | SURF Lisa | job/scheduler |  | per-job Slurm exit state, failure rates, energy wasted on failures |
| GPU thermal-limit event | SURF Lisa | GPU thermal |  | GPU thermal-limit events; explicitly splits ML vs generic jobs |
| FAILED (Slurm state) | NREL Eagle HPC Jobs | job/scheduler |  | Slurm exit states incl. FAILED, NODE_FAIL, CANCELLED, TIMEOUT, OUT_OF_MEMORY |
| NODE_FAIL (Slurm state) | NREL Eagle HPC Jobs (also Kestrel) | node/scheduler |  | Slurm exit states incl. ... NODE_FAIL; Kestrel: 'same Slurm state family incl. NODE_FAIL' |
| CANCELLED (Slurm state) | NREL Eagle HPC Jobs | job/scheduler |  | Slurm exit states incl. FAILED, NODE_FAIL, CANCELLED, TIMEOUT, OUT_OF_MEMORY |
| TIMEOUT (Slurm state) | NREL Eagle HPC Jobs | job/scheduler (walltime) |  | Slurm exit states incl. FAILED, NODE_FAIL, CANCELLED, TIMEOUT, OUT_OF_MEMORY |
| OUT_OF_MEMORY (Slurm state) | NREL Eagle HPC Jobs | job/memory |  | Slurm exit states incl. FAILED, NODE_FAIL, CANCELLED, TIMEOUT, OUT_OF_MEMORY |
| RAS/hardware-fault event | ALCF Cobalt workload + RAS traces (Intrepid/Mira) | machine/RAS |  | job termination info PLUS separate RAS/hardware-fault logs — a rare pairing |
| JOBEND (job_status) | Two Sigma cluster trace (CMU ATLAS) | job/scheduler |  | job_status field (JOBEND / JOBFAIL / JOBCANCEL) + wallclock_limit for timeout inference |
| JOBFAIL (job_status) | Two Sigma cluster trace (CMU ATLAS) | job/scheduler |  | job_status field (JOBEND / JOBFAIL / JOBCANCEL) |
| JOBCANCEL (job_status) | Two Sigma cluster trace (CMU ATLAS) | job/scheduler |  | job_status field (JOBEND / JOBFAIL / JOBCANCEL) |
| wallclock_limit timeout (inferred) | Two Sigma cluster trace (CMU ATLAS) | job/scheduler (walltime) |  | wallclock_limit for timeout inference |
| job state/exit field (Slurm) | DKRZ Mistral Slurm job-history dataset | job/scheduler |  | carries job state/exit fields — the failure-relevant Mistral dataset |
| fail-slow (degraded NVMe) | SNIA Reliability Traces: Alibaba NVMe | storage device (silent/degradation) |  | Fail-Slow (degraded NVMe, ~11 months) ... explicit fail-slow (degradation) ... events |
| fail-stop (complete SSD failure) | SNIA Reliability Traces: Alibaba NVMe | storage device (hard) |  | Fail-Stop (complete SSD failures, ~4 months) ... explicit ... fail-stop (hard) device events |
| SSD failure label via trouble ticket | Alibaba SSD SMART logs (dcbrain) | storage device |  | failure labels via trouble tickets aligned to SMART time series |
| correlated/cascading SSD failure (ticket + location) | Dataset of SSD Failures in Alibaba (Tianchi / FAST'21) | storage device |  | failure tickets + location/app context for correlated/cascading analysis |
| per-disk HDD failure label | Large-scale Disk Failure Prediction Dataset (Tianchi / PAKDD 2020) | storage device |  | per-disk failure labels (strongly class-imbalanced) |
| labeled device failure (reliability sub-collection) | SNIA IOTTA Trace Repository | storage device |  | the reliability section carries labeled device failures |
| THETA_HARDWARE_ERROR (+ exit codes + RAS) | IEEE DataPort ALCF Data Catalog | machine/RAS |  | Intrepid→Aurora with exit codes + THETA_HARDWARE_ERROR + RAS |