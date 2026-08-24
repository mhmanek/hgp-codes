This repository reproduces a the HGP codes from the paper "Constant-Overhead Fault-Tolerant Quantum Computation with Reconfigurable Atom Arrays" by Qian Xu, Juan Pablo Bonilla Ataides and others.

# Procedure

I ran a search for sampling 1000 different (3,4)-regular "seed" classical matrices with Tanner graph girth ≥ 6. From the resulting set, I maximized seed distance and broke ties based on maximum spectral gap. This is exactly the seed-search procedure described in the paper's methods section. I then took the hypergraph product of the resulting matrix with itself. The resulting code parameters are given below.

# Results

| $n_{seed}$ | paper | my $n_{qubits}$ | my $k_{qubits}$ | my $d_{HGP}$ | my HGP code |
|---|---|---|---|---|---|
| 12 | [[225, 9, 4]] | 225 | 9 | 6 | [[225, 9, 6]] |
| 20 | [[625, 25, 6]] | 625 | 25 | 8 | [[625, 25, 8]] |
| 28 | [[1225, 49, 8]] | 1225 | 49 | 10 | [[1225, 49, 10]] |
| 40 | [[2500, 100, 12]] | 2500 | 100 | 12 | [[2500, 100, 12]] |
| 60 | [[5625, 225, 16]] | 5625 | 225 | 14 | [[5625, 225, 14]] |
| 80 | [[10000, 400, 18]] | 10000 | 400 | 18 | [[10000, 400, 18]] |

Notes: $d_{HGP} = \text{minimum}(d_{seed}, d_{seed}^T)$

$k_{seed}^T = \text{number of rows of } H_{seed} - \text{rank}(H_{seed})$

In every case, the seed matrix was full-rank, i.e., $k_{seed}^T =0$, implying $d_{seed}^T = \infty$ and giving $d_{HGP} = d_{seed}$

I am unsure why my results gave a larger distance than the paper in the cases $n_{seed}=12, 20, 28$. I am working to understand why this difference occurred.

For example, in the case $n_{seed}=12$, the following matrix is a $[12,3,6]$ classical code whose Tanner graph has $\text{girth}=6$, and when we take the HGP with itself, it is easy to check that we indeed get a quantum code with parameters $[[225,9,6]]$. 

$$H_{12} =
\begin{bmatrix}
0 & 1 & 1 & 0 & 0 & 1 & 0 & 0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 1 & 1 & 1 & 0 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & 1 & 0 & 0 & 1 & 1 & 1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 & 0 & 0 & 1 & 0 & 1 & 0 & 1 \\
1 & 0 & 0 & 0 & 0 & 1 & 0 & 1 & 0 & 0 & 1 & 0 \\
1 & 1 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 1 & 0 & 0 \\
1 & 0 & 1 & 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 \\
0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 1 & 1 & 0
\end{bmatrix}$$

# Visualization Tool

I saw [this talk](https://www.youtube.com/watch?v=MqGBwQjS4CI) which explains qLDPC codes and presents an animation to visualize hypergraph product codes. The file [hgp-visualisation.html](https://hgp-codes.vercel.app/) replicates the visual animation presented in the talk, and is a good way to develop intuition for the HGP.
