import numpy as np
from f2linalg import nullspace

def regular_seed(n_bits, wc=3, wr=4, seed=0):
    """Random (wc, wr)-regular parity check matrix"""
    assert (n_bits * wc) % wr == 0
    r = n_bits * wc // wr
    bit_stubs   = np.repeat(np.arange(n_bits), wc)   # [0,0,0,1,1,1,2,2,2,...]
    check_stubs = np.repeat(np.arange(r), wr)        # [0,0,0,0,1,1,1,1,2,2,2,2,...]
    rng = np.random.default_rng(seed)
    while True:
        rng.shuffle(bit_stubs)
        H = np.zeros((r, n_bits), dtype=np.uint8)
        for i in range(n_bits * wc):
            H[check_stubs[i], bit_stubs[i]] += 1
        if np.all(H <= 1):
            break
    assert np.all(np.sum(H, axis=0) == wc) # assert the column sums are all wc
    assert np.all(np.sum(H, axis=1) == wr) # assert the row sums are all wr
    return H

def classical_distance(H):
    """Exact code distance by enumerating all 2^k codewords. Small k only!"""
    basis = nullspace(H) # this is the basis for the codespace
    k = basis.shape[0]
    assert k <= 20
    best = basis.shape[1] + 1
    for mask in range(1, 2**k):
        c = np.zeros(basis.shape[1], dtype=basis.dtype)
        for i in range(k):
            if (mask >> i) & 1:
                c ^= basis[i]
        w = int(c.sum())
        if w < best:
            best = w
    return best

def best_seed(n_bits, trials=100):
    """Sample many seeds, keep the one with the largest exact distance."""
    best_H, best_d = None, -1
    for s in range(trials):
        H = regular_seed(n_bits, wc=3, wr=4, seed=s)
        d = classical_distance(H)
        if d > best_d:
            best_H, best_d = H, d
    return best_H, best_d
