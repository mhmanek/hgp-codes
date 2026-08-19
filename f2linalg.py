import numpy as np

def row_reduce(A):
    """Reduced row echelon form of A over GF(2).
    Returns (R, pivots) where pivots is the list of pivot column indices."""
    A = A.copy().astype(np.uint8) % 2 # first convert into a binary matrix by taking mod 2
    r = 0 # initialise variable for pivot-row counter r
    pivots = []
    for c in range(np.shape(A)[1]): # walk left to right over columns
        for j in range(r, np.shape(A)[0]): # for each column: find a row at index >= r with a 1 there; if none, skip the column
            if A[j, c] != 0:
                A[[r, j]] = A[[j, r]] # swap that row up to position r
                for i in range(0, np.shape(A)[0]):
                    if i != r and A[i, c] != 0:
                        A[i] ^= A[r] # XOR row r into every other row that has a 1 in this column
                pivots.append(c) # append the column index to pivots
                r += 1
                break
    return(A, pivots)

def rank(A):
    return len(row_reduce(A)[1]) # the rank is just how many pivots row_reduce found

def nullspace(A):
    """Basis for {x : A x = 0 mod 2}, returned as rows of a matrix."""
    R, pivots = row_reduce(A)
    n = A.shape[1]
    pivot_set = set(pivots)
    free_variables = [c for c in range(n) if c not in pivot_set]
    basis = []
    for j in free_variables:
        v = np.zeros(n, dtype=np.uint8)
        v[j] = 1
        for k in range(len(pivots)):
            v[pivots[k]] = R[k, j]
        basis.append(v)
    return np.array(basis, dtype=np.uint8).reshape(len(basis), n)

def in_rowspace(A, v):
    """Is the vector v a linear combination of the rows of A?"""
    return rank(A) == rank(np.vstack([A, v])) # compare rank(A) with rank of (A with v stacked underneath it)

# Tests
# rng = np.random.default_rng()
# M = rng.random((20, 30))
# print(rank(M) + nullspace(M).shape[0])