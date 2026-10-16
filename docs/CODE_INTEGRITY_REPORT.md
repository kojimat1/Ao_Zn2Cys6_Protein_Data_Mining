# Code integrity report

The original and GitHub-ready notebooks were compared cell by cell. Python abstract syntax trees were compared after replacing string literals with a neutral placeholder; comments are absent from the syntax tree. This confirms that control flow, function calls, operators, identifiers, and numeric parameters were retained while allowing English translations of comments, docstrings, and user-facing messages. Colab shell cells were excluded from AST comparison and inspected separately.

| Original | GitHub-ready copy | Result | Detail |
|---|---|---|---|
| `260727_STREME.ipynb` | `260727_STREME.ipynb` | PASS | 4 Python cells compared |
| `260904_AoTF_DBD_Length_histogram_revised.ipynb` | `260904_AoTF_DBD_Length_histogram_revised.ipynb` | PASS | 7 Python cells compared |
| `260922_AoTF_Phylogenetic_Tree_Analysis.ipynb` | `260922_AoTF_Phylogenetic_Tree_Analysis.ipynb` | PASS | 17 Python cells compared |
| `260922_antiSMASH_area_based_bgc_proximity_sensitivity.ipynb` | `260922_antiSMASH_area_based_bgc_proximity_sensitivity.ipynb` | PASS | 8 Python cells compared |
| `260923_AO_TF_PCA.ipynb` | `260923_AO_TF_PCA.ipynb` | PASS | 11 Python cells compared |
| `260925_PCA_sequence_length_effect_analysis.ipynb` | `260925_PCA_sequence_length_effect_analysis.ipynb` | PASS | 8 Python cells compared |
| `260925_PCA_threshold_sensitivity_analysis.ipynb` | `260925_PCA_threshold_sensitivity_analysis.ipynb` | PASS | 8 Python cells compared |
| `261012_AO090005001236_synteny.ipynb` | `261012_AO090005001236_synteny.ipynb` | PASS | 3 Python cells compared |
| `SM00066_ドメイン領域抽出_non_DBD_extraction_追加.ipynb` | `SM00066_domain_and_non_DBD_sequence_extraction.ipynb` | PASS | 7 Python cells compared |
