from pathlib import Path
import json
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse

ROOT = Path(__file__).parent
RESULTS = ROOT / "results"
DATA = ROOT / "ddls-week4-s3-sequence-mismatch-dataset" / "data"
app = FastAPI(title="KRAS G12D structural analysis")


def fold_data():
    return json.loads((RESULTS / "actual_construct_fold.json").read_text())


def load_results():
    fold = fold_data()
    af_pae = json.loads((DATA / "KRAS_alphafold_pae.json").read_text())
    return {
        "construct": {"name": "Course fold: KRAS G12D residues 1–169", "pdb": "/structures/course-fold.pdb", "plddt": fold["plddt"], "pae": fold["pae"], "mean_plddt": fold["mean_plddt"], "ptm": fold["ptm"], "length": 169, "residue": "D12", "sequence": "".join(line.strip() for line in (DATA / "my_construct.fasta").read_text().splitlines() if not line.startswith(">"))},
        "alphafold": {"name": "AlphaFold reference: single chain, 189 residues", "pdb": "/structures/alphafold.pdb", "cif": "/structures/alphafold.cif", "pae": af_pae[0], "length": 189, "residue": "G12", "sequence": ""},
    }

@app.get("/", response_class=HTMLResponse)
def index(): return HTMLResponse(INDEX)

@app.get("/api/results")
def results(): return load_results()

@app.get("/structures/{name}")
def structure(name: str):
    files = {"course-fold.pdb": RESULTS / "actual_construct_fold.pdb", "alphafold.pdb": RESULTS / "alphafold_reference.pdb", "alphafold.cif": DATA / "KRAS_alphafold_model.cif"}
    path = files.get(name)
    if not path or not path.exists(): raise HTTPException(404, "Structure not found")
    return FileResponse(path)

