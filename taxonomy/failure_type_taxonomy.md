# Failure-Type Taxonomy — Every Type, Its Class, and the Rationale

**Built:** 2026-07-18. **Method:** 931 raw failure-type mentions enumerated exhaustively from the 37 extracted studies plus the failure-info fields of the ~157-dataset catalog, canonicalized into 88 canonical types across 11 classes. Every assignment carries a written rationale (the causal-locus argument) and a cause / symptom / outcome-label tag. Verified as part of the triple verification pass (see 09_verification_report.md). Full raw enumeration in 08a_raw_type_enumeration.md; machine-readable copies in heatmap/taxonomy.json and heatmap/enumerated_types.json.

## Why three kinds of 'failure type' must not be mixed

Every mention in the literature is one of: a **cause** (a component/actor that originated the fault), a **symptom** (an observable that can mask several causes — NCCL timeout, training hang), or an **outcome-label** (a scheduler terminal state — FAILED, TIMEOUT — carrying zero causal information). Roughly a third of all 931 mentions are outcome-labels. Filing them into cause classes is the single largest error source found in v1 of the heat map; they now live in their own row.

## The classes

### GPU/accelerator hardware
Faults whose causal locus is the accelerator package or its board: GPU/NPU/TPU silicon, device memory (HBM/SRAM/GDDR), on-package or intra-node accelerator interconnect (NVLink/NVLink Bridge/SXM), GPU-resident firmware processors (GSP, PMU), thermal interface/sensors, and board components (connectors, resistors).
**Boundary rules:** NVLink stays HERE, not network: its failure domain is one node/package and its repair action is GPU/board replacement (deciding rule: interconnect repaired by swapping the accelerator = accelerator; repaired by fabric ops = network). GPU DRIVER software goes to software/system. CUDA runtime errors are symptoms filed under software/system. GPU OOM and application-triggered Xids (13/31/43) go to user/application. GPU SDC goes to SDC/fail-slow with a back-pointer here.
**Changed from v1:** Unchanged in scope; boundary rules made explicit for NVLink and driver.

### CPU/host memory/PCIe
Host-side hardware: CPU, DIMM/DRAM (CE/UE/Chipkill), PCIe bus/links, motherboard/BIOS/chassis, BMC, and whole-node-level hardware failure where no finer component is identified.
**Boundary rules:** Host NIC goes to network/interconnect. Node PSU/fans go to power/facility. Mercurial-core/CPU SDC goes to SDC/fail-slow. Generic 'node failure/unreachable' is filed here but marked SYMPTOM (it masks any hardware cause). NODE_FAIL the scheduler state goes to outcome-label/meta.

### Network/interconnect
Inter-node fabric: IB/RoCE/Ethernet/Omni-Path/Gemini/torus links, switches, cables/optics/AOC, NICs/HCAs and their firmware, plus communication-layer symptoms (NCCL/MPI/TCP timeouts and resets) recorded as symptoms.
**Boundary rules:** NVLink and other intra-node accelerator links are excluded (GPU class). Comm-library BUGS (NCCL/MPI code defects) go to software/system; NCCL timeout is filed here only as a SYMPTOM row and must never be counted as a network root cause without diagnosis (Meta-RSC marks all three domains possible).

### Storage/filesystem
Storage devices (HDD/SSD/NVMe/tape), controllers/RAID/HBA, and filesystem software local and remote (Lustre, GPFS, NFS, HDFS, S3, XFS, ext4), including mounts, checkpoint I/O paths, and capacity exhaustion.
**Boundary rules:** Filesystem SOFTWARE counts here, not software/system (Lustre LBUG, XFS/ext4 bugs, NFS client) — the failure domain and remediation are storage-side. User path/permission mistakes go to user/application; corrupt input CONTENT goes to data/input; drive fail-SLOW manifestation goes to SDC/fail-slow with the device defect recorded here as cause.
**Changed from v1:** Explicitly absorbs FS software (was ambiguous between storage and software rows).

### Power/facility
Facility power (outages, fluctuations), cooling (A/C, rack air, node fans/heatsinks), node/bulk power supplies, environment, and unplanned host maintenance interruptions.
**Boundary rules:** Node PSUs and fans count here by convention (power/cooling function beats board location). GPU thermal THROTTLING from room/rack cooling is here; a faulty GPU thermal sensor/TIM is GPU class. PMU firmware errors are GPU class. Planned/normal maintenance reboots are non-failures (meta).
**Changed from v1:** Scope note added: includes node PSU/fan and unplanned maintenance.

### Software/system
System and platform software: OS kernel, GPU driver/firmware, system services/daemons, DL framework and comm-library bugs, VM layer, failover/HA logic, CUDA runtime errors (as symptoms).
**Boundary rules:** Scheduler/RM software goes to scheduler/resource-mgmt. Filesystem software goes to storage. User code and user-triggered exceptions go to user/application. Firmware sits here when the defect is code-fixable (Mira FIRMWARE, Xid 38) with hardware as the ambiguity alternative.

### User/application
Faults originating in user code, configuration, environment setup, resource sizing, or operator action: script errors, version mismatches, missing files/permissions, OOM within the requested allocation, application-triggered GPU faults, algorithmic divergence, human/operator error.
**Boundary rules:** Framework-internal bugs go to software/system. Input CONTENT problems go to data/input (rule: wrong path/format handling = user; corrupt/malformed bytes = data). OOM from node overcommit or a system leak = software or scheduler, not user. Scheduler terminal states (FAILED/TIMEOUT/CANCELLED) do NOT belong here — they are outcome-labels (meta).
**Changed from v1:** Narrowed: no longer the dump bucket for FAILED/TIMEOUT/CANCELLED trace states, which move to the new meta class.

### Data/input
Failures caused by the data itself: corrupted/malformed/unreadable input content, bad training batches that drive NaN/loss spikes, dataset content errors.
**Boundary rules:** Bad path, wrong permissions, format-handling bugs = user/application. Dataloader PROCESS death (OOM, deadlock) = software/system; only content-triggered loader failure lands here. Checkpoint unreadability from FS faults = storage.

### SDC/fail-slow
Manifestation class for silent and gray failures: silent data corruption (mercurial CPU cores, GPU/TPU SDC, radiation-induced flips) and fail-slow/straggler degradation (slow GPUs/nodes, degraded drives, throughput regressions) — events with no fail-stop signal.
**Boundary rules:** Every entry here is a MANIFESTATION and must cross-reference a causal class when diagnosed: Perseus shows 80% of storage fail-slow is software-rooted, SuperBench gray failures are hardware-rooted, CPU SDC is silicon-defect-rooted. Detected-uncorrectable errors (DBE, DUE) are NOT SDC — they are fail-stop and belong to their hardware class. Injected/synthetic performance anomalies (HPAS/FINJ) are filed here with a synthetic flag.
**Changed from v1:** Re-scoped from causal class to manifestation overlay with mandatory cross-reference; retained as a class because 8 sources report SDC/fail-slow as an indivisible unit.

### Scheduler/resource-mgmt
Workload-manager causal territory: scheduler/RM software bugs (PBS/Slurm/SGE/YARN/Borg control plane), scheduling-logic anomalies, preemption/eviction/requeue policy events, deadline kills, queueing anomalies.
**Boundary rules:** Preemption/eviction/requeue are POLICY OUTCOMES, not faults — kept here as outcome-labels so they never pollute failure rates; an eviction whose recorded reason is hardware recounts to that class. Terminal states like FAILED/TIMEOUT are meta, not scheduler causes. Scheduler-visible NODE_FAIL is meta with a hardware pointer.

### Outcome-label/meta
NEW meta class: labels and rows that carry no causal information — scheduler terminal states (FAILED/COMPLETED/CANCELLED/TIMEOUT/NODE_FAIL/LOST), binary failed flags, unknown/indeterminate residuals, coarse multi-class category labels (Hardware, Infrastructure), schema/field definitions, censoring artifacts, and aggregate statistical observations.
**Boundary rules:** A mention lands here iff it names an outcome or a label vocabulary rather than a component/actor. Coarse cause categories stay in a causal class only when unambiguous (Software→software/system, Network→network, Environment→facility, Human→user); 'Hardware' and 'Infrastructure' span multiple classes so they land here. Nothing here may appear in a cause row of the matrix; each entry may carry a pointer to the class the source claims dominates.
**Changed from v1:** New class. Absorbs the outcome-label rows previously scattered across user/application and unknown.

## Canonical failure types (every type, with rationale)

### GPU/accelerator hardware (16 types)

