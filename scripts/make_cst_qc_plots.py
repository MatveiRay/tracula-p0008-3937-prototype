import matplotlib.pyplot as plt
import numpy as np

thresholds = [1,2,5,10,20,30,50,100,300]
lh = [35314.710938,26784.056641,13091.004883,4582.351562,706.054199,252.019348,146.011215,146.011215,146.011215]
rh_pairs = [(1,396.030396),(10,282.021637),(20,230.017654),(50,204.015656),(100,204.015656),(300,204.015656)]

plt.figure(figsize=(8,5))
plt.plot(thresholds, lh, marker='o', label='LH CST')
plt.plot([x for x,_ in rh_pairs], [y for _,y in rh_pairs], marker='o', label='RH CST')
plt.xscale('log')
plt.xlabel('Absolute probability-map threshold')
plt.ylabel('Volume, mm^3')
plt.title('CST volume across absolute thresholds')
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=.35)
plt.tight_layout()
plt.savefig('figures/graph1_cst_threshold_sweep.png', dpi=180)

labels = ['rel01','rel05','rel10']
lh_rel = [8586.659180,188.014435,146.011215]
rh_rel = [274.021027,204.015656,204.015656]
ov_rel = [8.000614,0,0]
x = np.arange(len(labels)); w = 0.24
plt.figure(figsize=(8,5))
plt.bar(x-w, lh_rel, width=w, label='LH CST')
plt.bar(x, rh_rel, width=w, label='RH CST')
plt.bar(x+w, ov_rel, width=w, label='Overlap')
plt.xticks(x, labels)
plt.xlabel('Relative QC threshold')
plt.ylabel('Volume, mm^3')
plt.title('CST comparison across relative QC thresholds')
plt.legend()
plt.grid(True, axis='y', linestyle='--', alpha=.35)
plt.tight_layout()
plt.savefig('figures/graph2_cst_relative_qc.png', dpi=180)
