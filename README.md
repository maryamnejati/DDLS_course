# KRAS G12D structural-analysis report

Small disk-backed FastAPI product for reading the exact-construct fold and the AlphaFold reference. It serves the PDB/mmCIF files and confidence data without a database.

## Run

```bash
uv run uvicorn app:app --host 127.0.0.1 --port 8000
```

Open http://127.0.0.1:8000

The frontend uses Tailwind CSS and 3Dmol.js from their CDNs. The exact-construct fold is KRAS G12D, residues 1–169, single-chain monomer. The AlphaFold reference is a 189-residue single-chain model containing G12, so it is not an exact sequence match.
