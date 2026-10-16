# Reproducible analyses of *Aspergillus oryzae* GAL4-like Zn2Cys6 proteins

This repository contains the Google Colab notebooks and input data used for the revised analyses of GAL4-like Zn2Cys6 proteins in *Aspergillus oryzae* RIB40 and related *Aspergillus* species. The deposited workflows include cross-species evaluation of the proximity of orthologous genes to predicted biosynthetic gene clusters (BGCs) and pairwise Mantel comparisons among phylogenetic distance matrices derived from the DBD, operationally defined non-DBD, and full-length sequences.

## Repository layout

```text
notebooks/                         Analysis notebooks
input_data/annotations/            GTF annotations for seven species
input_data/sequences/              DBD, non-DBD, and full-length FASTA files
input_data/pca/                    Amino-acid composition and length tables
input_data/bgc_proximity/          A. oryzae antiSMASH and TF-ID inputs
input_data/synteny/                Curated BGC and ortholog workbooks
input_data/antismash_related_species/  Related-species antiSMASH JSON files
input_data/ortholog_lists/          Curated ortholog lists for six related species
input_data/source_preparation/        InterProScan and complete-proteome source files
reference_outputs/phylogenetic_trees/ Reference Newick trees
docs/                              File inventory and validation reports
```

Notebook outputs are intentionally excluded. Each notebook creates its own results or download archive.

## Recommended workflow

The notebooks were developed for Google Colab. Open a notebook in Colab and upload the files listed below to `/content` without changing their basenames.

| Order | Notebook | Required inputs |
|---:|---|---|
| 1 | `SM00066_domain_and_non_DBD_sequence_extraction.ipynb` | The six files in `input_data/source_preparation/` |
| 1b | `scripts/finalize_non_dbd_fasta.py` | The raw non-DBD FASTA generated in step 1, `aor0-5.faa`, and `aor0-5_SM00066.tsv`; adds the defined C-terminal-DBD exception AO090012000182 |
| 2 | `260904_AoTF_DBD_Length_histogram_revised.ipynb` | `aor0-5_SM00066_Protein_ID_Length.csv` |
| 3 | `260922_antiSMASH_area_based_bgc_proximity_sensitivity.ipynb` | `aor0-5.json`, `aor0-5.gtf`, `SM00066_ID_list.txt` |
| 3b | `260721_antiSMASH_area_based_with_reference_set_*.ipynb` | For each related species, the corresponding GTF file, antiSMASH JSON file, and curated ortholog list |
| 4 | `261012_AO090005001236_synteny.ipynb` | The two XLSX files and all seven GTF files |
| 5 | `260727_STREME.ipynb` | The three FASTA files in `input_data/sequences/` |
| 6 | `260922_AoTF_Phylogenetic_Tree_Analysis.ipynb` | The three FASTA files in `input_data/sequences/` |
| 6b | `260922_Mantel_test_pairwise_3_trees_Spearman_Holm.ipynb` | `Domain_tree.nwk`, `non_DBD_tree.nwk`, and `FL_tree.nwk` generated in step 6 or provided in `reference_outputs/phylogenetic_trees/` |
| 7 | `260923_AO_TF_PCA.ipynb` | The three aaComp CSV files plus the three `*_itol_colorstrip_support_k10.txt` files produced by notebook 6 |
| 8 | `260925_PCA_threshold_sensitivity_analysis.ipynb` | The three aaComp CSV files |
| 9 | `260925_PCA_sequence_length_effect_analysis.ipynb` | The three aaComp CSV files and the corresponding three FASTA files |

The six species-specific notebooks represented by step 3b evaluate whether orthologs of the 48 *A. oryzae* genes classified as BGC-associated at the primary 20-kb threshold are also located near antiSMASH-predicted BGCs in the related species. The analyses use the species-specific GTF annotations in `input_data/annotations/`, antiSMASH JSON files in `input_data/antismash_related_species/`, and curated ortholog lists in `input_data/ortholog_lists/`.

The ortholog lists were manually compiled from CAoGD and are therefore provided as curated input data rather than as notebook-generated outputs.

The Mantel-test notebook in step 6b compares patristic-distance matrices derived from the DBD, non-DBD, and full-length phylogenetic trees. Spearman correlations are used as the primary statistics, and pairwise P-values are adjusted using the Holm method.

The files in `reference_outputs/phylogenetic_trees/` are retained reference results. Notebook 6 can regenerate the trees from the FASTA inputs.

The sequence-preparation notebook applies its general C-terminal extraction rule and therefore omits AO090012000182, whose DBD is near the C terminus. Run `scripts/finalize_non_dbd_fasta.py` after the notebook to reproduce the deposited fixed non-DBD FASTA exactly.

## Software

Python dependencies are listed in `requirements.txt`. The phylogenetic workflow additionally installs MAFFT and FastTree. The motif workflow creates a Conda environment containing MEME Suite 5.5.9 and runs STREME. Google Colab is recommended because several notebooks use `google.colab.files` and `/content` paths.

## GitHub upload

The antiSMASH JSON files are 46-63 MB each. `.gitattributes` assigns JSON files to Git LFS. Before the first commit, run:

```bash
git lfs install
git add .
git commit -m "Add analysis notebooks and input data"
```

Upload this repository with Git rather than the GitHub web uploader so that the LFS rules are applied.

## Reproducibility status

The release copy passed JSON parsing, Python syntax checks for non-shell cells, a scan for Japanese text, and a code-structure comparison against the supplied notebooks. See:

- `docs/MATERIALS_AUDIT.md`
- `docs/VALIDATION_REPORT.md`
- `docs/CODE_INTEGRITY_REPORT.md`
- `docs/FILE_RENAMING.md`

The archive includes the raw source files required by the sequence-extraction notebook. The main PCA notebook additionally reads three iTOL color-strip files generated by the phylogenetic notebook; this is a workflow dependency rather than a missing source file.

## License

No reuse license was supplied with the original archive. Select and add an appropriate `LICENSE` file before making the repository public.

## Restricted source data

Genome sequences, protein sequences, gene annotations, and antiSMASH JSON
files derived from CAoGD/CAoGDX are not redistributed in this repository
because an explicit redistribution license could not be confirmed.

The antiSMASH JSON files are also excluded because they contain copies of
the input genome sequences and annotations. Users should obtain the source
data directly from CAoGD/CAoGDX and regenerate the antiSMASH results using
the versions and settings described in the manuscript.

Required filenames and workflow dependencies are documented in
`input_data/README.md`.

CAoGDX: https://nribf21.nrib.go.jp/CAoGDX/
