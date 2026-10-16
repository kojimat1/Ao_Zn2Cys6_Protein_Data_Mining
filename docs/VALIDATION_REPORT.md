# Validation report

Validation performed on the GitHub-ready copy. Notebook outputs were cleared; analytical code, parameters, and calculations were retained.

## Checks performed

- Parsed every notebook as valid JSON.
- Parsed Python code cells after excluding Colab/shell magic lines.
- Scanned notebook source for Japanese characters.
- Audited required inputs separately in `MATERIALS_AUDIT.md`.

## Notebook results

| Notebook | Python syntax |
|---|---|
| `260727_STREME.ipynb` | PASS |
| `260904_AoTF_DBD_Length_histogram_revised.ipynb` | PASS |
| `260922_AoTF_Phylogenetic_Tree_Analysis.ipynb` | PASS |
| `260922_antiSMASH_area_based_bgc_proximity_sensitivity.ipynb` | PASS |
| `260923_AO_TF_PCA.ipynb` | PASS |
| `260925_PCA_sequence_length_effect_analysis.ipynb` | PASS |
| `260925_PCA_threshold_sensitivity_analysis.ipynb` | PASS |
| `261012_AO090005001236_synteny.ipynb` | PASS |
| `SM00066_domain_and_non_DBD_sequence_extraction.ipynb` | PASS |

## Execution limits

The sequence-preparation notebook was executed from the first code cell through the last code cell with the deposited source files and completed with exit code 0. It produced 234 DBD sequences, 232 sequences under the general non-DBD rule, and 233 full-length sequences, with no missing FASTA IDs, invalid coordinates, or sequence-length mismatches. The generated full-length FASTA was byte-identical to the deposited full-length FASTA, and the generated DBD sequences matched the deposited DBD sequence multiset.

AO090012000182 is intentionally absent from the general non-DBD output because its DBD occupies residues 582-628 of a 673-aa protein. `scripts/finalize_non_dbd_fasta.py` extracts residues 1-581 for this defined C-terminal-DBD exception, normalizes FASTA headers, and reproduced the deposited fixed non-DBD FASTA with an identical SHA-256 checksum.

A full clean run was not claimed for notebooks that install external software or invoke Google Colab APIs. Input completeness and workflow dependencies are documented in `MATERIALS_AUDIT.md`.
