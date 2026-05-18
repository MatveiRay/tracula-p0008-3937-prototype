# Project status

## Completed

- TRACULA pipeline successfully executed for `P0008_3937` through `prep`, `bedp`, `path`, and `stat`.
- 42 tracts reconstructed.
- Atlas-like visualization obtained in FreeView from `merged_avg16_syn_bbr.mgz`.
- Whole-tract metrics exported to CSV.
- Initial CST QC performed using absolute and relative thresholds.

## Current QC interpretation

- CST is reconstructed bilaterally.
- `rel05` is the preferred QC threshold among the tested relative maps.
- `rel01` is too permissive and produces a large left-sided tail.
- Current summary status: `CST_QC = PASSED_WITH_NOTES`.

## Planned improvements

- automate the export of tract tables and QC reports;
- add FA/RD/AD profiles along each tract;
- formalize checkpoint strategy;
- support batch processing and report generation for future control cohorts.
