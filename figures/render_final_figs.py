#!/usr/bin/env python3
"""FINAL poster figures to the verified typography spec (rework/TYPOGRAPHY_SPEC.md)
+ Bangalore 7/30 feedback: color legends (colorbars), ~2x fonts, less dead space.
Durable script (replaces earlier inline heredocs). Outputs figA/figB/figC *_final.png/pdf."""
import csv, re
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mp
from matplotlib.colors import LinearSegmentedColormap

HERE = Path(__file__).parent
F = 1.0  # fonts below are ABSOLUTE printed points; canvases match poster placement size

ROWS = ["GPU/accelerator hardware","CPU/host memory/PCIe","network/interconnect",
 "storage/filesystem","power/facility","software/system","user/application",
 "data/input","SDC/fail-slow","scheduler/resource-mgmt","Outcome-labels & unattributed"]
SH = {'Conte-FRESCO-A':'Conte','UIUC-Cray-FRESCO-B':'UIUC Cray','MIT-Supercloud':'MIT SC',
 'Llama3-405B':'Llama-3 405B','Alibaba-Unicron':'Unicron','Platform-X-L4':'Platform-X',
 'Meta-HSDP-100k':'Meta HSDP','DGX-B200':'DGX/B200','SuperBench-Azure':'SuperBench',
 'Minder-ByteDance':'Minder','Intrepid-RAS':'Intrepid','NERSC-Seaborg':'Seaborg',
 'DKRZ-Mistral':'Mistral','BlueWaters':'Blue Waters','LANL-Mustang':'Mustang',
 'LANL-Trinity':'Trinity','Alibaba-PAI':'Alibaba PAI','PWA-aggregate':'PWA (16 logs)',
 'NREL-Eagle':'Eagle','NREL-Kestrel':'Kestrel','LLNL-Lassen':'Lassen','SURF-Lisa':'SURF Lisa',
 'Nemotron-DGX-Cloud':'Nemotron'}
HPCset={"LANL-22sys","BlueWaters","Titan","Mira","TSUBAME-2","TSUBAME-3","Frontier","Tachyon",
 "Fugaku","Marconi100","SURF-Lisa","Conte-FRESCO-A","UIUC-Cray-FRESCO-B","NREL-Eagle","NREL-Kestrel",
 "MIT-Supercloud","PWA-aggregate","Delta-A100-H100","Intrepid-RAS","NERSC-Seaborg","LANL-Mustang",
 "LANL-Trinity","IN2P3","LLNL-Lassen","DKRZ-Mistral"}
AIset={"Philly","Helios","Alibaba-PAI","Acme","Meta-RSC","Llama3-405B","Alibaba-Unicron",
 "Platform-X-L4","Meta-HSDP-100k","Fire-Flyer","DGX-B200","SuperBench-Azure","ByteRobust",
 "Minder-ByteDance","Nemotron-DGX-Cloud"}
cmap = LinearSegmentedColormap.from_list("sb", ["#eef3fa","#c4d6ee","#7ea8d8","#3d6fb4","#16386e"])
cmap.set_bad("#f2f0ed")

def load(path):
    rows=list(csv.reader(open(path)))
    hdr=rows[0][1:]; d={}
    for r in rows[1:]:
        for j,c in enumerate(r[1:]):
            if c.strip(): d[(r[0],hdr[j])]=c.strip()
    return hdr,d

def val(s):
    m=re.match(r'^([<~]?)([\d.]+)',s); return float(m.group(2)) if m else np.nan
def mark(s):
    return re.sub(r'[\d.]','',s)

hdr,dc = load(HERE.parent/'matrices'/'matrix_count_v3.csv')

# ---------------- FIG A: cause-attributed heat map + colorbar ----------------
cause_rows = ROWS[:10]
cols = [c for c in hdr if any((r,c) in dc for r in cause_rows)]
cols = [c for c in cols if c in HPCset] + [c for c in cols if c in AIset] + \
       [c for c in cols if c not in HPCset and c not in AIset]
M = np.full((len(cause_rows), len(cols)), np.nan); MK={}
for i,r in enumerate(cause_rows):
    for j,c in enumerate(cols):
        s=dc.get((r,c))
        if s: M[i,j]=val(s); MK[(i,j)]=mark(s)
