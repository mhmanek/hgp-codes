import numpy as np
from f2linalg import nullspace
import random

def exact_distance(H, max_k=22):
    """Exact minimum distance of the code ker(H), by enumerating every codeword."""
    B = nullspace(H)
    k, n = B.shape
    if k == 0:
        return float('inf')
    if k > max_k:
        raise ValueError(f"k = {k} > max_k = {max_k}: 2^{k} codewords is too many")
    masks = [int("".join(map(str, row)), 2) for row in B]
    cur, best = 0, n + 1
    for i in range(1, 1 << k):
        cur ^= masks[(i & -i).bit_length() - 1]
        w = cur.bit_count()
        if 0 < w < best:
            best = w
    return best

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

def best_seed(n_bits, trials=100):
    """Sample many seeds, keep the one with the largest exact distance."""
    best_H, best_d = None, -1
    for s in range(trials):
        H = regular_seed(n_bits, wc=3, wr=4, seed=s)
        d = exact_distance(H)
        if d > best_d:
            best_H, best_d = H, d
    return best_H, best_d

def has_four_cycle(H):
    """True iff two checks share two or more bits. Equivalent to girth < 6."""
    G = H.astype(np.int64) @ H.astype(np.int64).T
    np.fill_diagonal(G, 0)
    return bool((G >= 2).any())

def spectral_gap(H):
    """sigma_1 - sigma_2 of H"""
    s = np.linalg.svd(H.astype(float), compute_uv=False)
    return float(s[0] - s[1])



###

# def regular_seed_girth6(n_bits, rng, wc=3, wr=4, attempts=200):
#     """A random (wc,wr)-regular seed whose Tanner graph has girth >= 6.

#     girth >= 6  <=>  no two bits share more than one check.  We enforce that
#     edge by edge while building, in the spirit of progressive edge growth:
#     walk the bits in random order and, for each of its wc edges, connect it to
#     the least-loaded check that would not close a 4-cycle.

#     Why not reject whole graphs, as the naive reading of "rejection sampling"
#     suggests?  The expected number of 4-cycles in a random (3,4)-regular
#     bipartite graph is ((wc-1)(wr-1))^2/4 = 9, independent of n, so only about
#     e^-9 ~ 1 draw in 10^4 is clean -- measured: 1 accepted in 4000 draws at
#     n=40, 0 in 4000 at every other size.  Edge-level rejection is the only
#     version that terminates.
#     """
#     r = n_bits * wc // wr
#     for _ in range(attempts):
#         H       = np.zeros((r, n_bits), dtype=np.uint8)
#         rowd    = [0] * r                          # bits placed in each check
#         co      = [set() for _ in range(n_bits)]   # bits sharing a check with b
#         members = [[] for _ in range(r)]
#         order   = list(range(n_bits))
#         rng.shuffle(order)
#         ok = True

#         for b in order:
#             for _edge in range(wc):
#                 cand = [c for c in range(r)
#                         if rowd[c] < wr                     # check not yet full
#                         and H[c, b] == 0                    # no repeated edge
#                         and not (co[b] & set(members[c]))]  # no 4-cycle
#                 if not cand:
#                     ok = False
#                     break
#                 lo = min(rowd[c] for c in cand)             # least-loaded check,
#                 cand = [c for c in cand if rowd[c] == lo]   # random tie-break
#                 c = cand[rng.randrange(len(cand))]

#                 H[c, b] = 1
#                 for x in members[c]:
#                     co[x].add(b)
#                     co[b].add(x)
#                 members[c].append(b)
#                 rowd[c] += 1
#             if not ok:
#                 break

#         if ok and all(d == wr for d in rowd):
#             return H
#     raise RuntimeError(f"no girth-6 seed at n_bits={n_bits} in {attempts} attempts")

# def search(n_bits, draws=1000, seed=0):
#     """Returns (best_H, record).

#     `record` holds every accepted draw's (d, gap, k1, rank) -- the ensemble
#     distribution is as much the finding as the winner is.
#     """
#     rng = random.Random(seed)
#     record, best_H, best_key = [], None, None

#     for _ in range(draws):
#         H = regular_seed_girth6(n_bits, rng)   # girth >= 6 by construction
#         assert not has_four_cycle(H)           # cheap independent confirmation

#         k1  = nullspace(H).shape[0]
#         d   = exact_distance(H)
#         gap = spectral_gap(H)
#         record.append({"d": d, "gap": gap, "k1": k1, "rank": n_bits - k1})

#         key = (d, gap)                         # distance first, gap as tie-break
#         if best_key is None or key > best_key:
#             best_key, best_H = key, H

#     return best_H, record

