# DDLS 2026 — Week 4 interview transcript

**Lab:** Interview a Structural-Biology Data Owner
**Data owner:** Dr. Yuki Tanaka — Medicinal chemist / drug-discovery researcher
**Student:** Maryam Nejati <maryam.nejati@scilifelab.se>
**Exported:** 2026-09-16T12:27:34+00:00

> This is the record of your interview with the data owner. Hand it to your analyst agent as the raw source for `AGENTS.md` and `spec.md`.

---

**You**:

Hi! tell me about your project. please tell me the protein and walk me through the protein structure

**Dr. Yuki Tanaka**:

I’m Dr Yuki Tanaka at Uppsala, working on a small-molecule inhibitor for KRAS—specifically the harder G12D programme. I have the AlphaFold KRAS structure, my assay protein’s sequence, and the bundled confidence file. I want the pocket read properly: where the nucleotide sits, how the glycine-rich loop and switch regions shape the groove, and which residues my hit series can grab. Do you want the basic KRAS architecture first, or should we go straight to the pocket around position 12?

**You**:

both basic KRAS architecture and the pocket are interesting. tell me about both and what the pocket binds

**Dr. Yuki Tanaka**:

KRAS is a small GTPase: a compact catalytic domain with a short C-terminal tail that helps anchor it at the membrane. The active domain is organised around the **P-loop/glycine-rich loop** at the N-terminus, **switch I**, and **switch II**; those switches move between GDP- and GTP-bound states and control effector binding.

The central pocket binds **GDP or GTP**, with magnesium and phosphate contacts concentrated around the P-loop and switch regions. For inhibitors, the useful chemistry is usually an adjacent groove beside the nucleotide site—around position 12 and the switch-II side—where a compound can exploit the mutant residue and lock the protein in an inactive state. For G12D, the new aspartate is charged, so polarity and electrostatics matter much more than in the G12C compounds. Do you want the pocket described as contacts for designing substituents, or as the biological GDP/GTP site?

**You**:

which residues are in this pocket? and how many residues the protein has? is it one chain protein or a complex?

**Dr. Yuki Tanaka**:

KRAS is a **single-chain protein**, not a multiprotein complex; the nucleotide and Mg²⁺ sit in the active site. The downloaded structure contains **189 residues**.

For the pocket, start with the **P-loop around residues 10–17**, **switch I around 30–38**, and **switch II around 59–76**; those form the nucleotide site and the adjacent inhibitor groove. Position 12 is in the P-loop, so G12D directly changes the chemistry there. Do you want the residue list from the downloaded structure, or specifically for the protein used in your assay?

**You**:

do you have any experimental structure from the protein as well? and have you done any experiments on the mutant protein or just the wild type protein?

**Dr. Yuki Tanaka**:

No experimental structure from our protein—we only have the downloaded AlphaFold model. Our assays are on **G12D KRAS**, residues **1–169**, not the plain glycine-at-12 protein; that is the construct behind the inhibitor programme. The model is 189 residues, so don’t treat its tail as part of the assay protein. Do you want the pocket read restricted to residues 1–169?

**You**:

what will the analysis of the pocket affect in your next decisions and what's the goal of the analysis?

**Dr. Yuki Tanaka**:

It determines which substituents we make next: what can reach **Asp12**, which residues line the adjacent groove, and whether we can gain G12D selectivity rather than making another generic KRAS binder. The goal is a residue-level pocket map for the **G12D, 1–169 assay construct**, so Friday’s team chooses the right analogues—not chemistry aimed at the wrong 189-residue model or at G12C. Do you want the analysis to prioritise direct Asp12 contacts, or broader pocket occupancy and selectivity?

**You**:

why do you trust the model you have?

**Dr. Yuki Tanaka**:

Because KRAS has a well-established GTPase fold, and the downloaded model shows the expected P-loop and switch-region architecture. But I don’t treat a computer-generated structure as proof of the exact inhibitor pose—especially around a charged **Asp12**; that’s where the chemistry has to be tested. Do you want a practical pocket read from it, or a decision on whether it’s sufficient for Friday’s design meeting?

**You**:

what are the files you're handing to me as the data? could you explain what they are and their format?

