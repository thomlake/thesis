import numpy as np
import matplotlib.pyplot as plt

deltasub = np.array([0, 0.5, 1, 1, 0.5, 0, 0, -0.5, -1, -1, -0.5, 0])#, 0, 0.5, 1, 1, 0.5, 0, 0, -0.5, -1, -1, -0.5, 0, 0, 0.5, 1, 1, 0.5, 0, 0, -0.5, -1, -1, -0.5, 0, 0, 0.5, 1, 1, 0.5, 0, 0, -0.5, -1, -1, -0.5, 0])
deltas = np.array([0])
for i in range(6):
    deltas = np.concatenate([deltas, deltasub])
fx = deltas.cumsum()
x = np.arange(len(fx))
fig, ax = plt.subplots(1, 1, figsize=(6,3))
ax.plot(x, fx, color='k')
ax.set_xlim((0, len(x) - 1))
ax.set_ylim((fx.min() - 1, fx.max() + 1))
ax.grid()
ax.set_xlabel(r'$t$')
ax.set_ylabel(r'$x_t$', rotation=0)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
plt.tick_params(axis='both', which='both', left='off', right='off', bottom='off', top='off')
# plt.tight_layout()
# fig.patch.set_visible(False)
# ax.spines['top'].set_visible(False)
# ax.spines['bottom'].set_visible(False)
# Only show ticks on the left and bottom spines
# ax.yaxis.set_ticks_position('left')
# ax.xaxis.set_ticks_position('bottom')
# plt.show()
plt.savefig('osc-step.png', frameon=False)
