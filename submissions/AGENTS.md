# Operating instructions

## Environment
- Use `uv`: create the environment with `uv venv`.
- Run all Python with `uv run`; this works the same on every OS.

## Data and outputs
- Data lives in `ddls-week4-s3-sequence-mismatch-dataset/data/`.
- `my_construct.fasta` is the assay construct sequence.
- `KRAS_alphafold_model.cif` is the mmCIF coordinate model; load its structure with an mmCIF-capable structure parser. pLDDT is in the B-factor column (`_atom_site.B_iso_or_equiv`).
- `KRAS_alphafold_pae.json` contains PAE; load the JSON and use its `predicted_aligned_error` values.
- Write outputs to `results/`.

## Version control
This folder is a git repository. Commit the current state before any big change, and commit again whenever something starts working, using short, clear messages.

## Course fold service
To fold a protein sequence that isn't in the AlphaFold DB, read https://ddls-structure-api-8a7d6803.svc.hypha.aicell.io/skill.md and follow it. Take the fold key from the `DDLS_FOLD_KEY` variable in `.env` by loading it with `set -a; source .env; set +a`, then send it as the Bearer token. Never write the key itself into `AGENTS.md` or any other committed file.

## Structure-reporting rule
Never report an answer about a structure without first reporting the confidence that matches the claim and confirming that the model is actually this protein. Use per-residue pLDDT for a fold or region claim; use PAE/interface confidence for claims about how parts sit together. Check the model against the assay sequence and assembly before treating it as the protein under study.