fig,ax = plt.subplots(figsize=(23.0, 12.1), dpi=300)
im = ax.imshow(np.ma.masked_invalid(M), cmap=cmap, vmin=0, vmax=100, aspect="auto")
for i in range(len(cause_rows)):
    for j in range(len(cols)):
        v=M[i,j]
        if np.isnan(v): continue
        t=("0" if v==0 else f"{v:.2f}" if v<0.1 else f"{v:.1f}" if v<10 else f"{v:.0f}")+MK.get((i,j),'')
        ax.text(j,i,t,ha='center',va='center',fontsize=14,
                color="#ffffff" if v>55 else "#1a1a1a")
ax.set_xticks(np.arange(-0.5,len(cols)),minor=True); ax.set_yticks(np.arange(-0.5,len(cause_rows)),minor=True)
ax.grid(which='minor',color='white',linewidth=1.2); ax.tick_params(which='minor',length=0)
ax.set_xticks(range(len(cols)))
ax.set_xticklabels([SH.get(c,c) for c in cols], rotation=45, ha='right', fontsize=19)
ax.set_yticks(range(len(cause_rows)))
ax.set_yticklabels([r.replace('/',' / ') for r in cause_rows], fontsize=21)
for s in ax.spines.values(): s.set_visible(False)
nh=sum(1 for c in cols if c in HPCset)
ax.axvline(nh-0.5,color='#1a1a1a',linewidth=1.6)
ax.text((nh-1)/2,-0.85,'Traditional HPC',ha='center',fontsize=20,fontweight='bold')
ax.text(nh+(len(cols)-nh-1)/2,-0.85,'AI training',ha='center',fontsize=20,fontweight='bold')
cb = fig.colorbar(im, ax=ax, fraction=0.028, pad=0.012)
cb.set_label("share of that cluster's failures (%)", fontsize=17)
cb.ax.tick_params(labelsize=16); cb.outline.set_visible(False)
fig.tight_layout()
fig.savefig(HERE/'figA_causes_final.png', bbox_inches='tight')
fig.savefig(HERE/'figA_causes_final.pdf', bbox_inches='tight'); plt.close(fig)

# ---------------- FIG B: label-only bars (fonts up) ----------------
labels=[]
for c in hdr:
    s=dc.get((ROWS[10],c))
    if s and not any((r,c) in dc for r in cause_rows): labels.append((c,val(s),s))
labels.sort(key=lambda x:x[1])
fig,ax=plt.subplots(figsize=(10.8,9.8),dpi=300)
groups={**{c:'#3d6fb4' for c in HPCset},**{c:'#b4643d' for c in AIset}}
colors=[groups.get(c,'#6e6e6e') for c,_,_ in labels]
ax.barh(range(len(labels)),[v for _,v,_ in labels],color=colors,height=0.62)
for i,(c,v,s) in enumerate(labels):
    ax.text(v+0.4,i,s,va='center',fontsize=17,color='#1a1a1a')
ax.set_yticks(range(len(labels)))
ax.set_yticklabels([SH.get(c,c) for c,_,_ in labels],fontsize=20)
ax.set_xlabel("failed / unsuccessful share of jobs (%), scheduler label only",fontsize=17)
ax.tick_params(axis='x',labelsize=16)
ax.legend(handles=[mp.Patch(color='#3d6fb4',label='HPC'),mp.Patch(color='#b4643d',label='AI'),
                   mp.Patch(color='#6e6e6e',label='Cloud')],fontsize=14,loc='lower right',frameon=False)
for s in ('top','right'): ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig(HERE/'figB_labels_final.png',bbox_inches='tight')
fig.savefig(HERE/'figB_labels_final.pdf',bbox_inches='tight'); plt.close(fig)

