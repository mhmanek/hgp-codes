import numpy as np
from f2linalg import nullspace

def regular_seed(n_bits, wc=3, wr=4, seed=0):
    """Random (wc, wr)-regular parity check matrix"""
    assert (n_bits * wc) % wr == 0
    r = n_bits * wc // wr
    bit_stubs   = np.repeat(np.arange(n_bits), wc)   # [0,0,0,1,1,1,...]
    check_stubs = np.repeat(np.arange(r), wr)        # [0,0,0,0,1,1,1,1,...]
    # TODO shuffle one of them, zip them together, set H[check, bit] = 1
    rng = np.random.default_rng(seed)
    while True:
        rng.shuffle(bit_stubs)
        H = np.zeros((r, n_bits), dtype=np.uint8)
        for i in range(n_bits * wc):
            H[check_stubs[i], bit_stubs[i]] += 1
        if np.all(H <= 1):
            break
    assert np.sum(H, axis=0) == wc
    assert np.all() # assert the column sums are all wc
    assert np.all(np.sum(H, axis=1) == wr) # assert the row sums are all wr
    return H

def classical_distance(H):
    """Exact minimum distance by enumerating all 2^k codewords. Small k only!"""
    nullspace(H)
    # TODO enumerate all 2^k - 1 nonzero combinations, return the smallest weight
    # TODO refuse to run if k is large -- raise, don't silently take an hour
    raise NotImplementedError

def best_seed(n_bits, trials=60):
    """Sample many seeds, keep the one with the largest exact distance."""
    # TODO loop, build, measure distance, keep the best; return (H, d)
    raise NotImplementedError