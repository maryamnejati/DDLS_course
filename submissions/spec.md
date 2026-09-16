# KRAS G12D pocket decision specification

## Decision
The owner needs a defensible residue-level pocket map to choose the next inhibitor analogues for Friday: identify what can reach Asp12, which residues line the adjacent switch-II-side groove, and how to gain G12D selectivity rather than make another generic KRAS binder.

## Protein and assembly
The protein used in the assay is KRAS G12D, residues 1–169, a single-chain protein and not a multiprotein complex. It is the assay construct, not full-length KRAS. The supplied structure is predicted, not experimental: an AlphaFold database model of KRAS with one chain and 189 residues, containing glycine at position 12 and a C-terminal tail absent from the assay construct. It is therefore a structural reference, not the exact assay protein.

## Supplied files
- `ddls-week4-s3-sequence-mismatch-dataset/data/my_construct.fasta`: FASTA sequence for the owner's G12D assay construct, residues 1–169.
- `ddls-week4-s3-sequence-mismatch-dataset/data/KRAS_alphafold_model.cif`: AlphaFold mmCIF coordinates for the 189-residue, single-chain KRAS reference model. The CIF's atom B-factor column contains pLDDT.
- `ddls-week4-s3-sequence-mismatch-dataset/data/KRAS_alphafold_pae.json`: JSON positional confidence file containing predicted aligned error (PAE), used for confidence in how regions or interfaces sit together.

## Exact claim and residues
The owner's claim is that the analysis should support substituent decisions for the actual G12D, 1–169 assay construct: determine which residues surround the nucleotide site and adjacent inhibitor groove, especially what can contact the mutated Asp12 and what may provide selectivity. The relevant starting regions are the P-loop/glycine-rich loop (approximately residues 10–17), switch I (30–38), and switch II (59–76). The nucleotide site binds GDP or GTP with Mg²⁺ and phosphate contacts concentrated around the P-loop and switch regions. Do not present a pocket list from the 189-residue glycine-at-12 model as a pocket read for the G12D assay protein.

## Matching confidence to the claim
- For a fold or local pocket/region claim, report per-residue pLDDT from the mmCIF B-factor column.
- For a claim about how domains or parts sit together, report PAE/interface confidence from the JSON.
- The PAE file cannot turn the 189-residue wild-type-like model into the 169-residue G12D construct. No experimental structure for the owner's construct is supplied.

## Sequence and assembly checks
Before using coordinates for the owner's claim, verify chain count and residue coverage, compare the FASTA sequence with the model sequence, confirm the model has glycine at position 12 while the assay sequence has Asp12, and restrict assay interpretation to residues 1–169. Account for the model's extra residues 170–189 and tail. Confirm the single-chain assembly; do not infer a multiprotein complex from the model. A model/sequence mismatch or wrong residue numbering invalidates an unqualified assay-pocket claim.

## Done
Done means a defensible pocket map explicitly tied to KRAS G12D residues 1–169, listing residues around the nucleotide site and adjacent inhibitor groove, with confidence appropriate to each claim and clear suggestions for contacting Asp12 or gaining selectivity. It must distinguish the physical pocket observed in the longer AlphaFold reference from the actual assay construct, and flag that experimental comparison to a KRAS G12D structure and purified-protein binding/activity measurements would be needed to validate the design decision.