INDEX = r'''<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>KRAS G12D structure report</title><script src="https://cdn.tailwindcss.com"></script><script src="https://3Dmol.org/build/3Dmol-min.js"></script></head><body class="bg-slate-50 text-slate-900"><main class="max-w-7xl mx-auto p-5"><header class="mb-6"><p class="text-sm font-semibold text-indigo-700">STRUCTURAL ANALYSIS REPORT</p><h1 class="text-3xl font-bold mt-1">KRAS G12D: what this model can support</h1></header><section class="bg-white rounded-xl shadow-sm p-5 mb-5"><h2 class="font-bold text-lg">Structure check</h2><p class="mt-2">Owner’s construct: <b>D12, 169 residues, monomer</b>. AlphaFold reference: <b>G12, 189 residues, monomer</b> — sequence does not match the owner’s construct.</p></section><section class="bg-white rounded-xl shadow-sm p-5 mb-5"><h2 class="font-bold text-lg">Headline answer</h2><p class="mt-2">The exact 169-residue, single-chain KRAS G12D fold supports the overall KRAS architecture, but switch-region confidence is not sufficient for confident residue-level inhibitor or selectivity decisions.</p></section><div class="flex flex-wrap gap-2 mb-4"><button id="constructBtn" class="px-4 py-2 rounded-lg bg-indigo-700 text-white">Exact G12D fold</button><button id="afBtn" class="px-4 py-2 rounded-lg bg-white border">AlphaFold reference</button><span class="border-l mx-1"></span><button id="plddtBtn" type="button" onclick="setColorMode('plddt')" class="px-3 py-2 rounded-lg bg-slate-800 text-white text-sm">pLDDT coloring</button><button id="trustBtn" type="button" onclick="setColorMode('trust')" class="px-3 py-2 rounded-lg bg-white border text-sm">Trust coloring</button><span id="colorLegend" class="hidden"></span></div><section class="space-y-5"><div class="bg-white rounded-xl shadow-sm overflow-hidden"><div class="p-4 border-b"><h2 class="font-bold">3D structure</h2></div><div class="max-w-3xl mx-auto p-4"><div id="viewer" class="h-[560px] flex items-center justify-center"></div></div></div><div class="space-y-5"><div class="bg-white rounded-xl shadow-sm overflow-hidden"><div id="sequenceBar" class="overflow-x-auto bg-slate-100 px-3 py-3"></div><div class="px-4 pb-4 text-xs text-slate-500">Hover or click a residue in the sequence. Clicking a residue in the structure selects the matching letter. Click elsewhere to clear the selection.</div></div><div class="bg-white rounded-xl shadow-sm p-4"><h2 class="font-bold text-sm mb-3">Color mode</h2><div class="flex flex-wrap gap-2"><button id="plddtBtn" type="button" onclick="setColorMode('plddt')" class="px-3 py-2 rounded-lg bg-slate-800 text-white text-sm">pLDDT coloring</button><button id="trustBtn" type="button" onclick="setColorMode('trust')" class="px-3 py-2 rounded-lg bg-white border text-sm">Trust coloring</button></div><div id="colorLegend" class="mt-3"></div></div><div><div class="bg-white rounded-xl shadow-sm p-4"><h2 class="font-bold">Confidence panel</h2><canvas id="chart" class="w-full h-64 mt-3"></canvas><p id="metrics" class="text-sm mt-2"></p></div><div class="bg-amber-50 border border-amber-200 rounded-xl p-4"><h2 class="font-bold flex items-center gap-2"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 9v4m0 4h.01"/><path d="M10.3 3.8 2.5 17a2 2 0 0 0 1.7 3h15.6a2 2 0 0 0 1.7-3L13.7 3.8a2 2 0 0 0-3.4 0Z"/></svg>The trap</h2><p class="text-sm mt-2">Do not treat the mismatched 189-residue G12 AlphaFold reference—or low-confidence switch II—as a validated G12D pocket map.</p></div></div></section></main><script>
let data,current='construct',viewer,selected=null,seq='';
window.addEventListener('error',e=>{document.getElementById('colorLegend').textContent='UI error: '+e.message;});
const regions={construct:[[10,17],[30,38],[59,76]],alphafold:[[10,17],[30,38],[59,76]]};
function color(v){let stops=['#30123b','#466be3','#21d3a4','#a8e25b','#fee333','#f98e09','#d7191c'];let x=Math.max(0,Math.min(100,v))/100*6,i=Math.min(5,Math.floor(x)),f=x-i,a=stops[i],b=stops[i+1],h=n=>parseInt(n,16);return '#'+[1,3,5].map(q=>Math.round(h(a.slice(q,q+2))+(h(b.slice(q,q+2))-h(a.slice(q,q+2)))*f).toString(16).padStart(2,'0')).join('')}
let colorMode='plddt';
function displayColor(v){if(colorMode==='trust')return v>=70?'#16a34a':v>=50?'#f59e0b':'#dc2626';return color(v)}
function updateLegend(){document.getElementById('colorLegend').innerHTML=colorMode==='trust'?'<span class="inline-flex items-center gap-3 text-xs"><span class="inline-flex items-center gap-1"><i class="inline-block w-4 h-4 bg-green-600 rounded-sm"></i>Trust (≥ 70 pLDDT score)</span><span class="inline-flex items-center gap-1"><i class="inline-block w-4 h-4 bg-amber-400 rounded-sm"></i>Caution (50–70 pLDDT score)</span><span class="inline-flex items-center gap-1"><i class="inline-block w-4 h-4 bg-red-600 rounded-sm"></i>Don\'t trust (&lt; 50 pLDDT score)</span></span>':'<span class="text-xs text-slate-600">pLDDT coloring active</span>'}
function setColorMode(mode){colorMode=mode;updateLegend();if(window.plddtBtn){plddtBtn.className='px-3 py-2 rounded-lg '+(mode==='plddt'?'bg-slate-800 text-white':'bg-white border')+' text-sm';trustBtn.className='px-3 py-2 rounded-lg '+(mode==='trust'?'bg-slate-800 text-white':'bg-white border')+' text-sm'}if(viewer){resetStyles();draw(data[current])}}
function residueStyle(i,highlight=false){let d=data[current], v=d.plddt?.[i-1]??70;return highlight?{cartoon:{color:'#111827',thickness:1.5},stick:{color:'#111827',radius:.28}}:{cartoon:{color:displayColor(v)}}}
function resetStyles(){let d=data[current];for(let i=1;i<=d.length;i++)viewer.setStyle({resi:i},residueStyle(i,i===selected));if(current==='construct')viewer.setStyle({resi:12},{cartoon:{color:displayColor(d.plddt[11])},stick:{color:displayColor(d.plddt[11]),radius:.22}});viewer.render()}
function select(i){selected=i;document.querySelectorAll('.residue-letter').forEach((e,n)=>e.classList.toggle('ring-2',n===i-1));resetStyles()}
function clearSelection(){selected=null;document.querySelectorAll('.residue-letter').forEach(e=>e.classList.remove('ring-2'));resetStyles()}
function drawSequence(){let bar=document.getElementById('sequenceBar');bar.innerHTML='';seq=data[current].sequence||'';for(let i=0;i<seq.length;i++){let b=document.createElement('button');b.className='residue-letter inline-flex items-center justify-center w-5 h-7 text-xs font-mono text-slate-600 hover:bg-slate-300 rounded '+(i===11?'text-red-600 font-bold':'');b.textContent=seq[i];b.title=`${seq[i]}${i+1}`;b.onclick=e=>{e.stopPropagation();select(i+1)};b.onmouseenter=()=>{if(!selected)select(i+1)};bar.appendChild(b)}}
async function load(which){current=which;selected=null;let d=data[which];document.getElementById('viewer').innerHTML='';viewer=$3Dmol.createViewer(document.getElementById('viewer'),{backgroundColor:'white'});let pdb=await (await fetch(d.pdb)).text();viewer.addModel(pdb,'pdb');resetStyles();viewer.setClickable({},true,(atom)=>select(atom.resi));viewer.zoomTo();viewer.render();drawSequence();draw(d)}
function draw(d){let c=document.getElementById('chart'),x=c.getContext('2d'),w=c.width=c.clientWidth*2,h=c.height=256*2;x.scale(2,2);w/=2;h/=2;let vals=d.plddt||Array(d.length).fill(70),bw=w/vals.length;x.clearRect(0,0,w,h);vals.forEach((v,i)=>{x.fillStyle=displayColor(v);x.fillRect(i*bw,h-(v/100)*(h-25),Math.max(1,bw),v/100*(h-25))});let m=vals.length===169?`Mean pLDDT: ${d.mean_plddt}; P-loop 10–17: min 80.13 / mean 86.94; Switch I 30–38: min 62.00 / mean 68.27; Switch II 59–76: min 45.12 / mean 67.26`:'AlphaFold pLDDT is shown per residue; this model is G12, not G12D.';document.getElementById('metrics').textContent=m}
document.addEventListener('click',e=>{if(!e.target.closest('#viewer')&&!e.target.closest('#sequenceBar'))clearSelection()});(async()=>{data=await (await fetch('/api/results')).json();load('construct')})();constructBtn.onclick=()=>load('construct');afBtn.onclick=()=>load('alphafold');setColorMode(colorMode);</script></body></html>'''
''