**Dr. Yuki Tanaka**:

Three files:

- **`KRAS_alphafold_model.cif`** — the protein coordinates in **mmCIF** format: atoms, residues, chain information, and the folded model.
- **`my_construct.fasta`** — the assay protein sequence in **FASTA** format, one-letter amino-acid code.
- **`KRAS_alphafold_pae.json`** — a **JSON** file containing the model’s positional confidence information.

The CIF is the one to read the physical pocket from; the FASTA tells you what protein we actually use. Do you want the pocket read from the coordinates or the sequence checked first?

**You**:

did you get the .cif file from alfafold? do you have a good per residue pLDDT in the pocket region?

**Dr. Yuki Tanaka**:

Yes—the **`.cif` came from the AlphaFold database**, bundled with the JSON confidence file. I haven’t inspected the individual pocket confidence values; that’s your side of the analysis, not mine. The relevant question is whether the P-loop and switch-region coordinates are reliable enough to guide substituent design—can you read that from the JSON?

**You**:

is the fasta and the 3d structure the full length protein?

**Dr. Yuki Tanaka**:

No. The **FASTA is the assay construct, residues 1–169**, with the floppy C-terminal tail removed. The **mmCIF model is 189 residues** and includes that tail, so it is longer than the protein we actually test.

**You**:

so you want the residues that line the nucleotide pocket in your G12D construct, to aim an inhibitor at, and you analysed only 1-169 residues for the alfafold structure. and the residues in alfafold structure that you got are the mutated ones, is that right?

**Dr. Yuki Tanaka**:

No—two corrections. **My assay construct is G12D and spans residues 1–169**, but the AlphaFold mmCIF is a **189-residue KRAS model with glycine at position 12**, not the G12D sequence; I have not analysed a 1–169 subset of it yet. So the pocket read from that model would need to be interpreted as a structural reference, not as the exact G12D construct.

**You**:

what does "the project is done" look like for you? and what makes you say that the analysis is not correct at the first glance?

**Dr. Yuki Tanaka**:

“Done” means I have a defensible pocket map for **the actual assay protein: KRAS G12D, residues 1–169**—the residues surrounding the nucleotide site and adjacent inhibitor groove, with clear suggestions for where the next analogues should contact Asp12 or gain selectivity. It should support the Friday design decision, not merely describe a generic KRAS fold.

I call the first read incorrect because the supplied model is **189 residues and has glycine at position 12**, whereas our tested protein is **169 residues and has Asp12**. The model may still show the general KRAS architecture, but a pocket list taken from it without that distinction is not a pocket read for our compound-testing protein. Can you separate the model’s physical pocket from the 1–169 G12D construct when you report it?

**You**:

ok, thank you

**Dr. Yuki Tanaka**:

Fine. For Friday, keep the report tied to **G12D, residues 1–169**, and label the 189-residue AlphaFold coordinates as a reference rather than the assay protein. The key chemistry is the environment around Asp12 and the adjacent switch-region groove.

**You**:

is there anything else that I haven't asked and you want me to know?

**You**:

is there anything else that I haven't asked and you want me to know?

**Dr. Yuki Tanaka**:

Yes: **the PAE/JSON file cannot make the 189-residue model become the 169-residue G12D assay protein**, and we have no experimental structure for that construct. Use the model for the broad KRAS fold and pocket geometry, but keep residue calls tied to the actual G12D sequence before choosing compounds.

**You**:

ok, thank you

**Dr. Yuki Tanaka**:

Right. The useful deliverable is the **G12D 1–169 pocket map**, with the longer AlphaFold model clearly treated as reference only.

**You**:

Is there any experimental check I could check against?

**Dr. Yuki Tanaka**:

Yes. Compare the coordinates against an **experimentally solved KRAS G12D structure**—ideally GDP- or GTP-bound, and preferably inhibitor-bound—checking the P-loop, switch I/II, and the environment around Asp12. For the actual 1–169 protein, confirm the pocket experimentally with purified-protein binding or activity measurements; a structure from wild-type KRAS is only a fold-level comparison, not proof of the G12D pocket. Do you have access to a structural database, or are you limited to your own assay data?
