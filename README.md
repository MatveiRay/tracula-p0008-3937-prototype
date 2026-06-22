# TRACULA / FreeSurfer: P0008_3937

This repository documents the current prototype for TRACULA-based white-matter tract reconstruction and the first QC layer for subject `P0008_3937`.

## Current status

Completed TRACULA stages:

1. `prep`
2. `bedp`
3. `path`
4. `stat`

The prototype reconstructs 42 tracts and produces both tract visualizations and whole-tract statistics.

## Software stack

- FreeSurfer 8.1.0 / TRACULA
- FSL
- ANTs
- FreeView
- Python scripts for exporting metrics and QC plots

## Main fixes made during setup

- validated AP/PA DWI, `bvec`, `bval`, and JSON inputs;
- corrected `echospacing` from `0.000322866` to `0.322866`;
- disabled unavailable thalamic nuclei segmentation with `usethalnuc = 0`;
- switched `interreg` from `3` to `5` to avoid unavailable `rob` templates;
- replaced incompatible ANTs build with a micromamba-installed version.

## Reproducible TRACULA commands

```bash
trac-all -prep -c /Users/rdti/TRACULA_WORK/P0008_3937/dmrirc/dmrirc.P0008_3937
trac-all -bedp -c /Users/rdti/TRACULA_WORK/P0008_3937/dmrirc/dmrirc.P0008_3937
trac-all -path -c /Users/rdti/TRACULA_WORK/P0008_3937/dmrirc/dmrirc.P0008_3937
trac-all -stat -c /Users/rdti/TRACULA_WORK/P0008_3937/dmrirc/dmrirc.P0008_3937
```

## Atlas-like visualization

```bash
freeview \
-v /Users/rdti/TRACULA_OUT/P0008_3937/dmri/dtifit_FA.nii.gz \
-tv /Users/rdti/TRACULA_OUT/P0008_3937/dpath/merged_avg16_syn_bbr.mgz
```

## Repository contents

- `metrics/P0008_3937_tracts_overall.csv` — whole-tract metrics for 42 tracts;
- `figures/` — FreeView screenshots and QC plots;
- `scripts/export_tracts_overall.py` — export of tract-level metrics from TRACULA outputs;
- `scripts/make_cst_qc_plots.py` — plotting of CST QC summaries;
- `config/dmrirc.P0008_3937.example` — key TRACULA configuration parameters;
- `docs/project_status.md` — current limitations and planned improvements.

## Current limitations

- the current version is focused on successful reconstruction and visual validation;
- full automation of QC and report generation is still under development;
- FA/RD/AD profiles along tracts are planned as the next quantitative layer.

## Planned next steps

1. automate QC checks and output summaries;
2. generate FA/RD/AD tract profiles;
3. add subject-level PDF reports;
4. prepare multi-subject control/reference workflow.
