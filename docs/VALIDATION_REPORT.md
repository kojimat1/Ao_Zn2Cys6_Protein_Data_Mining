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
| `260721_antiSMASH_area_based_with_reference_set_acl0-1.ipynb` | PASS |
| `260721_antiSMASH_area_based_with_reference_set_afl0-1.ipynb` | PASS |
| `260721_antiSMASH_area_based_with_reference_set_afu0-1.ipynb` | PASS |
| `260721_antiSMASH_area_based_with_reference_set_and0-2.ipynb` | PASS |
| `260721_antiSMASH_area_based_with_reference_set_ang0-2.ipynb` | PASS |
| `260721_antiSMASH_area_based_with_reference_set_atr0-1.ipynb` | PASS |
| `260727_STREME.ipynb` | PASS |
| `260904_AoTF_DBD_Length_histogram_revised.ipynb` | PASS |
| `260922_AoTF_Phylogenetic_Tree_Analysis.ipynb` | PASS |
| `260922_Mantel_test_pairwise_3_trees_Spearman_Holm.ipynb` | PASS |
| `260922_antiSMASH_area_based_bgc_proximity_sensitivity.ipynb` | PASS |
| `260923_AO_TF_PCA.ipynb` | PASS |
| `260925_PCA_sequence_length_effect_analysis.ipynb` | PASS |
| `260925_PCA_threshold_sensitivity_analysis.ipynb` | PASS |
| `261012_AO090005001236_synteny.ipynb` | PASS |
| `SM00066_domain_and_non_DBD_sequence_extraction.ipynb` | PASS |

## Execution limits

During preparation of the repository, the sequence-preparation notebook was executed from the first code cell through the last code cell using the source files available to the authors and completed with exit code 0. The generated full-length FASTA was byte-identical to the reference full-length FASTA used in the study, and the generated DBD sequences matched the reference DBD sequence multiset used in the study.

AO090012000182 is intentionally absent from the general non-DBD output because its DBD occupies residues 582-628 of a 673-aa protein. `scripts/finalize_non_dbd_fasta.py` extracts residues 1-581 for this defined C-terminal-DBD exception, normalizes FASTA headers, and reproduces the fixed non-DBD FASTA used in the study with an identical SHA-256 checksum.

A full clean run was not claimed for notebooks that install external software or invoke Google Colab APIs. Input completeness and workflow dependencies are documented in `MATERIALS_AUDIT.md`.
