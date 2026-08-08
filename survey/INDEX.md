# Index of all 148 surveyed datasets and operational reports

Every entry the survey examined, grouped by what its evidence can support.
Full descriptions (organization, scale, contents, access, caveats) are in
[`dataset_catalog.md`](dataset_catalog.md); the verdict rationale per entry is in
[`ledger.md`](ledger.md) and [`ledger.csv`](ledger.csv).


## Cause-attributed — publishes failure shares with cause attribution (19)

| Dataset / report | System | Access | Link |
|---|---|---|---|
| Acme LLM cluster trace (Shanghai AI Lab / AcmeTrace) | Acme (Seren + Kalos, Shanghai AI Lab) | public | [source](https://github.com/InternLM/AcmeTrace) |
| AcmeTrace — utilization + failure/RAS subset (Acme traces, Seren & Kalos) | Acme (Shanghai AI Lab, Seren+Kalos) | public | [source](https://huggingface.co/datasets/Qinghao/AcmeTrace) |
| ALCF Cobalt workload + RAS traces (IIT / Zhiling Lan) | ANL Intrepid + Mira (ALCF Cobalt) | public (with citation) |  |
| Blue Gene/P Intrepid RAS + Job Logs (Intrepid RAS log dataset) | ALCF Intrepid (Blue Gene/P) | public (USENIX CFDR, Intrepid_RAS_0901_0908_scrubbed) | [source](https://www.usenix.org/cfdr-data) |
| Blue Gene/Q Mira RAS Logs (5-Year Failure Record / LogAider dataset) | Mira | public (ALCF reports portal + LogAider repo) | [source](https://reports.alcf.anl.gov/data/mira.html) |
| Blue Waters K20X GPU error records (Blue Waters Kepler GPU failure data) | Blue Waters | restricted / on-request (findings via papers only) | [source](https://bluewaters.ncsa.illinois.edu/hardware-summary) |
| Fire-Flyer 2 AI-HPC Xid Error Characterization (DeepSeek) | DeepSeek Fire-Flyer 2 | paper-only (public paper, no data repository) | [source](https://arxiv.org/abs/2408.14158) |
| From Detection to Recovery: Operational Analysis on LLM Pre-training with 504 GPUs | Lablup/Upstage DGX B200 cluster | on-request (paper public, data via lablup.com contact) | [source](https://arxiv.org/abs/2605.09370) |
| LANL failure data (22 HPC systems, 1996-2005) | LANL 22-system fleet | public (USENIX CFDR / CMU PDL; LA-UR-05-7318) | [source](https://www.usenix.org/cfdr-data) |
| LANL Trinity trace (ATLAS repository) | LANL Trinity (ATLAS scheduler trace) | public | [source](https://www.pdl.cmu.edu/ATLAS/) |
| Llama 3 405B Pre-training Interruption Breakdown (Herd of Models, Table 5) | Meta Llama 3 405B H100 cluster | paper-only (public paper, no data artifact) | [source](https://arxiv.org/abs/2407.21783) |
| MegaScale / ByteRobust — ByteDance large-scale GPU LLM-training failure statistics | ByteDance production GPU fleet (MegaScale/ByteRobust) | paper-only (papers public, no raw data released) | [source](https://arxiv.org/abs/2402.15627) |
| Meta ML Research Cluster Reliability Data ("Revisiting Reliability in Large-Scale Machine Learning Research Clusters", arXiv:2410.21680) | Meta RSC (RSC-1 + RSC-2) | paper-only (no data download) | [source](https://arxiv.org/abs/2410.21680) |
| Microsoft Philly Trace (philly-traces) | Microsoft Philly | public (trace CC-BY-4.0; cause taxonomy paper-only) | [source](https://github.com/msr-fiddle/philly-traces) |
| Mira 2K-day Multi-Source Job Failure Logs (RAS + Cobalt + Task-Execution + Darshan I/O) | Mira | public | [source](https://reports.alcf.anl.gov/data/mira.html) |
| NERSC I/O Failure Database (CFDR NERSC / Remedy trouble-ticket data) | NERSC fleet 2001-2006 | on-request (CFDR / contact NERSC PDSI researchers; companion report public) | [source](https://www.usenix.org/cfdr-data) |
| NVIDIA DGX Cloud Reliability Data (Nemotron training runs) | NVIDIA DGX Cloud (Nemotron, H100) | public blog, no dataset download | [source](https://developer.nvidia.com/blog/ensuring-reliable-model-training-on-nvidia-dgx-cloud/) |
| Story of Two GPUs: Characterizing the Resilience of Hopper H100 and Ampere A100 GPUs (Delta GPU resilience artifact) | NCSA Delta (A100 + H100) | public (Zenodo 10.5281/zenodo.15287639, CC-BY-4.0) | [source](https://doi.org/10.5281/zenodo.15287639) |
| USRC Failure/Interrupt Data 1996-2005 (LA-UR-05-7318) | LANL 22 anonymized systems | public | [source](https://usrc.lanl.gov/data/failure-data.php) |

## Outcome-label only — per-job exit states, no cause (25)

| Dataset / report | System | Access | Link |
|---|---|---|---|
| Alibaba cluster-trace-v2017 | Alibaba colocation cluster (v2017) | public | [source](https://github.com/alibaba/clusterdata/tree/master/cluster-trace-v2017) |
| Alibaba cluster-trace-v2018 | Alibaba colocation cluster (v2018) | public | [source](https://github.com/alibaba/clusterdata) |
| Alibaba GPU Cluster Trace 2020 (cluster-trace-gpu-v2020) | Alibaba PAI | public | [source](https://github.com/alibaba/clusterdata/tree/master/cluster-trace-gpu-v2020) |
| Alibaba PAI GPU cluster trace (cluster-trace-gpu-v2020) | Alibaba PAI | public | [source](https://github.com/alibaba/clusterdata/tree/master/cluster-trace-gpu-v2020) |
| DKRZ Mistral Slurm job-history dataset | DKRZ Mistral | unverified ('see paper') |  |
| F-DATA: A Fugaku Workload Dataset for Job-centric Predictive Modelling in HPC Systems | Fugaku (RIKEN R-CCS) | public | [source](https://zenodo.org/records/11467483) |
| FRESCO Job Failure & Performance Data Repository | Purdue Conte + TACC Stampede + Purdue Anvil (FRESCO) | public | [source](https://www.datadepot.rcac.purdue.edu/sbagchi/fresco/) |
| Google Borg Cluster Trace 2011 (clusterdata-2011-2) | Google Borg 2011 cell | public | [source](https://github.com/google/cluster-data/blob/master/ClusterData2011_2.md) |
| Google Borg cluster trace 2019 (clusterdata-2019) | Google Borg 2019 (8 cells) | public | [source](https://github.com/google/cluster-data/blob/master/ClusterData2019.md) |
| Grid Workloads Archive (GWA) | TU Delft GWA grids (DAS-2, Grid'5000, NorduGrid, AuverGrid, LCG, Grid3, TeraGrid, SharcNet + Bitbrains/Materna cloud) | public | [source](http://gwa.ewi.tudelft.nl/datasets/) |
| Helios GPU Cluster Traces (HeliosData) | SenseTime Helios (Venus/Earth/Saturn/Uranus) | public | [source](https://github.com/S-Lab-System-Group/HeliosData) |
| IN2P3 Computing Center 2024 Workload Dataset | IN2P3 Computing Center | public |  |
| LANL Mustang cluster trace (ATLAS) | LANL Mustang | public | [source](https://www.pdl.cmu.edu/ATLAS/) |
| LAST — Lassen job/energy dataset (LLNL) | LLNL Lassen | public-but-verify (possibly on-request) |  |
| NREL Eagle HPC Jobs | NREL Eagle | public |  |
| NREL Kestrel HPC Jobs | NREL Kestrel | public |  |
| Parallel Workloads Archive (PWA) | PWA aggregate (~40 SWF logs) | public | [source](https://www.cs.huji.ac.il/labs/parallel/workload/) |
| PM100: A Job Power Consumption Dataset of a Large-scale Production HPC System | Marconi100 (CINECA) | public | [source](https://zenodo.org/records/10127767) |
| Polaris public job-history logs (ALCF Public Data Catalog) | ALCF Polaris | public | [source](https://reports.alcf.anl.gov/data/polaris.html) |
| SenseTime Helios GPU Trace (HeliosData) | SenseTime Helios | public (GitHub, CC-BY-4.0) | [source](https://github.com/S-Lab-System-Group/HeliosData) |
| SURF Lisa "Generic and ML Workloads in an HPC Datacenter" | SURF Lisa | public |  |
| Tachyon HPC job failure log (KISTI Tachyon-II scheduler job records) | Tachyon (KISTI Tachyon2) | on-request | [source](https://doi.org/10.1007/s11227-023-05482-y) |
| The MIT Supercloud Dataset | MIT Supercloud (TX-Green/LLSC) | public | [source](https://registry.opendata.aws/dcc/) |
| Theta job + Darshan I/O logs (ALCF) | Theta | public | [source](https://reports.alcf.anl.gov/data/) |
| Two Sigma cluster trace (via CMU ATLAS) | Two Sigma (CMU ATLAS) | public |  |

## Rates only — event rates or MTBF, no share breakdown (37)

| Dataset / report | System | Access | Link |
|---|---|---|---|
| A Large-Scale Study of Soft-Errors on GPUs in the Field (Nie et al., HPCA 2016) | Titan | restricted / on-request (ORNL-internal logs; paper public) | [source](https://www.researchgate.net/publication/299641571) |
| Alibaba 2023 GPU cluster trace (cluster-trace-gpu-v2023) + HPN link/switch failure statistics | Alibaba PAI (v2023 trace) + Alibaba HPN network | public | [source](https://github.com/alibaba/clusterdata/tree/master/cluster-trace-gpu-v2023) |
| Alibaba SSD SMART logs (dcbrain) | Alibaba SSD fleet (dcbrain) | public |  |
| Backblaze Drive Stats (Hard Drive Test Data / SMART dataset) | Backblaze cloud-storage fleet (component-level HDD/SSD) | public | [source](https://www.backblaze.com/cloud-storage/resources/hard-drive-test-data) |
| BLOOM / BigScience training chronicles (176B) | Jean Zay (BLOOM 176B run) | public |  |
| COM1 (CFDR COM1) — Commercial disk hardware failure/repair log | Anonymous ISP disk fleet (CFDR umbrella) | on-request (not openly downloadable via CFDR) | [source](https://www.usenix.org/cfdr-data) |
| COM2 (CFDR COM2 warranty service hardware-replacement log) | anonymous ISP server fleet (CFDR umbrella) | public (USENIX CFDR) | [source](https://www.usenix.org/cfdr-data) |
| COM3 (CFDR COM3 disk replacement data) | Anonymous ISP FC storage (CFDR umbrella) | paper-only (CFDR lists it but no download) | [source](https://www.usenix.org/cfdr-data) |
| Cray XT logs (syslog / event log / console log) | anonymous Cray XT (CFDR umbrella) | public (direct USENIX tarballs) | [source](https://www.usenix.org/cfdr-data) |
| Dataset of SSD Failures in Alibaba (Tianchi / FAST'21) | Alibaba SSD fleet (Tianchi/FAST'21; distinct ~1M-SSD fleet cut from dcbrain) | public (Tianchi registration) |  |
| ExaMon / Marconi monitoring framework data (Examon data from Marconi HPC system snapshot) | CINECA Marconi (NOT Marconi100) | public | [source](https://zenodo.org/record/4537850) |
| Experimental Findings on the Sources of Detected Unrecoverable Errors in GPUs | Lab neutron-beam GPUs (Kepler/Volta, ISIS ChipIR) — not a production cluster | public (paper only, no raw beam-data repository) | [source](https://arxiv.org/abs/2108.00554) |
| FTA — Condor pools (UW-Madison) & Notre Dame desktop-grid availability traces | UW-Madison Condor pools + Notre Dame desktops (FTA subset) | gone | [source](http://fta.scem.uws.edu.au) |
| FTA — Failure Trace Archive (non-HPC subsets: lri05, deug05, pl05, websites02, ldns04, overnet03, microsoft99) | Commodity/internet-scale systems (desktop grids, PlanetLab, DNS, P2P, web) | public (primary site intermittently down; download pages 403/404 at check time) | [source](http://fta.scem.westernsydney.edu.au) |
| FTA — Grid'5000 availability trace (g5k06) | Grid'5000 | on-request/gone (FTA mirrors dead) | [source](http://fta.scem.uws.edu.au/index.php?n=Main.DataSets) |
| FTA — SETI@home host availability trace | SETI@home volunteer desktop grid (FTA) | gone (FTA host connection refused as of 2026-07; may need Wayback/curators) | [source](http://fta.scem.uws.edu.au/index.php?n=Main.DataSets) |
| GLM-130B training logs (Tsinghua / Zhipu) | Tsinghua/Zhipu GLM-130B cluster | public |  |
| GPU Lifetimes on Titan Supercomputer: Survival Analysis and Reliability | Titan | public | [source](https://doi.org/10.13139/ORNLNCCS/1657202) |
| HPC1 (CFDR HPC1) hardware replacement log | PSC 765-node cluster (CFDR umbrella) | on-request (CFDR registration/DUA) | [source](https://www.usenix.org/cfdr-data) |
| HPC2 disk replacement data (CFDR) | LANL 256-node cluster (CFDR umbrella) | public (CFDR) | [source](https://www.usenix.org/cfdr-data) |
| HPC3 data (CFDR) | Anonymized 1,532-node HPC cluster (CFDR umbrella) | on-request (CFDR request process) | [source](https://www.usenix.org/cfdr-data) |
| HPC4 / Sandia-USENIX Five-System Supercomputer Logs (Oliner-Stearley DSN'07) | Sandia/LLNL five-system logs (BGL, Thunderbird, RedStorm, Spirit, Liberty) | public via loghub/Zenodo (BGL/Thunderbird/Spirit); RedStorm/Liberty via broken CFDR | [source](https://www.usenix.org/cfdr-data) |
| Imbue 70B "from bare metal" report | Imbue 4,092x H100 / 511-host cluster | public |  |
| Large-scale Disk Failure Prediction Dataset (Tianchi / PAKDD 2020 Alibaba AIOps) | Alibaba HDD fleet (PAKDD 2020) | public (Tianchi registration) |  |
| LLM360 (Amber / CrystalCoder / K2) | LLM360 open training runs | public |  |
| M100 dataset: time-aggregated data for anomaly detection | Marconi100 (CINECA) | public | [source](https://zenodo.org/records/7541722) |
| M100 ExaData (Marconi100 ExaData) | Marconi100 (CINECA) | public | [source](https://doi.org/10.1038/s41597-023-02174-3) |
| Machine Learning Models for GPU Error Prediction (Titan) — Nie et al. 2018 SBE telemetry | Titan | paper-only (trace restricted) | [source](https://www.osti.gov/biblio/1462859) |
| Minder (ByteDance) | ByteDance Ampere training clusters | paper-only |  |
| OLCF Summit Supercomputer GPU Snapshots During Double-Bit Errors and Normal Operations | Summit | public/on-request via OLCF DOI 10.13139/OLCF/1970187 | [source](https://doi.org/10.13139/OLCF/1970187) |
| OPT-175B Training Logbook (Meta OPT Chronicles / metaseq logbook) | Meta OPT-175B A100 cluster | public (GitHub, MIT license) | [source](https://github.com/facebookresearch/metaseq/tree/main/projects/OPT/chronicles) |
| PNNL MPP2 Hardware Failure Log (CFDR) | PNNL MPP2 (EMSL HPCS-2) | public (USENIX CFDR) | [source](https://www.usenix.org/cfdr-data) |
| SNIA Reliability Traces: Alibaba NVMe Fail-Slow & Fail-Stop | Alibaba NVMe fleet (via SNIA IOTTA) | public |  |
| TPUv4 Resiliency at Scale (Google) | Google TPUv4 pods | paper-only |  |
| Understanding GPU Errors on Large-Scale HPC Systems (Titan GPU field data) | Titan | paper-only (raw logs restricted) | [source](https://impact.ornl.gov/en/publications/understanding-gpu-errors-on-large-scale-hpc-systems-and-the-impli/) |
| Understanding the Landscape of Ampere GPU Memory Errors (Zhu et al. 2025) | Delta + Polaris + Perlmutter A100 fleets | paper-only (arXiv:2508.03513) | [source](https://arxiv.org/abs/2508.03513) |
| USRC System 20 (MX20) Usage & Node Internal-Disk Failure Data | LANL System 20 (part of the LANL 1996-2005 collection) | public | [source](https://usrc.lanl.gov/data/failure-data.php) |

## Paper statistics only — usable numbers, no released dataset (8)

| Dataset / report | System | Access | Link |
|---|---|---|---|
| Blue Waters Failure & Error Logs (LogDiver dataset / NCSA Blue Waters resiliency data) | Blue Waters | paper-only (NCSA-internal) |  |
| Desh / Doomsday Cray XC RAS & Console System Log Corpus (Das & Mueller, NCSU) | anonymized Cray XC SC1/SC2/SC3 (DOE sites) | paper-only (site-owned, anonymized) | [source](https://dl.acm.org/doi/10.1145/3208040.3208051) |
| Fault-Tolerant HSDP at 100,000 GPUs (Meta) | Meta ~32K-GPU HSDP job | paper-only |  |
| From Detection to Recovery (504x B200 cluster) | Lablup/SKT/NVIDIA Korea B200 cluster | paper-only |  |
| L4 (Microsoft "Platform-X") | Microsoft Platform-X | paper-only |  |
| OPT-175B Training Logbook / Chronicles (OPT175B_Logbook.pdf; metaseq OPT chronicles) | Meta OPT-175B A100 cluster (992 GPUs) | public (archived metaseq GitHub PDFs) | [source](https://github.com/facebookresearch/metaseq/tree/main/projects/OPT/chronicles) |
| SuperBench (Microsoft Azure A100 fleet) | Microsoft Azure A100 fleet | paper-only |  |
| Unicron (Alibaba) | Alibaba production LLM clusters (Unicron) | paper-only |  |

## Umbrella repository — members carry their own verdicts (6)

| Dataset / report | System | Access | Link |
|---|---|---|---|
| ALCF Public Data Catalog (Argonne Leadership Computing Facility Data Catalog) | ALCF facility umbrella (Intrepid/Mira/Cooley/Theta/ThetaGPU/Polaris/Aurora) | public | [source](https://reports.alcf.anl.gov/data/) |
| ALCF Public Data reports (Mira/Theta job + I/O + RAS summaries) | ALCF portal (Mira + Theta umbrella) | public | [source](https://reports.alcf.anl.gov/data/) |
| Atlas Cluster Trace Repository (CMU PDL ATLAS) — LANL Mustang + Trinity HPC scheduler traces | CMU PDL ATLAS umbrella (Mustang, Trinity, Two Sigma) | public | [source](https://ftp.pdl.cmu.edu/pub/datasets/ATLAS/) |
| Computer Failure Data Repository (CFDR) | CFDR umbrella | public (usenix.org/cfdr-data; 403 to bots) | [source](https://www.usenix.org/cfdr-data) |
| Failure Trace Archive (FTA) | FTA umbrella (26 systems, 1994-2009) | gone | [source](http://fta.scem.uws.edu.au/) |
| SNIA IOTTA Trace Repository (incl. Reliability sub-collection) | SNIA IOTTA umbrella | public (click-through license) |  |

## No failure information — telemetry, I/O, power, or synthetic only (35)

| Dataset / report | System | Access | Link |
|---|---|---|---|
| Adastra MI250 power dataset (CINES/GENCI) | Adastra (CINES) | public |  |
| ALBADross Eclipse Active-Learning Anomaly-Diagnosis Dataset (HPAS-injected LDMS telemetry) | Sandia Eclipse (+Volta testbed) | on-request | [source](https://www.osti.gov/servlets/purl/2004257) |
| ALCF I/O Data Repository (Darshan logs) | ALCF Mira/Theta Darshan | public | [source](https://ftp.mcs.anl.gov/pub/darshan/data/) |
| ALCF Polaris Darshan Log Collection | ALCF Polaris (Darshan) | public | [source](https://wordpress.cels.anl.gov/darshan/data/) |
| ALCF Public Data reports portal (Theta & Polaris) | ALCF Theta / Polaris | public | [source](https://reports.alcf.anl.gov/data/) |
| ALCF Theta Darshan Summary Reports (ANL-ALCF-DARSHAN-THETA) | Theta | public | [source](https://reports.alcf.anl.gov/data/index.html) |
| Antarex HPC Fault Dataset (FINJ-generated) | Antarex single node (ETH Zurich) | public | [source](https://zenodo.org/record/2553224) |
| April 2020 Darshan counters from the Summit supercomputer | OLCF Summit | public | [source](https://doi.org/10.13139/OLCF/1865904) |
| darshan-hpc/darshan-logs example log repository (PyDarshan example logs) | Mixed systems (curated Darshan test corpus) | public | [source](https://github.com/darshan-hpc/darshan-logs) |
| Dataset Artifact for Prodigy: Towards Unsupervised Anomaly Detection in Production HPC Systems | Sandia Eclipse | public | [source](https://doi.org/10.5281/zenodo.8079388) |
| DKRZ "Mistral" job I/O dataset (Betke & Kunkel) | DKRZ Mistral | papers open; raw repo unreachable — likely contact authors |  |
| E2EWatch Eclipse Telemetry / Anomaly-Diagnosis Dataset (Aksar et al.) | Sandia Eclipse | on-request | [source](https://www.osti.gov/servlets/purl/1873069) |
| Frontier Energy / Waste-Heat Dataset (OLCF) | Frontier | public |  |
| HPAS (HPC Performance Anomaly Suite) | tool (used on Voltrino/Eclipse/Cori/Volta) | public | [source](https://github.com/peaclab/HPAS) |
| HPC-ODA Dataset Collection | LRZ CooLMUC / SuperMUC-class | public | [source](https://zenodo.org/record/3701440) |
| I/O Burst Prediction Darshan dataset (Blue Waters + Mira + Theta) | Blue Waters + Mira + Theta (Darshan corpora) | on-request (Blue Waters via Globus) / public (ALCF portal); no combined release | [source](https://bluewaters.ncsa.illinois.edu/data-sets.html) |
| I/O Traces of HPC Applications (Frontera / Zenodo) | TACC Frontera | public (CC-BY-4.0) |  |
| Long Term Per-Component Power and Thermal Measurements of the OLCF Summit System | OLCF Summit | public | [source](https://www.osti.gov/dataexplorer/biblio/dataset/1861393) |
| NCSA Blue Waters Darshan I/O Logs (Blue Waters System Monitoring Data Set — Darshan component) | Blue Waters | on-request (Globus, Blue Waters Monitoring collection) | [source](https://bluewaters.ncsa.illinois.edu/data-sets) |
| Perlmutter LDMS/DCGM System Telemetry (NERSC, Performance Monitoring API) | NERSC Perlmutter | on-request | [source](https://sc25.supercomputing.org/proceedings/posters/poster_files/post270s2-file3.pdf) |
| Perlmutter System-wide GPU Telemetry Dataset (Characterizing Production GPU Workloads) | NERSC Perlmutter | on-request | [source](https://arxiv.org/abs/2502.18680) |
| Proctor / Voltrino Performance Anomaly Dataset (peaclab) | Sandia Voltrino (+ NERSC Cori) | on-request | [source](https://github.com/peaclab/Proctor) |
| RoWD (Rogue Workload Detector) framework — releases the SCRIPT-AI dataset | Fugaku | on-request (paper paywalled; SCRIPT-AI release location unconfirmed) |  |
| Sandia Eclipse LDMS Operational Telemetry (BU PeacLab / SNL anomaly-diagnosis dataset) | Sandia Eclipse (+Volta) | on-request | [source](https://www.osti.gov/servlets/purl/1) |
| Smaller AI silent-data-corruption studies | various (LLM-PRISM, llm-sdc-training, ACL 2025 SDC, Anatomy of SDC) | mixed (mostly paper-only; one public artifact) |  |
| Taxonomist Application Detection Artifact (BU/Sandia Volta LDMS dataset) | Sandia Volta (Cray XC30m) | public | [source](https://springernature.figshare.com/articles/dataset/Artifact_for_Taxonomist_Application_Detection_through_Rich_Monitoring_Data/6384248) |
| Taxonomist dataset (Artifact for Taxonomist: Application Detection through Rich Monitoring Data) | Sandia Volta/Voltrino (Cray XC30m) | public | [source](https://springernature.figshare.com/articles/dataset/Artifact_for_Taxonomist_Application_Detection_through_Rich_Monitoring_Data/6384248) |
| Theta + Cori Darshan I/O Throughput Dataset (Isakov et al.) | Theta + Cori | on-request (curated subsets unpublished; underlying logs partly public) | [source](https://zenodo.org/records/6476501) |
| TOKIO / pytokio + NERSC Cori Darshan+LMT corpus | NERSC Cori | code public; archives largely on-request |  |
| Trinity Open Science Environmental Sensor Data (SEDC) | LANL Trinity | public | [source](https://usrc.lanl.gov/data/operational-data.php) |
| USRC Memory Usage Statistics from Open Clusters (LA-UR-19-28211) | LANL Grizzly/Badger/Snow | public | [source](https://usrc.lanl.gov/data/LA-UR-19-28211.php) |
| USRC parallel-filesystem fsstats (anon-pfs 1-9) | LANL anonymized parallel filesystems | public | [source](https://usrc.lanl.gov/data/storage-data.php) |
| USRC VPIC restart/checkpoint particle files (LANL operational VPIC dataset) | VPIC simulation output (LANL) | public |  |
| USRC Workstation Filesystem Statistics & Archive/NFS Metadata (LANL) | LANL workstations + archive/NFS filesystems | public | [source](https://usrc.lanl.gov/data/storage-data.php) |
| USRC/CFDR LANL Systems 8/15/16/23 Node Usage Traces (MX8/MX15/MX16/MX23) | LANL 22-system / CFDR umbrella (usage companions) | public | [source](https://usrc.lanl.gov/data/failure-data.php) |

## Duplicate — same artifact as another entry (18)

| Dataset / report | System | Access | Link |
|---|---|---|---|
| AcmeTrace (Seren + Kalos cluster traces) | Acme (Seren + Kalos, Shanghai AI Lab) | public | [source](https://github.com/InternLM/AcmeTrace) |
| ALCF I/O Data Repository (Mira Darshan Log Collection) | ALCF Mira/Theta Darshan | public | [source](https://www.alcf.anl.gov/publications/alcf-io-data-repository) |
| ALCF Mira Darshan I/O Logs (ALCF I/O Data Repository) | ALCF Mira/Theta Darshan | public | [source](https://wordpress.cels.anl.gov/darshan/data/) |
| Alibaba GPU cluster trace 2023 (cluster-trace-gpu-v2023) | Alibaba PAI | public | [source](https://github.com/alibaba/clusterdata/tree/master/cluster-trace-gpu-v2023) |
| Alibaba GPU Cluster Traces (cluster-trace-gpu-v2020 / v2023 / alibaba-lingjun-dataset-2023) | Alibaba PAI (+ Lingjun) | public | [source](https://github.com/alibaba/clusterdata/tree/master/cluster-trace-gpu-v2020) |
| Argonne Leadership Computing Facility DATA CATALOG | ALCF fleet (Aurora/Polaris/Theta/ThetaGPU/Mira/Cooley/Intrepid) | on-request (IEEE DataPort subscription) | [source](https://ieee-dataport.org/documents/argonne-leadership-computing-facility-data-catalog) |
| Blue Gene/P Intrepid RAS Log (CFDR) | ALCF Intrepid (Blue Gene/P) | public | [source](https://www.usenix.org/cfdr-data) |
| Google Borg Cluster Traces (clusterdata-2011-1 / ClusterData2019) | Google Borg 2011 + 2019 | public | [source](https://github.com/google/cluster-data) |
| LANL HPC Failure Data (Schroeder & Gibson / CFDR LA-UR node-outage logs) | LANL 22-system fleet | public | [source](https://www.usenix.org/cfdr-data) |
| Llama 3 405B Pre-training Reliability Breakdown (Interruption Root-Cause Table) | Meta Llama 3 405B H100 cluster | paper-only | [source](https://arxiv.org/abs/2407.21783) |
| Loghub HPC RAS log collection (BGL, Thunderbird, Liberty, Spirit) | Sandia/LLNL five-system logs (Loghub redistribution) | public (Zenodo 8196385) | [source](https://github.com/logpai/loghub) |
| Loghub Sandia/LLNL Supercomputer System Logs (BGL, Thunderbird, Spirit, Liberty) | Sandia/LLNL five-system logs (Loghub redistribution) | public (Zenodo 8196385) | [source](https://zenodo.org/records/8196385) |
| MegaScale production failure narrative (NSDI'24 fault-tolerance / robustness section) | ByteDance production GPU fleet (MegaScale/ByteRobust) | paper-only | [source](https://www.usenix.org/system/files/nsdi24-jiang-ziheng.pdf) |
| Nie et al. Titan GPU error trace (DSN 2018) — related public release: "GPU Lifetimes on Titan" (TitanGPULife) | Titan | split: TitanGPULife public, 6-mo trace restricted | [source](https://par.nsf.gov/servlets/purl/10065578) |
| Philly Trace (Microsoft Philly GPU cluster trace) | Microsoft Philly | public | [source](https://github.com/msr-fiddle/philly-traces) |
| Prodigy Eclipse Dataset (Dataset Artifact for Prodigy) | Sandia Eclipse | public | [source](https://zenodo.org/records/8079388) |
| Revisiting Reliability in Large-Scale Machine Learning Research Clusters (Meta RSC-1 / RSC-2) | Meta RSC (RSC-1 + RSC-2) | paper-only | [source](https://arxiv.org/abs/2410.21680) |
| Titan GPU Failure / Lifetime Data (ORNL Titan K20X DBE/OTB dataset) | Titan | public | [source](https://github.com/olcf/TitanGPULife) |

---

**Total: 148 entries.**