# ---------------- FIG C: GPU error classes + colorbar ----------------
GROWS=["Uncorrectable memory (DBE/HBM)","Correctable memory (SBE/remap)","MMU / illegal access  [mostly app bugs]",
"GSP / driver","NVLink","Off-bus / device lost (Xid79)","PCIe / interface","Thermal / power","SDC (silent)",
"Generic GPU (no subclass)","Other named"]
GCOLS=[("Blue Waters\nK20X","logged\nevents",{0:(0.009,'~'),2:(36.8,'~'),3:(21.1,'~'),5:(41.9,'~'),10:(0.12,'~')}),
 ("TSUBAME-2\nK20X","all failures",{9:(44.4,'')}),
 ("TSUBAME-3\nP100","all failures",{3:(21.6,'~'),9:(27.8,'')}),
 ("Delta\nA100","critical\nXids",{0:(0.17,''),1:(0.45,'<'),2:(59.8,''),3:(26.0,''),4:(13.0,''),5:(0.07,''),7:(0.52,'')}),
 ("Ampere 3-sys\nA100/A40","ECC events",{0:(0.8,'<'),1:(99.2,'')}),
 ("Fire-Flyer\nA100 PCIe","raw Xids",{0:(0.25,''),1:(1.9,''),2:(53.0,''),3:(0.01,''),4:(42.6,''),5:(0.29,''),10:(2.0,'')}),
 ("Acme\nA100","failed-job\nGPU-time",{0:(11.0,''),4:(30.3,''),9:(15.8,'')}),
 ("Meta RSC\nA100","lemon nodes",{6:(15.4,''),9:(28.2,'')}),
 ("SuperBench\nA100","defective\nnodes",{1:(3.37,''),4:(0.30,''),6:(2.03,'')}),
 ("Delta\nH100","critical\nXids",{0:(3.19,''),1:(1.26,'<'),2:(95.4,''),3:(0.16,''),4:(0,''),5:(0,''),7:(0,'')}),
 ("Llama-3\nH100","interruptions",{0:(17.2,''),3:(4.1,''),5:(30.1,''),7:(1.4,''),8:(1.4,''),10:(4.5,'')}),
 ("DGX B200","17 failures",{0:(11.8,''),3:(5.9,''),4:(29.4,''),5:(11.8,''),10:(41.2,'')}),
]
n_r,n_c=len(GROWS),len(GCOLS)
V=np.full((n_r,n_c),np.nan); VM={}
for j,(_,_,cells) in enumerate(GCOLS):
    for i,(v,m) in cells.items(): V[i,j]=v; VM[(i,j)]=m
C=np.full_like(V,np.nan)
for j in range(n_c):
    col=V[:,j]; mx=np.nanmax(col) if not np.all(np.isnan(col)) else 1
    C[:,j]=col/mx*100 if mx>0 else col
fig,ax=plt.subplots(figsize=(23.0,11.3),dpi=300)
im=ax.imshow(np.ma.masked_invalid(C),cmap=cmap,vmin=0,vmax=100,aspect="auto")
for i in range(n_r):
    for j in range(n_c):
        v=V[i,j]
        if np.isnan(v): continue
        t=("0" if v==0 else f"{v:.2f}" if v<0.1 else f"{v:.1f}" if v<10 else f"{v:.0f}")+VM.get((i,j),'')
        ax.text(j,i,t,ha='center',va='center',fontsize=14,
                color="#ffffff" if (C[i,j] if not np.isnan(C[i,j]) else 0)>55 else "#1a1a1a")
ax.set_xticks(np.arange(-0.5,n_c),minor=True); ax.set_yticks(np.arange(-0.5,n_r),minor=True)
ax.grid(which='minor',color='white',linewidth=1.3); ax.tick_params(which='minor',length=0)
ax.set_xticks(range(n_c))
ax.set_xticklabels([f"{l}\n[{d}]" for l,d,_ in GCOLS],fontsize=14.5)
ax.set_yticks(range(n_r)); ax.set_yticklabels(GROWS,fontsize=21)
for s in ax.spines.values(): s.set_visible(False)
for x,lab,ctr in ((1.5,'K20X era',0.5),(2.5,'P100',2),(8.5,'A100 era',5.5),(10.5,'H100',9.5),(None,'B200',11)):
    if x is not None: ax.axvline(x,color='#1a1a1a',linewidth=1.6)
    ax.text(ctr,-0.85,lab,ha='center',fontsize=20,fontweight='bold')
cb=fig.colorbar(im,ax=ax,fraction=0.028,pad=0.012)
cb.set_label("share, normalized within each column (%)",fontsize=17)
cb.ax.tick_params(labelsize=16); cb.outline.set_visible(False)
fig.tight_layout()
fig.savefig(HERE/'figC_gpu_errors_final.png',bbox_inches='tight')
fig.savefig(HERE/'figC_gpu_errors_final.pdf',bbox_inches='tight'); plt.close(fig)
print("final figures rendered: figA/figB/figC *_final")
