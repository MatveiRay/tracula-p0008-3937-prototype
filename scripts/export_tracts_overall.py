from pathlib import Path
import csv

ROOT = Path('/Users/rdti/TRACULA_OUT/P0008_3937/dpath')
OUT = Path('/Users/rdti/TRACULA_OUT/P0008_3937/P0008_3937_tracts_overall.csv')

rows = []
for stats_file in sorted(ROOT.glob('*/pathstats.overall.txt')):
    values = {}
    for line in stats_file.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split()
        if len(parts) == 2:
            values[parts[0]] = parts[1]
    tract_dir = stats_file.parent.name
    tract_name = tract_dir.replace('_avg16_syn_bbr', '')
    rows.append({
        'Tract': tract_name,
        'Count': values.get('Count', ''),
        'Volume_voxels': values.get('Volume', ''),
        'Len_Avg': values.get('Len_Avg', ''),
        'FA_Avg': values.get('FA_Avg', ''),
        'RD_Avg': values.get('RD_Avg', ''),
        'AD_Avg': values.get('AD_Avg', ''),
        'MD_Avg': values.get('MD_Avg', ''),
    })

with OUT.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)
print(f'Saved {OUT} with {len(rows)} tracts')
