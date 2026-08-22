# hgp-codes
What this repository contains:
1. Code files that reproduce claims from the paper "Constant-overhead fault-tolerant quantum computation with reconfigurable atom arrays"
2. An html tool for visualizing hypergraph product codes

# Paper Claim Reproductions

| $n_{seed}$ | paper | my $n_{qubits}$ | my $k_{qubits}$ | my $d_{HGP}$ | my HGP code |
|---|---|---|---|---|---|
| 12 | [[225, 9, 4]] | 225 | 9 | 6 | [[225, 9, 6]] |
| 20 | [[625, 25, 6]] | 625 | 25 | 8 | [[625, 25, 8]] |
| 28 | [[1225, 49, 8]] | 1225 | 49 | 10 | [[1225, 49, 10]] |
| 40 | [[2500, 100, 12]] | 2500 | 100 | 12 | [[2500, 100, 12]] |
| 60 | [[5625, 225, 16]] | 5625 | 225 | 14 | [[5625, 225, 14]] |
| 80 | [[10000, 400, 18]] | 10000 | 400 | 18 | [[10000, 400, 18]] |

Note: $d_{HGP}$ is minimum of $d_{seed}$ and $d_{seed}^T$, so I checked rank($H_{seed}$) and number of rows of $H_{seed}$ to get $k_{seed}^T$ (which was often 0 implying $d_{seed}^T = \infty$)


# Visualization Tool

I saw [this talk](https://www.youtube.com/watch?v=MqGBwQjS4CI) which explains qLDPC codes and presents an animation to visualize hypergraph product codes.
