import numpy as np
from f2linalg import nullspace, rank
from hgp import hypergraph, check_css, rep_code, css_params, max_stabilizer_weights
from seeds import regular_seed, best_seed, exact_distance, regular_seed_girth6, search
from resource import hgp_qubit_count, table1, t_rearrange
import random

def run_complete_search(n_final):
    final_seed = search(n_final)[0]
    record = search(n_final)[1]
    final_Hx, final_Hz = hypergraph(final_seed, final_seed)
    row_count_final = final_seed.shape[0]
    rank_final = rank(final_seed)

    print(final_Hx.shape[0], final_Hz.shape[0])
    print("n =", css_params(final_Hx, final_Hz)[0])
    print("k =", css_params(final_Hx, final_Hz)[1])
    print("distance of seed =", exact_distance(final_seed))
    print("rank of seed =", rank(final_seed))
    print("row count of seed =", row_count_final)
    print("k^T =", row_count_final - rank_final)
    print(final_seed)

run_complete_search(12)

# print(table1(180, 2e-5))