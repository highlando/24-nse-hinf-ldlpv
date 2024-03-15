import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-notebook')
# plt.rcParams.update({'font.size': 22})

gammal = [8, 2,  0.5,  0.125,  0.038]
bbl = [291.0, 337.4, 720.7, 1482.8, 2164.4 ]
pol = [203.2, 350.4, 517.1, 714.4, np.NaN]

plt.figure(1, figsize=(8, 3))
plt.semilogx(gammal, bbl, 's-', label='bounding box')
plt.semilogx(gammal, pol, 'o-', label='polytope')
plt.xlabel('achieved performance $\\gamma$')
plt.ylabel('CPU time (seconds)')
plt.legend()
plt.tight_layout()
plt.savefig('gammaplot.png')
plt.show()