**GPU uncorrectable ECC error (DBE, Xid 48)**  *[cause]*
- *Aliases:* double-bit ECC error, DBE, ECCError, ECC errors, GPU Memory Errors, uncorrectable ECC error, ECC Uncorrectable (SECDED), dead_dbe, GPU ECC error, Summit DBE event, ECC ~38.9% (Nemotron)
- *Sources:* Acme, Unicron, Meta-RSC, Titan, Delta, Fire-Flyer(63/64/94/95 family), DGX-B200, NVIDIA DGX Cloud, Philly, Imbue, OPT, Ampere-mem, Beam-DUE, Summit
- *Why this class:* Origin is a physical bit-flip in GPU device memory (cosmic ray, voltage, wear) that exceeds SECDED correction; the GPU is the failing component and the error is always application-fatal.

**GPU correctable single-bit error (SBE)**  *[cause]*
- *Aliases:* Single Bit Error, Single-Bit Errors, Consecutive SBEs (degraded correctable), SBE offender nodes
- *Sources:* Titan, Delta, Ampere-mem
- *Why this class:* Same physical locus as DBE but corrected by ECC; a cause signal (predictor of DBE/page retirement), not a job-killing event.

**GPU memory row remapping / page retirement (Xid 63/64)**  *[symptom]*
- *Aliases:* ECC dynamic page retirement, Row Remapping Event, Row Remapping Failure (spare-row exhaustion), nvidia::memory::retirement/replace, gray-failure row remapping (SuperBench)
- *Sources:* Titan, Delta, Fire-Flyer, M100-Nagios, SuperBench
- *Why this class:* A logged recovery action triggered by underlying degrading GPU memory cells; remapping failure marks spare-row exhaustion. Past a threshold it silently degrades performance (SuperBench >10 rows).

**GPU contained/uncontained memory error (Xid 94/95)**  *[cause]*
- *Aliases:* Contained Memory Error, Uncontained Memory Error
- *Sources:* Delta, Fire-Flyer, DGX-B200
- *Why this class:* Uncorrectable GPU memory fault with containment semantics; locus is device memory, differing only in blast radius (process kill vs node reboot).

**GPU HBM fault**  *[cause]*
- *Aliases:* GPU HBM3 Memory, high-bandwidth memory faults (MI250X), correctable HBM fault
- *Sources:* Llama3 (17.2%), HSDP (22.9%, largest), Frontier
- *Why this class:* On-package memory stack failure; the single largest interruption cause at Meta 100K-GPU scale.

**GPU SRAM fault**  *[cause]*
- *Aliases:* GPU on-chip/on-die SRAM errors
- *Sources:* Llama3, HSDP
- *Why this class:* On-die memory structure failure inside the accelerator.

**GPU off the bus (Xid 79 / OTB)**  *[symptom]*
- *Aliases:* GPU fell off the bus, GPU card dropout, GPU falling off the bus, dead_otb, OTB, GPU Fallen Off Bus, fallen off the bus (Tsubame-3)
- *Sources:* Meta-RSC, Titan, Delta, DGX-B200, Fire-Flyer, NVIDIA DGX Cloud, Tsubame-3, Llama3
- *Why this class:* The GPU vanishing from PCIe is a detection event, not a mechanism: Titan traced it to SXM/connector mechanical defects and board resistor corrosion; Meta-RSC shows 43-63% co-occurrence with PCIe errors and IPMI critical interrupts.
- *Ambiguity:* CPU/host memory/PCIe is defensible (it is a PCIe-link event); deciding rule: the failing part historically replaced is the GPU/board, so it stays in the GPU class with a PCIe cross-reference.

**NVLink error (Xid 74/145/149)**  *[cause]*
- *Aliases:* NVLinkError, GPU NVLink Error, NVLink errors, NVLink Error (Xid_74), XID 145/149 NVLink errors, NVLink failures (stalled point-to-point transfers), NVLink error (Imbue), NVLink (Minder 29.4%)
- *Sources:* Acme (30.25% of failure GPU-time), Unicron, Meta-RSC, Fire-Flyer (42.57% of Xids), Delta, DGX-B200 (top category), Llama3, Imbue, Minder
- *Why this class:* Fire-Flyer root-caused its dominant Xid 74 volume to NVLink Bridge connector hardware; failure domain is a single node/package and remediation is GPU/board swap — an accelerator fault, not a fabric fault.
- *Ambiguity:* Network/interconnect is the natural alternative (it is an interconnect); deciding rule: intra-node links repaired by accelerator replacement stay in the GPU class, inter-node fabric goes to network. This is the paper's stated NVLink rule.

**GPU GSP error (Xid 119/120)**  *[cause]*
- *Aliases:* GSP RPC timeout, GPU GSP Error, GPU execution errors (Xid 119), GPU System Processor (Llama3)
- *Sources:* Delta (A100 3,857; 100% job-fatal), Fire-Flyer, DGX-B200, Llama3
- *Why this class:* The GPU System Processor (on-die service processor) hangs; requires GPU reset/RMA. Nearly eliminated on H100, indicating a silicon/firmware generation issue.
- *Ambiguity:* Software/system if treated as firmware code defect; deciding rule: the GSP is a GPU-resident component whose failure is cleared by GPU reset, so it stays with the accelerator.

**GPU PMU SPI error (Xid 122/123)**  *[cause]*
- *Aliases:* PMU SPI Error
- *Sources:* Delta (97.56% job-fatal)
- *Why this class:* Power-management-unit communication failure inside the GPU package; mechanism undocumented by NVIDIA but locus is the accelerator.

**GPU thermal interface/sensor fault**  *[cause]*
- *Aliases:* GPU Thermal Interface + Sensor
- *Sources:* Llama3, HSDP
- *Why this class:* Physical TIM/sensor defect on the GPU assembly.

**GPU overheating / thermal throttling**  *[symptom]*
- *Aliases:* GPU thermal limiting, GPU thermal-limit event, temperature-related GPU failures (Tsubame-3), GPU overheating (Kalos NVLink/ECC link)
- *Sources:* SURF-Lisa, Tsubame-3, Acme (overheating behind NVLink/ECC spikes)
- *Why this class:* Thermal excursion is a condition that precipitates NVLink/ECC failures and throttling; the GPU is where it manifests.
- *Ambiguity:* Power/facility when the origin is rack/room cooling capacity (SURF explicitly blames rack air-cooling limits); deciding rule: sensor/TIM defect = GPU class, inadequate facility cooling = power/facility.

**Generic GPU/accelerator hardware failure**  *[cause]*
- *Aliases:* Faulty GPU, Faulty GPU Compute, GPU (Tsubame-2 44.37%/Tsubame-3 27.81%), GPU hardware failures, dead/faulty GPUs, GPU Unavailable, Accelerator Fault, Aicore kernel execute failed, XID-classified GPU failure, GPU failure/repair (Lassen), defective MI250X hardware, cross-generation GPU failure, GPU display/video-memory rarities (Xid 56/57/58/65), simultaneous correlated GPU reboots, GPU replacement survival analysis (Titan), fail-stop (TPU)
- *Sources:* Llama3 (30.1%), HSDP, Meta-RSC, Frontier-TSUBAME, L4, OPT, Lassen, TitanGPULife, Minder, TPUv4
- *Why this class:* Bucket for accelerator failures reported without a finer mechanism; the replaced/drained component is the GPU (or TPU chip).

**GPU board component failure (resistor corrosion)**  *[cause]*
- *Aliases:* silver sulfide corrosion DBE/OTB storm, SXM2-Board, SXM2_Cable
- *Sources:* Titan (~59% of 18,688 GPUs replaced), Tsubame-3
- *Why this class:* Root cause on the GPU circuit board, not the die — the canonical example of an environmental-chemistry hardware mechanism behind a DBE/OTB symptom storm.

**Radiation-induced GPU DUE (illegal/misaligned address, illegal instruction)**  *[cause]*
- *Aliases:* Illegal Address (beam), Misaligned Address, Illegal Instruction (beam), illegal address access (DUE source)
- *Sources:* Beam-DUE
- *Why this class:* Neutron-induced transient bit flips corrupting addresses/instruction words; cause is a particle strike on GPU silicon, distinguishable from the identically-named user-code errors by injection context.
- *Ambiguity:* These CUDA error strings are indistinguishable from user bugs in field logs; deciding rule: beam/injection provenance = hardware transient, production logs default to user/application.

**GPU-stack death undetected by heartbeat**  *[symptom]*
- *Aliases:* nodes answer heartbeats while GPU stack dead
- *Sources:* BlueWaters
- *Why this class:* A detection-gap manifestation of GPU failure; matters for the paper's monitoring argument.

### CPU/host memory/PCIe (11 types)

**Host DRAM/DIMM error**  *[cause]*
- *Aliases:* Main Memory Errors, System Memory, Main Memory (CPU) ECC errors, Memory failures (LANL >10% everywhere), DIMM (lemon 20.5%), Memory (Tsubame/HPC1 28.5%/COM1/COM2), Memory Unit (Mira), memory errors vs Chipkill escapes, DRAM CE, DRAM UE, DDR3 fleet memory error, Thunderbird ECC, KERNSTOR
- *Sources:* Meta-RSC, Llama3, HSDP, Fire-Flyer, LANL, BlueWaters, CFDR, Google-DRAM, Meza, Oliner, Frontier-TSUBAME, Mira
- *Why this class:* Host memory device physics; the most common low-level hardware cause in classical HPC (LANL) and a steady lemon-node driver in AI clusters.

