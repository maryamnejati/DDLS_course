# KRAS G12D structural-analysis report

## The answer first

Do not choose inhibitor analogues from the supplied AlphaFold pocket as though it were the owner’s KRAS G12D structure. The exact 169-residue, single-chain course fold supports the overall KRAS architecture, but its switch regions are not confident enough for residue-level G12D selectivity decisions. The owner should use this result to prioritize validation—not to claim which substituent will contact Asp12. The medicinal-chemistry team acts on that distinction.

## The question

The owner needs a defensible structural starting point for choosing the next inhibitor analogues: which parts of KRAS can be trusted around the nucleotide site and adjacent switch-II groove, and which contacts might support G12D selectivity? The answer should change whether the team advances a pocket hypothesis now or first obtains a better mutant/complex model.

## The protein & the files

The assay protein is KRAS G12D, residues 1–169, as a single-chain monomer. The owner supplied `my_construct.fasta`, the 169-residue assay sequence, and an AlphaFold mmCIF structure, `KRAS_alphafold_model.cif`, with one chain and 189 residues. The mmCIF B-factor field contains per-residue pLDDT. The supplied PAE file is `KRAS_alphafold_pae.json`.

I also folded the exact owner sequence through the course service and saved the response as `results/actual_construct_fold.json` and `results/actual_construct_fold.pdb`. That fold has one chain, 169 residues, mean pLDDT 85.45, and pTM 0.9034. These are predicted structures, not experimental structures. The main limitation is that neither prediction establishes the ligand-bound conformation or proves a G12D-selective pocket.

## The right confidence, stated plainly

For a fold or local-region claim, the governing confidence is per-residue pLDDT—not the global score alone. In the exact-construct fold:

- **P-loop, residues 10–17:** minimum **80.13**, mean **86.94**. This is a comparatively strong local fold signal.
- **Switch I, residues 30–38:** minimum **62.00**, mean **68.27**. This is mixed and should not be treated as a fixed side-chain template.
- **Switch II, residues 59–76:** minimum **45.12**, mean **67.26**. The minimum is very low; the mean is not sufficient for confident pocket-shape or selectivity claims. The within-region PAE also reaches **20.89 Å**, reinforcing that the switch-II arrangement is uncertain.
- **Context, residues 80–120:** minimum **75.12**, mean **89.18**. This is substantially more reliable than the switches.

The app’s pLDDT track shows the same pattern: a stronger P-loop and folded core, with an amber/low-confidence dip across the switch regions. The global mean and pTM therefore support the existence of a KRAS-like fold, not a precise inhibitor-binding geometry.

## The structure check

The supplied AlphaFold reference is **one chain and 189 residues**, with **Gly12**. The owner’s FASTA is **one chain and 169 residues**, with **Asp12 (G12D)**. Positions 1–169 otherwise match in the sequence comparison; the AlphaFold model contains 20 additional C-terminal residues absent from the assay construct.

That means the AlphaFold model is not the owner’s construct. It is a longer, glycine-at-12 reference and must not be presented as a residue-level readout of the G12D assay protein. The course fold was run on the exact 169-residue G12D sequence, so it is the appropriate model for the owner’s construct identity. Both are monomeric, matching the supplied assay description; there is no basis here to call either model a functional dimer or multiprotein assembly.

## The trap and the honest truth

The biggest trap is reading a confident-looking pocket from the wrong structure: the 189-residue AlphaFold model is **G12, not G12D**, and it includes a 20-residue tail that is not in the assay construct. I tested this rather than assuming identity: I counted chains and residues, compared the model sequence with the FASTA, and checked residue 12 directly. The result is unambiguous.

The uncomfortable truth is that the exact-construct fold does not rescue a confident residue-level selectivity story. It gives a plausible KRAS architecture, but Switch I and especially Switch II are too uncertain for claims such as “this analogue will contact Asp12” or “these residues define a fixed switch-II selectivity groove.” A polished viewer cannot add information that the prediction does not contain.

## The answer / recommendation

Use the exact-construct course fold for broad architecture and for cautious placement of the high-confidence core. The P-loop is the strongest owner-relevant region in this model: residues 10–17 have min/mean pLDDT 80.13/86.94. The 80–120 context is also relatively well supported at 75.12/89.18.

Do **not** use the current fold to rank substituents by predicted Asp12 contact, infer a fixed switch-II pocket, or make a G12D-selectivity claim. Switch I is only moderate, and Switch II is the limiting region: 45.12 minimum pLDDT, 67.26 mean, and 20.89 Å maximum within-region PAE. Trust the global fold and the high-confidence core at moderate confidence; trust residue-level pocket and selectivity conclusions at low confidence.

The actionable next step is to predict or model the actual G12D construct in the relevant nucleotide/ligand state, then evaluate the ligand-bound interface with interface-appropriate confidence. If the decision must be made before that, treat any analogue choice as a hypothesis for testing, not as a structure-supported design conclusion.

## Caveats & next steps

The mai caveat is that although the pLDDT score of the D12 position is high, this score for other moieties around the pocket (G60, Q61) is very low in the mutated protein. As a result, a high confidence structure for the pocket could not be infered through this analysis. The biological caveat is that KRAS switch regions are conformationally mobile and ligand/nucleotide state can change the pocket. A monomeric apo-like prediction cannot establish the functional or ligand-bound assembly.

Next I would: (1) generate multiple predictions of the exact 1–169 G12D construct with the relevant nucleotide state; (2) predict a proper ligand-bound complex and inspect interface confidence rather than only pLDDT; (3) compare states or experimentally determined KRAS G12D structures if available; and (4) test the resulting contacts with purified-protein binding and activity measurements. An experimental structure of the actual construct/complex would be the strongest validation.

## AI-use disclosure

The coding agent prepared the disk-backed FastAPI/Tailwind viewer, converted and served the structure files, generated the pLDDT visualizations, and drafted this report from the analysis outputs and transcript. I verified the key structural facts against the files and outputs: chain count, lengths, residue 12 identity, sequence coverage, pLDDT region statistics, and the saved exact-construct fold. The attached project transcript records the model comparison, exact-sequence fold, visualisation work, and app changes; it should be read alongside `spec.md`, `results/actual_construct_fold.json`, the PDB/mmCIF files, and the app viewer.
