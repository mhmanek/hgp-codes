# hgp-codes
What this repository contains:
1. Code files that reproduce claims from the paper "Constant-overhead fault-tolerant quantum computation with reconfigurable atom arrays"
2. An html tool for visualizing hypergraph product codes

# Paper Claim Reproductions

(3,4)-regular Tanner graphs of classical LDPC codes

| n_{seed} | r_seed | k_seed | k_seed_transpose | best_d | n_qubits | k_qubits | rate_quantum | max_x_weight | max_z_weight |
| ---: | ---: | ---: | ---: | ---: |
| 16 | 12 | 4 | 0 | 8 | 400 | 16 | 0.04 | 7 | 7 |
| 20 | 15 | 5 | 0 | 8 | 625 | 25 | 0.04 | 7 | 7 |
| 24 | 18 | 6 | 0 | 8 | 900 | 36 | 0.04 | 7 | 7 |
| 28 | 21 | 7 | 0 | 10 | 1225 | 49 | 0.04 | 7 | 7 |
| 32 | 24 | 8 | 0 | 10 | 1600 | 64 | 0.04 | 7 | 7 |

n_{seed} is number of bits of seed classical LDPC code



# Visualization Tool

I saw [this talk](https://www.youtube.com/watch?v=MqGBwQjS4CI) which explains qLDPC codes and presents an animation to visualize hypergraph product codes.