**Host CPU fault**  *[cause]*
- *Aliases:* CPU (Llama3/Tsubame/HPC1/COM1/COM2), CPU-related failures (LANL type E design flaw >50%), CPU latency out of range (SuperBench)
- *Sources:* Llama3, Frontier-TSUBAME, LANL, CFDR, SuperBench
- *Why this class:* Processor silicon/design failure on the host; LANL's type-E design flaw shows a single CPU defect can dominate a system's failure profile.

**PCIe error / link degradation**  *[cause]*
- *Aliases:* PCIe Errors, PCIe Device, PCIe downgrading, PCIe link-width degradation (~25% of Imbue hosts), PCIe config issues, invalid DMA mapping, H2D/D2H memory bandwidth defect, PCIe-related faults (~6.6%), Link failure (NVMe PCIe) [device-side counted in storage]
- *Sources:* Meta-RSC (43-63% co-occur Xid 79), HSDP (18%), Imbue, MegaScale, Unicron, SuperBench, Nemotron
- *Why this class:* Host bus/link hardware and configuration; the strongest documented precursor of GPU-off-bus events.
- *Ambiguity:* When a PCIe error surfaces only as Xid 79, sources file it under GPU; deciding rule: explicit PCIe/AER/bandwidth evidence = this class, bare Xid 79 = GPU symptom row.

**Motherboard/BIOS/board/chassis fault**  *[cause]*
- *Aliases:* Server Chassis, IO Expansion Board, System Board, IP Motherboard, PCI motherboard, MLB, Motherboard (COM2 23.4%), Generic Card/Board (Mira), Blue Gene/Q compute card (78.16% of RAS job kills; msg 00080014/0008000B), BIOS (lemon 7.7%), Boot (Tsubame), mainboard damage (L4), Case, Rack, LED Front Panel, Ribbon Cable, DetectedClockCardErrors
- *Sources:* Llama3, Frontier-TSUBAME, CFDR, Mira/ALCF, Meta-RSC, L4, Intrepid
- *Why this class:* Node board-level hardware; on Mira the compute-card category alone explains 78% of system-attributed job kills.

**Whole-node failure / unreachable**  *[symptom]*
- *Aliases:* NodeFailure (Acme), Node Fault (L4), Machine unreachable, node lockups, Down (Tsubame), heartbeat loss (HBEAT), node unavailability/continuous downtime, harderror/softerror (Alibaba machine events), runtime fault instance (Minder faulty machine), missing-heartbeat detection
- *Sources:* Acme, L4, DGX-B200, Delta, Oliner, FRESCO, Alibaba-2017, Minder, Frontier-TSUBAME
- *Why this class:* Node death is observable at every layer but explains nothing: it masks board, PSU, kernel, or GPU causes ('uncategorized errors caused by unclear hardware issues' — Acme).
- *Ambiguity:* Could be meta (pure outcome); deciding rule: kept here because sources treat it as a hardware-side event with hardware remediation (drain/RMA), unlike scheduler NODE_FAIL states.

**IPMI critical interrupt**  *[symptom]*
- *Aliases:* BMC critical events, bmc::events, sys::rvitals
- *Sources:* Meta-RSC, M100-Nagios
- *Why this class:* Platform-management detection signal co-occurring with PCIe/Xid-79 events; a sensor, not a mechanism.

**Machine-check exception**  *[symptom]*
- *Aliases:* KERNMC, machine check interrupts, machine checks (Google CEE class 2)
- *Sources:* Oliner, Loghub, Google-SDC
- *Why this class:* Hardware-detected error report from the CPU; the detector output for several silicon causes.

**Kernel-detected memory/TLB interrupt (KERNDTLB)**  *[symptom]*
- *Aliases:* data TLB error interrupt, KERNELDTLB
- *Sources:* Oliner (BG/L), Loghub
- *Why this class:* Kernel log signature of host memory-path hardware faults.

**Lemon / repeat-offender node**  *[symptom]*
- *Aliases:* lemon-node root causes (GPU 28.2%/DIMM 20.5%/PCIe 15.4%/EUD/BIOS/NIC/PSU/Optics), repeat-offender node degradation (MTBI 719h→152h), EUD
- *Sources:* Meta-RSC, SuperBench
- *Why this class:* A statistical identity (node that keeps failing) whose underlying causes decompose into ordinary component classes; kept as a type because both hyperscalers operationalize it.

**Defective node failing proactive validation**  *[symptom]*
- *Aliases:* defective nodes overall (10.36%), defective hardware not detected by health checks, checknode Failed Node Screen, hardware anomalies that manifest probabilistically
- *Sources:* SuperBench, Frontier, MegaScale
- *Why this class:* Screening-time detection label over heterogeneous latent hardware defects; the causal content lives in the per-component rows.

**Transient parity error cleared by reboot**  *[cause]*
- *Aliases:* parity errors cleared by reboot (CPU/memory outages)
- *Sources:* CFDR/FAST07
- *Why this class:* Transient host-silicon upset; noted because it inflates CPU/memory outage counts without component replacement.

### Network/interconnect (8 types)

**IB/Ethernet fabric link flap or failure**  *[cause]*
- *Aliases:* Infiniband Link, IB Network Flash Cut, link flapping, Network interface flapping, NIC-ToR link failure (~0.057%/mo), network link flapping (bucket 1), Ethlink Errors, InfiniBand/Ethernet link errors, IB (Tsubame ~2%), VAPI KERNEL_IB fatal, net::ib::status, NIC port link down / pcs_err_cnt
- *Sources:* Meta-RSC, Fire-Flyer (~200 IB events/yr), Unicron, MegaScale, Alibaba-HPN, NVIDIA, Frontier-TSUBAME, Oliner, M100, L4
- *Why this class:* Physical-link instability between NIC, cable, and switch; kills synchronous multi-node jobs even when transient.

**Switch/cable/optics failure**  *[cause]*
- *Aliases:* Network Switch/Cable, ToR switch critical error/crash, AOC errors, Optics (lemon), QSW Quadrics switch, SP Switch failures, Omni-Path, dev::swc::* switch health/config-drift checks, NIC/network switch/cable
- *Sources:* Llama3 (8.4%), HSDP, Alibaba-HPN, DGX-B200, CFDR, NERSC, Frontier-TSUBAME, M100
- *Why this class:* Fabric-side shared hardware; failure domain spans many nodes at once.

