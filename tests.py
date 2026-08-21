# This file runs tests to check correctness of code

import numpy as np
from f2linalg import nullspace
from hgp import hypergraph, check_css, rep_code, css_params
from seeds import regular_seed, best_seed, classical_distance

# Hypergraph product of 3-bit repetition codes
# rep_3 = rep_code(3)
# rep_3_hgp = hgp(rep_3, rep_3)
# print(check_css(rep_3_hgp[0], rep_3_hgp[1]))

# n-bit hypergraph product code
n_seed = 16
best_H, best_d = best_seed(n_seed)
r = best_H.shape[0]
H_quantum = hypergraph(best_H, best_H)
n_qubits, k = css_params(H_quantum[0], H_quantum[1])
print(best_d, n_qubits, k, k/n_qubits)