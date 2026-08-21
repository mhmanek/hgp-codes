# This file runs tests to check correctness of code

import numpy as np
from f2linalg import nullspace, rank
from hgp import hypergraph, check_css, rep_code, css_params, max_stabilizer_weights
from seeds import regular_seed, best_seed, exact_distance, regular_seed_girth6

# n-bit hypergraph product code
# n_seed = 4
# best_H, best_d = best_seed(n_seed)

# r_seed = best_H.shape[0]
# k_seed = n_seed - rank(best_H)
# k_seed_transpose = r_seed - rank(best_H)

# H_quantum = hypergraph(best_H, best_H)
# n_qubits, k_qubits = css_params(H_quantum[0], H_quantum[1])
# rate_quantum = k_qubits / n_qubits
# max_x_weight, max_z_weight = max_stabilizer_weights(H_quantum[0], H_quantum[1])

# print('|', n_seed, '|', r_seed, '|', k_seed, '|', k_seed_transpose, '|', best_d, '|', n_qubits, '|', k_qubits, '|', rate_quantum, '|', max_x_weight, '|', max_z_weight, '|')