**NIC/HCA fault**  *[cause]*
- *Aliases:* NIC (Llama3/lemon/COM1), NIC dropout, IB HCA loopback below spec (6.04% of nodes — SuperBench's largest defect), RNIC/RDMA bandwidth degradation, hfi errors, GM_PAR NIC SRAM parity, GM_LANAI (LANai not running), GM_MAP mapper assertions
- *Sources:* Llama3, Meta-RSC, SuperBench, MegaScale, DGX-B200, Oliner (Spirit/Liberty), Tsubame-3
- *Why this class:* Host-side network adapter hardware/firmware; SuperBench shows it is the single largest deploy-time defect source, dwarfing GPU compute defects.
- *Ambiguity:* GM_* are Myrinet firmware/driver failures — software/system is arguable; deciding rule: faults cleared only by NIC reflash/replacement stay here.

**NCCL/collective-communication timeout**  *[symptom]*
- *Aliases:* NCCLTimeoutError, NCCL communication timeout, NCCL Watchdog Timeouts, NCCL timeout (10.1% Unicron), UB timeout, Mixed NCCL/NVLink hangs, PyTorch NCCL watchdog errors, Transformer Engine communication hangs, Notify register timeout (when network-side)
- *Sources:* Acme, MegaScale, Meta-RSC, Llama3 (root cause undetermined), HSDP (9%), Unicron (largest single cause), NVIDIA
- *Why this class:* The canonical masking symptom: a collective times out when ANY rank is stuck — GPU fault, link failure, or software hang upstream. Meta-RSC explicitly marks all three domains; Llama3 files 7 under Unknown.
- *Ambiguity:* Software/system (it is a library watchdog) — deciding rule: filed under network as the symptom's reporting layer, but it must never enter a cause row; diagnosed instances recount to the true class.

**Comm-library remote/system error**  *[symptom]*
- *Aliases:* NCCLRemoteError, NCCL system error, Network error (NCCL), unhandled CUDA error in NCCL, GPU NCCL all-to-all/all-reduce test failures, HCCP/ROCE error cqe status, NIC/network error reported by NCCL (~5.7%)
- *Sources:* Acme, NVIDIA, MegaScale, L4
- *Why this class:* Errors surfaced by the communication library on behalf of a remote peer or transport; the library is the messenger, not the origin.
- *Ambiguity:* Software/system when the defect is in the library itself; deciding rule: reproducible across healthy fabric = software bug, correlated with a link/node = network/hardware.

**TCP/connection error**  *[symptom]*
- *Aliases:* ConnectionError (most frequent Acme infra error), connection refused, connection reset, lost connection, network socket binding errors, network timeouts (retry-worthy class), auxiliary-service network instability
- *Sources:* Acme, Unicron, Frontier, Philly
- *Why this class:* Transport-level symptom, frequently from auxiliary services (metrics/logging) rather than the training fabric (Acme); transient and retryable (Unicron SEV3).

**MPI runtime/communication failure**  *[symptom]*
- *Aliases:* MPI error, MPI runtime failure (longest RTF in Philly), MPI deadlock, internal MPI daemon failure
- *Sources:* Philly, BlueWaters
- *Why this class:* Failed peer connections or daemon death seen through the MPI layer; masks network hardware, peer node death, or library bugs.
- *Ambiguity:* Software/system for library-internal bugs; deciding rule: same as NCCL — messenger layer files the symptom, diagnosis reassigns.

**Generic network failure**  *[cause]*
- *Aliases:* NetworkError, other network errors, Network (LANL/Tsubame ~8.7%), Network Fault (L4's most common hardware sub-type), burst-failure network root cause, Message Unit / MU torus errors (Mira 2.81%), Gemini HSN / LNet interrupts, tree-network packet errors, Nagios network checks
- *Sources:* Acme, Unicron, LANL, Frontier-TSUBAME, L4, FRESCO, Mira, BlueWaters, M100
- *Why this class:* Attributed-to-network bucket where sources did not name link vs switch vs NIC; retained as coarse cause since the locus (fabric) is established.

### Storage/filesystem (9 types)

**Remote/parallel filesystem failure or unavailability**  *[cause]*
- *Aliases:* S3StorageError, Filesystem Mounts, Storage Fault (L4), exit code 107 transport endpoint not connected (33% of FRESCO-A system failures), KERNMNTF Lustre mount FAILED, Lustre client problems, Lustre OSS LBUG, PTL_EXP/PTL_ERR/OST Lustre timeouts, system-wide outages (74% Lustre-involved), scratch/project/home Lustre MTBI, remote FS burst clusters, network+NFS congestion clusters, sys::gpfs::status / Nagios storage checks, global-FS failure, file-system failures via VSD/I-O nodes, HDFS transient errors
- *Sources:* Acme, Meta-RSC, L4, FRESCO, Oliner, BlueWaters, Tsubame-3, NERSC, M100, Philly
- *Why this class:* Shared-storage software/service failure is its own causal locus: one Lustre/NFS incident fans out into hundreds of correlated job failures (FRESCO exit-107 bursts, BlueWaters SWOs).
- *Ambiguity:* Network/interconnect for congestion-mediated cases: FRESCO attributes 20/26 bursts to network+NFS congestion; deciding rule: if the FS servers were healthy and only the path was saturated, file under network.

**Checkpoint save/load failure**  *[symptom]*
- *Aliases:* Model ckpt error (21.7% of Philly RTF), Failed to load checkpoint, unable to checkpoint (FS unavailable)
- *Sources:* Philly, L4, BlueWaters
- *Why this class:* Late-stage manifestation of remote-FS faults with outsized cost (fails after epochs of work); locus is the storage path.
- *Ambiguity:* User/application when the checkpoint path/permissions are wrong (L4 Misoperation); deciding rule: transient FS error = storage, bad path/perms = user.

**Storage I/O bottleneck / slow-filesystem-induced failure**  *[cause]*
- *Aliases:* checkpoint I/O bottleneck (NFS RPC slot saturation), checkpoint-I/O event, bus error root-caused to slow filesystem, remote IO / parallel-FS contention failures, NFS GETATTR surge behind ECC-labeled failures
- *Sources:* DGX-B200, NVIDIA, FRESCO
- *Why this class:* Saturated storage paths cause both outright job death (bus error, mmap on slow FS) and stalls; a performance-mode storage fault distinct from unavailability.

**Local filesystem software bug**  *[cause]*
- *Aliases:* XFS software bug (8.2% of Tsubame-3 sw loci), ext4 bug, EXT3-fs aborted journal (EXT_FS), CHK_DSK fault asserts
- *Sources:* Tsubame-3, Oliner (Thunderbird/Spirit)
- *Why this class:* Kernel-FS code defects; filed under storage per the boundary rule (failure domain and fix are filesystem-side).
- *Ambiguity:* Software/system (it is kernel code) — deciding rule adopted: all FS software goes to storage so the matrix's storage row captures the full storage stack.

**Disk/SSD/NVMe fail-stop failure**  *[cause]*
- *Aliases:* SSD (Llama3/HSDP/Tsubame ~290h recovery), Disk, Hard drive replacements (HPC1 30.6%, COM2 49.1%), DSK_FAIL, SCSI offline device, CMD_ABORT, EXT_CCISS controller storms, MPT task abort, BUS_PAR bus parity, drive failure, Backblaze failure label (AFR 1.36%), reactive failure, proactive SMART-triggered failure, SMART 5/187/188/197/198 predictors, failures with no SMART warning (23.3%), NVMe fail-stop symptoms (I/O 49.6%, Boot 19.6%, Threshold, Link, Lost), per-disk HDD failure label, SSD failure via trouble ticket, correlated intra-node/intra-rack drive failures, correlated second-failure-in-RAID-rebuild, node internal disk failure, ARR vs datasheet AFR (~3.4x), model/vintage AFR variance, bad-batch SATA lubricant breakdown, NPF returned drives (43%), infant mortality of batches, WAF<=1 deadly population, CD-ROM, disk errors (L4 node fault), labeled device failure (IOTTA), S187 correlated-failure indicator
- *Sources:* Llama3, HSDP, Frontier-TSUBAME, Oliner, CFDR/FAST07, Backblaze, SNIA (ATC'22/FAST'21/PAKDD), USRC, NERSC
- *Why this class:* Storage-device hardware death in all its ticketed symptom forms; the symptom sub-labels (I/O, Boot, Lost, Link) are kept as aliases of one device-failure cause since they share locus and remediation (replacement).

**Tape drive/media failure**  *[cause]*
- *Aliases:* HPSS tape drive ARR 15-20%/yr, tape cartridge media errors
- *Sources:* NERSC/CFDR
- *Why this class:* Archival-tier device/media failure; media (cartridge) is the most common cause of drive tickets.

**RAID/storage-controller/HBA fault**  *[cause]*
- *Aliases:* Controller, RAID card, RAID controller, SCSI board, SCSI BP, SCSI cable, dev::raid::status, shared HBA fault slowing all drives
- *Sources:* CFDR, COM1/COM2, M100, SNIA/Perseus
- *Why this class:* Shared storage-path hardware whose failure or degradation affects every drive behind it.

**Drive component defect causing fail-slow**  *[cause]*
- *Aliases:* bad capacitors (33/100 RMA), bad chips (46/100), bad sectors, rotor eccentricity, stuck read-only mode, root cause unresolved (21/100)
- *Sources:* SNIA/Perseus, ATC'22
- *Why this class:* The 20%-of-fail-slow hardware mechanisms Perseus verified; causes referenced by the fail-slow symptom row in the SDC/fail-slow class.

**Disk-space exhaustion**  *[cause]*
- *Aliases:* disk-space outages (BLOOM)
- *Sources:* BLOOM
- *Why this class:* Capacity exhaustion on shared storage halting training.
- *Ambiguity:* User/application when a user's own quota/output growth is at fault; deciding rule: shared-volume exhaustion = storage, per-user quota = user.

### Power/facility (4 types)

**Facility power outage / fluctuation**  *[cause]*
- *Aliases:* Power outages (LANL Environment), power outage (NERSC, comparable to unscheduled SW+HW), datacenter power fluctuations from synchronized GPU idle/busy transitions (tens of MW), cluster::status::wattage
- *Sources:* LANL, NERSC, Llama3, M100
- *Why this class:* Site electrical supply is the origin; longest mean repairs in LANL (~10h) and a new AI-specific mechanism (synchronized GPU load swings) in Llama3.

**Cooling/environment failure**  *[cause]*
- *Aliases:* A/C failures, System Cooling, Environment (LANL/CFDR category), temperature throttling (drive, env), insufficient power supply (drive env), diurnal throughput variation from midday temperature (1-2%), CPU overheating (FTA reason), environmental fail-slow causes
- *Sources:* LANL, HSDP, CFDR, SNIA/Perseus, Llama3, FTA
- *Why this class:* Facility thermal/environmental conditions degrade or kill hardware; includes the degrade-not-fail modes Llama3 documents.

**Node PSU/fan/power-board failure**  *[cause]*
- *Aliases:* Power Supply (Llama3/HPC1/COM1 34.8%/COM2), PSU (Tsubame, lemon 5.1%), FAN (Tsubame 2nd-largest), Fan, CPU heatsink, LV power board, Power-Board (~10 days recovery), Bulk Power Supply (Mira), Cooling Fan (LANL sub-cause), power leakage (L4)
- *Sources:* Llama3, Frontier-TSUBAME, CFDR, Mira, LANL, Meta-RSC, L4
- *Why this class:* Power-delivery and cooling components at node/rack scope; grouped with facility by function (power/cooling) per the class boundary rule.
- *Ambiguity:* CPU/host is defensible (they are node parts); deciding rule adopted: power/cooling function wins over board location so the matrix's power row captures the whole power path.

**Unplanned host maintenance interruption**  *[cause]*
- *Aliases:* Host Maintenance (Llama3 7.6%, HSDP 6.2%), host maintenance, forced OS upgrade (Borg EVICT reason)
- *Sources:* Llama3, HSDP, Borg
- *Why this class:* Operator/fleet-management action external to the job that interrupts it; a real interruption cause even though no component failed.
- *Ambiguity:* Scheduler/resource-mgmt is arguable (it is an orchestration decision); deciding rule: physical/host-level servicing = facility/ops, pure scheduling policy = scheduler.

### Software/system (9 types)

**OS kernel panic/fault**  *[cause]*
- *Aliases:* Kernel Fault (HSDP), Kernel Panic (msg 000A000D), hang by kernel panic (14% Tsubame-3 sw loci), kernel bug, Operating system failures (LANL sys E), Compute Node Kernel, KERNRTSP rts panic, KERNTERM, KERNREC, TOAST (PANIC_SP), NMI Dazed and confused, Losing-ticks CPU clock bug, OS Software (LANL sub-cause), memory swap, node hang (kernel)
- *Sources:* HSDP, Mira, Tsubame-3, LANL, Oliner
- *Why this class:* Kernel code defects and panics; the classic software failure locus in every pre-GPU study and still 5.8% of Meta HSDP interruptions.

**Unexpected node reboot**  *[symptom]*
- *Aliases:* System Reboot (HSDP 5.6%)
- *Sources:* HSDP
- *Why this class:* A reboot is the recovery event of an unlogged underlying fault (kernel, BMC, power); recorded as its own interruption category by Meta.

**System service/daemon failure**  *[cause]*
- *Aliases:* System Services (Meta-RSC), ciod errors (APPSEV/APPREAD/APPRES/APPUNAV), Machine Controller on Service Node (21.5%), Control System on Service Node, sbcast failures, ssh/sssd/xcat/monitoring Nagios checks, auxiliary services (metrics/logging), monitoring database storage error
- *Sources:* Meta-RSC, Oliner (BG/L), Mira, Frontier, M100, Acme, Ampere-mem
- *Why this class:* Control-plane and node daemons whose death kills or orphans jobs; Meta-RSC notes they can be corrupted from any domain but the code itself is the usual defect site.

**GPU driver/firmware error**  *[cause]*
- *Aliases:* GPU Driver/Firmware Error, GPU driver errors (SEV1), GPU Driver-related problems (42.7% of Tsubame-3 sw loci), GPUDriver, driver Xids 32/38/42/44/45/59/62 (push-buffer, firmware, context-switch, preemptive cleanup, microcontroller halt), FIRMWARE (Mira 62.1% by component), firmware mismatch (Imbue), Initialization Error (driver init)
- *Sources:* Meta-RSC, Unicron, Tsubame-3, Titan, Mira, Imbue, Beam-DUE
- *Why this class:* Driver/firmware code is the causal locus: small in share but SEV1 in consequence (node drain), and the top software root locus on Tsubame-3's AI-era workload.
- *Ambiguity:* GPU hardware for Mira's FIRMWARE attribution (hardware-embedded code); deciding rule: fixed by flash/patch = software, fixed by RMA = hardware.

**Framework/library software bug**  *[cause]*
- *Aliases:* Software Bug (Llama3 12.9%, HSDP 7.1%), Framework fault (L4, customized frameworks more fault-prone), Dependency, software bug (narrative), 2004 OS upgrade outage, 2006 security incident outage, VM failures (Tsubame ~7.7%), vm::virsh, failover-correlated application failures (37% within ±15min), inadequate automated failover, Frontier transient errors, stall-time inflation bugs, Software (coarse: LANL 5-24%, BlueWaters 20%/53% repair-hours, Oliner S 64% filtered, Tsubame-3 50.6%, NERSC dominant, Software_Error RAS, OtherSW, softerror, system-software faults tier, event-log software 65.7%)
- *Sources:* Llama3, HSDP, L4, NERSC, BlueWaters, Tsubame, LANL, Oliner, Mira, Meta-RSC
- *Why this class:* Defects in the training stack, platform software, VM and HA layers; the coarse 'Software' category labels are folded here because their locus, unlike 'Hardware', is unambiguous.

**CUDA runtime error (generic)**  *[symptom]*
- *Aliases:* CUDAError, CUDA errors, CUDA failure, unhandled CUDA error, CUDA runtime errors (excluded from B200 taxonomy), Launch Failure / kernel launch failure / interface (bus/link) error, Memory Allocation (CUDA), Devices Unavailable, Invalid Value, No Device/Invalid Device, Hardware Stack Error, Invalid PC, Invalid Address Space
- *Sources:* Acme (often the true cause behind NCCL cascades), Unicron, MegaScale, Philly, NVIDIA, Beam-DUE, DGX-B200
- *Why this class:* The CUDA runtime reports faults from GPU hardware, driver, or user code alike; Acme shows CUDAError frequently underlies NCCLTimeout cascades — a reporting layer, not an origin.
- *Ambiguity:* GPU hardware when correlated with Xids; user/application for API misuse; deciding rule: bare CUDA error strings stay in this symptom row until a Xid or stack trace reassigns them.

**Job/task hang or stall**  *[symptom]*
- *Aliases:* task hang (3.1%), Stuck training, node hang, system-induced hangs logged as walltime (undercounted), Abnormal behavior (L4 16.6%: hangs and slowdowns), stalls with no RDMA traffic
- *Sources:* Unicron, Acme, BlueWaters, L4, Tsubame-3
- *Why this class:* A hang is pure symptom — deadlock, network stall, or GPU fault upstream; BlueWaters shows hangs leak into walltime statistics, corrupting outcome-label counts.

**Dataloader crash/deadlock**  *[symptom]*
- *Aliases:* DataloaderKilled (costliest Acme framework failure), dataloader deadlock (BLOOM)
- *Sources:* Acme, BLOOM
- *Why this class:* The loader process dies or deadlocks — typically worker OOM or IPC bugs in the framework's loading machinery, per Acme's Framework attribution.
- *Ambiguity:* Data/input is the alternative the task raises; deciding rule: process-level death (OOM/deadlock/kill) = software; a loader failing on malformed CONTENT = data/input.

**I/O-scheduling software defect causing fail-slow**  *[cause]*
- *Aliases:* ill-implemented software scheduling (252/315 = 80%), OS scheduler preempting open-channel SSD FTL cores, Thread_ID = Disk_ID mod #Drives collision
- *Sources:* SNIA/Perseus
- *Why this class:* Perseus's verified root cause for 80% of fail-slow drives — fixed by scheduler/assignment changes, never by hardware replacement; causal locus is host software.

### User/application (11 types)

**User script/code error**  *[cause]*
- *Aliases:* TypeError (most frequent Acme error), NameError, KeyError, IndexError, SyntaxError, ArgumentError, ImportError, OSError, CalledProcessError, AssertionError, ZeroDivisionError, Syntax error (Philly), Script (category), Program/Script Bug (L4), user program errors tier, User errors (Helios: script config, syntax/semantic), User failures (FRESCO 33-48% of failures), user root-cause (L4, 2nd largest), User fault (root cause)
- *Sources:* Acme, Philly, L4, Helios, FRESCO, Meta-RSC, Borg
- *Why this class:* Defects in user-authored code and scripts; the highest-count, lowest-GPU-time failure family everywhere (fail-fast at startup).

**Framework-raised runtime exception (shape/dtype/attribute)**  *[symptom]*
- *Aliases:* RuntimeError, ValueError, AttributeError, Framework (category), tensor-op/shape/dtype errors
- *Sources:* Acme, AcmeTrace
- *Why this class:* Raised by the framework but almost always provoked by user model/config code (Acme: fail at startup); the exception name is the symptom of a user-side mistake.
- *Ambiguity:* Software/system when the traceback ends inside framework internals; deciding rule: user call-site in trace = user, framework-internal invariant violation = software.

**Environment/dependency/configuration error**  *[cause]*
- *Aliases:* Semantic error (library version mismatch, 9.2% Philly RTF), Software Incompatibility (L4), Configuration Error (low Notify-register timeout), CUDA ver. mismatch, CUDA init failed, Cannot load libs, ModelLoadingError, model-parallelism misconfiguration, Launching failure (L4 21.3% symptom), misconfiguration (Borg FAIL), wrong memory bounds
- *Sources:* Philly, L4, Acme, Borg, FRESCO
- *Why this class:* Version/config mismatches across image, driver, framework, toolkit — user-controlled environment state; disproportionately kills large multi-GPU jobs late (Philly).

**Missing file / permission error**  *[cause]*
- *Aliases:* FileNotFoundError (2nd most frequent Acme error), PermissionError, Permission error, Misoperation (checkpoint perms), IO (Mira user file mistakes: errno 2/13/21), Output node error, missing module/file/directory
- *Sources:* Acme, Philly, L4, Mira/ALCF, FRESCO
- *Why this class:* User file-management and access mistakes — Mira explicitly separates these misoperations from filesystem faults.
- *Ambiguity:* Data/input if the file is present but corrupt; storage if the FS made it unreachable. Deciding rule: errno-style path/perm errors = user; content errors = data; transport errors = storage.

**Application crash signal (segfault/abort/FPE/ILL/TRAP)**  *[symptom]*
- *Aliases:* Segmentation fault, SIGSEGV, SIGABRT, Core dump, Bug (Mira 7.35%), SIGFPE, SIGILL, SIGTRAP, Traceback from crash, exited abnormally (SEV2), segmentation faults
- *Sources:* MegaScale, Mira/ALCF, Philly, Unicron, Borg
- *Why this class:* Termination signals are how user-code memory/arithmetic bugs surface; occasionally the same signals mask hardware corruption (Titan Xid-13 case), but default attribution is the application.

**Host out-of-memory kill**  *[symptom]*
- *Aliases:* CPU out of memory (most frequent Philly type), OOM, OUT_OF_MEMORY (Slurm state), exit code 137, ENOMEM completion code 12, SGE OOM, memory leak (Borg FAIL reason), OOM death spiral near limit
- *Sources:* Philly, Meta-RSC (Table I: user program only), SURF, F-DATA, Eagle-Kestrel, FRESCO (r=0.83 with tail memory), Trinity, Tsubame-3, Borg
- *Why this class:* The OOM kill is a kernel enforcement event; Meta-RSC attributes it to the user program (mis-sized request or leak), and FRESCO's correlation with tail memory usage confirms user-side sizing as the usual origin.
- *Ambiguity:* The task's flagged case. Deciding rule: OOM within the user's requested allocation = user misconfig (this row); OOM from node overcommit/eviction (Borg EVICT) or a leaking system service = scheduler or software respectively.

**GPU out-of-memory**  *[symptom]*
- *Aliases:* GPU out of memory (Philly), OutofMemoryError (Acme)
- *Sources:* Philly, Acme
- *Why this class:* CUDA allocator exhaustion from model/batch sizing — user-controlled; distinct row because remediation (resize model) differs from host OOM.

**GPU illegal memory access / MMU fault (Xid 31/43)**  *[symptom]*
- *Aliases:* illegal memory access, Invalid mem access, MMU Error (Xid 31, 60-95% of Delta critical errors), Xid 43 illegal/out-of-bounds access, GPU memory page fault, GPU stopped processing (Titan Xid 43), Software Causes Xid_31/Xid_43
- *Sources:* Fire-Flyer (33.5%+19.2% of Xids), Delta, Titan, Unicron, NVIDIA, Philly
- *Why this class:* Application-triggered by consensus of Fire-Flyer, Titan, and Delta — user kernels touching illegal addresses; but Fire-Flyer warns it 'may also mask hardware memory corruption'.
- *Ambiguity:* GPU hardware (corrupted pointer from a real bit-flip); deciding rule: reproducible on healthy hardware = user; node-correlated recurrence across users = hardware.

**Graphics engine exception (Xid 13)**  *[symptom]*
- *Aliases:* Software Causes Xid_13, Xid 13/31/43/45 software group
- *Sources:* Titan (most frequent Xid), Fire-Flyer
- *Why this class:* Mostly user application bugs per Titan, but with a confirmed hardware case — Titan explicitly warns source attribution for this Xid is unreliable.
- *Ambiguity:* GPU hardware; same reproducibility rule as Xid 31/43.

**Human/operator error**  *[cause]*
- *Aliases:* Human error (LANL, shortest repairs), Human (CFDR category), ctrl-C/command errors
- *Sources:* LANL, CFDR, FRESCO
- *Why this class:* Admin/operator action is the origin; LANL's share is notably below Gray's classic 10-15%, likely undercounted.

**Training instability: loss spike / NaN / divergence**  *[symptom]*
- *Aliases:* Loss spike, NaN in gradients, loss divergences, NaN/underflow, NaN-loss, FP16 instability, loss-spike event (benign vs malignant), Model diverged, gradnorm spikes, non-convergence
- *Sources:* Acme, NVIDIA, OPT, GLM-130B, LLM360, Philly, Fire-Flyer
- *Why this class:* A numerical-trajectory anomaly that three distinct causes produce: algorithmic instability (default), bad data batches, or SDC. Acme's mitigation (rollback + skip offending batches) shows data is often implicated.
- *Ambiguity:* Data/input (bad batches) and SDC/fail-slow (Fire-Flyer traced spikes to uncaught SDC); deciding rule: fixed by skipping batches = data; node-dependent reproduction = SDC; otherwise = user/algorithmic.

### Data/input (1 types)

**Corrupt/malformed input data**  *[cause]*
- *Aliases:* Incorrect inputs (largest Philly RTF share, 30.4%), corrupted data/inconsistent format, data issues (GLM), offending data batches, DatasetLoadingError
- *Sources:* Philly, GLM-130B, Acme
- *Why this class:* The data content itself is wrong — unreadable, mis-formatted, or corrupt — independent of user code correctness or storage health.
- *Ambiguity:* User/application for bad paths (Philly lumps 'bad path' into this category); deciding rule: path/naming = user, byte content = data.

### SDC/fail-slow (5 types)

**CPU silent data corruption (mercurial cores/CEE)**  *[cause]*
- *Aliases:* Meta device errors / early-life failures / degradation / end-of-life wear-out, Google CEE symptom classes 1-4, mercurial-core characterization, Alibaba computation-type SDCs, consistency-type SDCs, bitflip characterization, apparent vs tricky SDCs, defect scope obs., failure-rate by test timing, multi-bit flips defeating ECC, vector-instruction SDC (SEVI), production-CPU SDC
- *Sources:* SDC-trio (Meta/Google/Alibaba), SEVI
- *Why this class:* Defective CPU silicon computing wrong answers without any error signal; causal locus is manufacturing/wear defects in cores, but filed in the SDC manifestation class because detection, not component, defines the operational problem.
- *Ambiguity:* CPU/host memory/PCIe (the defective part is a CPU); deciding rule adopted: silent manifestation wins the class, with the causal component recorded in the rationale/cross-reference.

**GPU/accelerator silent data corruption**  *[cause]*
- *Aliases:* Silent Data Corruption (Llama3 6 cases), Numerics/SDC (HSDP 5.5%), SDC not caught by ECC (Fire-Flyer), SDC (beam, FIT rates), SDC (TPU), gate-level GPU error pattern, SDC in LLM training, simulated precision-resilience fault, NaNs in intermediates (bucket 1)
- *Sources:* Llama3, HSDP, Fire-Flyer, Beam-DUE, TPUv4, SDC-anatomy, LLM-SDC, LLM-PRISM, NVIDIA
- *Why this class:* Wrong results from accelerator hardware with no fail-stop signal; invisible to Xid taxonomies (Fire-Flyer) and detectable only via training-dynamics anomalies.

**Compute fail-slow / straggler**  *[symptom]*
- *Aliases:* Computational stragglers (~0.5% of machines, ~10% slower), Stragglers (slow-but-not-failed communicators), Speed regressions (transient + persistent), performance degradation (Minder), Fail-slow events (DGX-B200 4/21), gray failure/degradation, fail-slow/less-reliable hardware (MIT-SC), gradual MFU decrease, end-to-end benchmark regressions (BERT/ResNet/GPT-2/LSTM/DenseNet/GEMM below spec), MatMul/all-reduce overlap gray failure, IB/NVLink all-reduce throughput degradation, broken redundant IB links (congesting collectives), Others (performance degradation, B200)
- *Sources:* MegaScale, Llama3, NVIDIA, Minder, DGX-B200, SuperBench, MIT-SC
- *Why this class:* Degradation-without-crash is a manifestation spanning GPU silicon, links, and software skew (MegaScale traced MFU decay to GC/time skew — software); every diagnosed case recounts to a causal class.
- *Ambiguity:* Any hardware class; deciding rule: this row records the gray manifestation, the matrix cause cells cite the diagnosed origin.

**Storage fail-slow (gray drive degradation)**  *[symptom]*
- *Aliases:* fail-slow NVMe (1.41%/4mo, 6x HDD rate), fail-slow->fail-stop transition (0.22%), Local IO bottleneck failures (FRESCO ~6MB/s peak), degraded NVMe
- *Sources:* SNIA (ATC'22/Perseus), FRESCO
- *Why this class:* Drive >=2x slower than peers with no SMART signal; Perseus proves 80% are software-rooted and only 20% hardware — the strongest evidence in the corpus that fail-slow is a manifestation, not a hardware class.
- *Ambiguity:* Storage/filesystem; deciding rule: symptom here, causes split to the I/O-scheduling-defect row (software) and drive-defect row (storage).

**Injected performance-anomaly fault (HPAS/FINJ suite)**  *[cause]*
- *Aliases:* cpuoccupy, cachecopy, dcopy, membw, memleak, memeater, netoccupy, dial, leak, ddot, cpufreq, pagefail, ioerr, copy (HDD)
- *Sources:* E2EWatch, Sandia Eclipse, ALBADross, Proctor, Prodigy, Antarex/FINJ
- *Why this class:* Synthetic contention/interference/misconfiguration faults injected to train detectors; they emulate fail-slow and resource-interference modes. Flagged synthetic — must never be pooled with field failure rates.

### Scheduler/resource-mgmt (3 types)

**Scheduler/resource-manager software failure**  *[cause]*
- *Aliases:* Scheduler software failures (LANL sys H most common sw failure), PBS_CHK task_check bug (largest filtered Oliner category, ~1,336 jobs killed), PBS_CON, PBS_BFD, PBS (Tsubame), batchs::* Nagios checks, workload-manager downtime, Platform fault (L4: resource-management logic bugs, abnormal preemption, platform config defects), job-scheduling anomalies
- *Sources:* LANL, Oliner (Spirit/Liberty), Frontier-TSUBAME, M100, F-DATA, L4
- *Why this class:* Bugs in the workload manager itself kill jobs wholesale (one PBS bug killed up to 1,336 jobs); the causal content of the scheduler class.

**Preemption/eviction/requeue (policy event)**  *[outcome-label]*
- *Aliases:* Preempted, PREEMPTED, Job preempted (YARN reclaim), EVICT (Borg infra-caused), Requeued, REQUEUED, Vacated, Interrupted (Alibaba 2017), higher-priority delay (M100)
- *Sources:* Meta-RSC, Philly, Borg, F-DATA, Alibaba-2017, Trinity
- *Why this class:* The task's flagged case: preemption is deliberate scheduler policy, not a failure — the actor is the scheduler acting correctly. Kept in this class so policy-loss can be quantified without polluting failure rates.
- *Ambiguity:* Borg EVICT bundles genuine infra causes (hardware failure, OOM overcommit); deciding rule: eviction with a recorded infra reason recounts to that causal class; reason-free evictions stay here as policy.

**Queueing/scheduling anomaly (never scheduled)**  *[outcome-label]*
- *Aliases:* Waiting (PAI, submission stuck), P90 queueing delay, DEADLINE (Kestrel scheduler deadline kills)
- *Sources:* Alibaba-PAI, Eagle-Kestrel
- *Why this class:* Jobs harmed by scheduling behavior rather than execution faults; DEADLINE is a scheduler-initiated termination policy.

### Outcome-label/meta (11 types)

**FAILED (generic non-zero-exit outcome)**  *[outcome-label]*
- *Aliases:* FAILED (Slurm, all traces), Failed (Philly/PAI/M100/pod phase), FAIL (Borg), JOBFAIL, status 0 (SWF), EC=1/EC>1, failed/presumably failed (F-DATA), Unsuccessful (Philly retries exhausted), Failed jobs (Tachyon binary, TwoSigma), Development jobs (FAILED-like), dep_fail, non-complete (Lassen ~10%), Application exit status: user (BlueWaters 18.75%)
- *Sources:* Meta-RSC, SURF, Helios, F-DATA, Eagle-Kestrel, Borg, PWA/SWF, Tachyon, ATLAS-TwoSigma, MIT-SC, PAI, Philly, AcmeTrace, BlueWaters
- *Why this class:* A scheduler exit state covering application bugs, bad inputs, environment errors, and some system faults with zero cause information (Eagle docs say so explicitly); must live in the meta row so cause rows stay clean.

**COMPLETED (success outcome)**  *[outcome-label]*
- *Aliases:* COMPLETED, Pass, FINISH, Normal (exit 0), Terminated (PAI = success), status 1 (SWF), completed (F-DATA), Mature jobs, finish successfully, Success (exit 0), JOBEND
- *Sources:* all trace sources
- *Why this class:* The non-failure baseline; included because every mention must map and completion rates are the paper's denominators.

**CANCELLED / user kill (outcome)**  *[outcome-label]*
- *Aliases:* CANCELLED, Killed (Philly 13.5%, 37.7% of GPU time), KILL (Borg, 85% of ended 2019 jobs), JOBCANCEL, Kill (SIGKILL mid-execution), status 5 (SWF), Exploratory jobs (early-stop), Aborted jobs, CANCELLED by 0 (root/admin — hides system-initiated kills), dependency-driven batch cancellations (Mustang)
- *Sources:* Helios, Philly, Borg, Mira/ALCF, PWA/SWF, MIT-SC, ATLAS-TwoSigma, Eagle-Kestrel, SURF
- *Why this class:* User/parent-initiated termination — mostly feedback-driven exploration (Helios), not failure; but Mustang and 'CANCELLED by 0' prove real hardware/system failures hide inside this label.
- *Ambiguity:* Cancellations triggered by failures (Mustang FAQ) belong in causal rows but are indistinguishable in the traces; deciding rule: without a kill-reason field, all stay here with a stated undercount caveat.

**TIMEOUT / walltime kill (outcome)**  *[outcome-label]*
- *Aliases:* TIMEOUT, Timeout (Mira 14.6%, dominant abnormal mode), walltime (BlueWaters 4.71%), Walltime (FRESCO, excluded from failure analysis), wallclock_limit inferred timeout, IDE/interactive TIMEOUT-like jobs, Timeout jobs (LANL 49-55% of CPU time), system kills for exceeding runtime limits
- *Sources:* SURF (largest runtime/energy share), Mira/ALCF, BlueWaters, FRESCO, Eagle-Kestrel (43.5% of node-hours), ATLAS, Meta-RSC, Helios, F-DATA
- *Why this class:* Walltime enforcement is policy meeting user misestimation — and some users time out intentionally (Eagle); BlueWaters proves system-induced hangs leak into it, so it cannot serve as a cause bucket.
- *Ambiguity:* User/application (misestimation) vs software (hidden hangs); deciding rule: stays meta; studies wanting cause must join with hang/failover logs as LogDiver did.

**NODE_FAIL (scheduler-visible node death)**  *[outcome-label]*
- *Aliases:* NODE_FAIL (all Slurm traces), Node fail (M100), node failure (Slurm-reported), NODE_FAIL absent from Mustang
- *Sources:* Meta-RSC, SURF (correlation 0.94), Eagle-Kestrel (only unambiguously system-attributed label), F-DATA, Helios, NVIDIA, MIT-SC, AcmeTrace
- *Why this class:* An outcome-label with a reliable pointer (infrastructure), but still not a cause: it says a node died, not why. Kept meta with a standing cross-reference to hardware classes.
- *Ambiguity:* CPU/host hardware is where most analyses count it; deciding rule: matrix cause rows take diagnosed node faults (the whole-node-failure symptom row); the Slurm state itself stays meta.

**RAS/system-event job kill**  *[outcome-label]*
- *Aliases:* RAS (Mira 0.17% of jobs, only system-attributed category), RAS/hardware-fault event, tasks killed by RAS fatal event
- *Sources:* Mira/ALCF, ALCF-Cobalt
- *Why this class:* A job-termination label asserting system responsibility; its causal content is decomposed in the RAS category rows (compute card, kernel panic, MU) already mapped to causal classes.

**Unknown/indeterminate failure**  *[outcome-label]*
- *Aliases:* Unknown (LANL 20-30%, HSDP, Mira, Tsubame-3, HPC1 Misc/Unknown), others (Unicron 3.3%), No signature (Philly), Indeterminate (Oliner I), User/System indeterminate (FRESCO/BlueWaters), SIGTERM ambiguous (user or scheduler), 143/SIGTERM, failures of unknown cause (B200 4/21), unknown software root loci (~20% Tsubame-3), Others (L4 4.7%), NCCL watchdog undetermined (Llama3 Unknown), EW/WT expired watchdogs, RBB, ADDR_ERR, System Crash (beam, untraceable), Undetermined
- *Sources:* LANL, HSDP, Mira, Philly, Oliner, FRESCO, BlueWaters, Unicron, DGX-B200, Tsubame-3, L4, Llama3, Beam-DUE
- *Why this class:* Explicitly unattributed residuals; LANL's 20-30% unknown share is itself a finding the paper should surface — burying these in causal rows would fabricate attribution.

**Coarse multi-class category label (Hardware/Infrastructure/attribution splits)**  *[outcome-label]*
- *Aliases:* Hardware (LANL 30-60%, BlueWaters 42%, Oliner H, CFDR >50%), Infrastructure (Acme category), hardware failures tier, hardware root-cause (~37% Unicron, L4 dominant, HSDP 78%), hardware failures narrative (OPT ~110, GLM dated), hardware faults requiring node drainage, transient faults split (73%), restart-remediable (~73%), R_HDW_BAD, internal/external failures (Desh), exogenous/endogenous (F-DATA), system-caused vs user-caused (BlueWaters 1.53%), System failures (FRESCO coarse), explicit vs implicit/gray vs manual restarts (ByteRobust), immediate crashes bucket, Training crash symptom (L4 57.5%), Application exit status: system/user-system, PNNL MPP2 records (no breakdown)
- *Sources:* LANL, BlueWaters, Oliner, CFDR, Unicron, L4, HSDP, OPT, GLM, Desh, F-DATA, FRESCO, ByteRobust, NVIDIA, MegaScale, PNNL
- *Why this class:* 'Hardware' and 'Infrastructure' span four of our causal classes, so these category totals cannot occupy any single cause row; they are attribution summaries used for cross-study comparison only.

**Node-health/availability anomaly label**  *[outcome-label]*
- *Aliases:* node anomaly label=1 (M100 0.035%), system-wide anomaly (14.4% of period), Nagios host/service state encodings, Label (Marconi binary), Nagios node offline/unavailable, availability vs unavailability intervals (FTA), binary_anom (Prodigy), removed-from-production/drained flag (non-failure), DIM_MACHINE_STATUS
- *Sources:* M100, ExaMon, FTA, Prodigy, ALCF
- *Why this class:* Binary availability proxies conflating crash, maintenance, and churn; the datasets' own authors reject them as fault labels (M100 drained-vs-anomaly analysis).

**Schema/label vocabulary (fields, not failures)**  *[outcome-label]*
- *Aliases:* SWF Status field, TORQUE E record + Exit_status + A/D/E codes, PEARC unified states, Moab JOBEND/JOBFAIL/JOBCANCEL vocabulary, Trinity job_event_state + completion_code, EXIT_STATUS/EXIT_CODE, Cobalt states (exited/killed/dep_fail), ec exit code, ExitCode+State (sacct), state_reason, derived_ec, fail_time/stop_time, exit_signal+err_text, kill_requid, RAS severities DEBUG..FATAL, ERRCODE, CATEGORY/COMPONENT/MSG_ID, RAS_EVENT category list, THETA_HARDWARE_ERROR table, '-' alert tag, Cray severity flags (rejected as unreliable), free-text failure description, failed-component+repair-action fields, COM1 symptom/diagnosis narrative, COM2 repair codes, disk replacement event caveat, Backblaze failure column, event reason codes (disk crash/CPU overheating), event_type component codes, GPU-Failed derived label, DBE-vs-snapshot label, dead/dead_dbe/dead_otb/out labels, GPU XID health-check signals, DRAM CE-logging jitter study, PPENDING/RUNNING censoring, SUSPENDED stray record, status 2-4 partial codes, status -1 unknown, LOST, machine REMOVE/ADD/UPDATE (conflates failure with decommission), site coding artifact (failed vs cancelled convention), missing downtime data, uBGL bring-up outlier, storage-failure missing logs caveat, database storage error data gap, 20-categories row (Philly), Helios/AcmeTrace/MIT-SC taxonomy rows, per-job Slurm exit state rows, PAKDD/DSN'21 outcome-only labels, normal shutdowns (Desh non-failure)
- *Sources:* PWA/SWF, FRESCO, ATLAS, ALCF, F-DATA, PM100, MIT-SC, Intrepid, Mira, Loghub, Desh, CFDR, Backblaze, FTA, Borg, Titan, Summit, Delta, Ampere-mem, SNIA, DKRZ, Helios, Tachyon
- *Why this class:* These mentions describe label vocabularies, schema fields, censoring artifacts, and data-quality caveats — metadata about how failures are recorded, not failure types; mapping them anywhere else would double-count their referents.

**Aggregate failure statistics/observations (non-type rows)**  *[outcome-label]*
- *Aliases:* Job status mix, GPU time wasted by status, failure vs job scale, user-level failure behavior, unsuccessful energy ~50%, unsuccessful umbrella comparisons (Google 1.4-6.8x), runtime skew of failed jobs, failed jobs use more cores, inter-failure Weibull/burstiness, attribution to usage not node, correlated same-state termination, correlated simultaneous multi-node failures (LANL), all-failures aggregate repair, diagnosability split (89.9% log-diagnosable), incident duration, success-rate vs CPU-hours decline, re-submission behavior, short-job failure pattern, recurring-job failures (52.6% from 50+ groups), startup failures (<1 min: 34-45%), node-seconds correlation, overall job failure rate, silent failures believed rare, stall-time inflation post-hoc, XK vs XE comparison, event-log software-vs-hardware view, subsystem MTBI table, indistinguishable candidate causes, other causes named without numbers
- *Sources:* Meta-RSC, Helios, SURF, Tachyon, LANL, ATLAS, PAI, FRESCO, L4, SuperBench, BlueWaters, Oliner, HSDP
- *Why this class:* Statistical findings ABOUT failures (burstiness, cost skew, correlation) rather than failure types; enumerated so no raw mention is dropped, but they populate the paper's findings sections, not the taxonomy matrix.

## Taxonomy verdict (from the classification pass)

The 10-class scheme survives contact with the full list, with ONE structural addition and TWO scope rulings; everything else is boundary-rule tightening, not row surgery. (1) ADD an 11th meta row: "Outcome-labels & unattributed". Roughly a third of the 931 mentions are scheduler terminal states (FAILED/CANCELLED/TIMEOUT/NODE_FAIL/LOST across Slurm, Borg, SWF, TORQUE, Cobalt, SGE), binary failed flags, schema fields, unknowns, or coarse spanning categories ("Hardware", "Infrastructure") that carry zero causal information. Under the v1 scheme these default into user/application (the usual home of FAILED/TIMEOUT) or get scattered, which both inflates the user row and lets coarse traces masquerade as attributed data. Matrix change: add one row; move every pure state/label/unknown/coarse-spanning entry there; each meta entry may carry a dominant-class pointer (e.g., NODE_FAIL→hardware). Cause rows then contain only genuinely attributed types, which is exactly the hygiene the paper's HPC-vs-AI comparison needs since classic HPC traces are label-only while AI-cluster studies attribute. (2) NVLink STAYS in GPU/accelerator hardware — do not move it to network. Grounds: Fire-Flyer root-caused its dominant Xid-74 volume to NVLink Bridge connector hardware; the failure domain is one node/package; remediation is GPU/board replacement, not fabric operations; and Delta/DGX-B200 report it through the GPU Xid channel. Deciding rule stated in the class definition: interconnect repaired by swapping the accelerator = accelerator class; repaired by fabric ops = network. No matrix row change, but add the rule as a footnote so Minder-style taxonomies (which call NVLink a category of its own) map cleanly. (3) KEEP SDC/fail-slow as a class but re-scope it as a MANIFESTATION overlay, not a causal locus. Perseus is decisive: 80% of verified fail-slow drives were software-scheduling-rooted and fixed without touching hardware; MegaScale's MFU decay was GC/time-skew (software); SuperBench's gray failures are hardware. If SDC/fail-slow were a causal row it would be wrong 80% of the time for storage fail-slow. Resolution: entries in this row are symptoms with a mandatory cross-reference; the diagnosed causes (Perseus's I/O-scheduling defect → software/system; bad capacitors → storage; mercurial cores → CPU silicon) live in causal rows. Retain the class because 8+ sources report SDC/fail-slow as an indivisible unit and the paper's fail-slow narrative needs a home; matrix cells in this row should cite the causal row where known. (4) Scheduler/resource-mgmt: no split. Preemption/eviction/requeue are marked outcome-of-policy (non-failure) inside the class; scheduler SOFTWARE bugs (PBS task_check killing ~1,336 jobs, LANL system H) are the row's causal content. Borg EVICT gets the stated recount rule (infra-reason evictions move to their causal class). (5) Rejected changes, for the record: splitting GPU memory vs GPU compute (no source's analysis requires it; Xid families map fine); splitting storage devices from FS software (unified with an explicit boundary rule — FS software is storage — because failure domain and remediation are storage-side, and it keeps Lustre/GPFS/NFS incidents in one row for the HPC-vs-AI comparison); a separate "facility-operations" class for host maintenance (folded into power/facility with a scope note; only 2 sources report it). Net matrix impact: +1 row (meta), 0 renames, 0 merges, boundary footnotes on NVLink, OOM (user-allocation vs overcommit), dataloader (process death=software vs content=data), NCCL timeout (symptom-only, never a cause cell), and preemption (policy, not failure).