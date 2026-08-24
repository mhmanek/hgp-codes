from seeds import regular_seed_girth6
import random
from hgp import hypergraph
import numpy as np

def hgp_block_params(n_seed):
    """(data, ancilla, total, k_logical) for an HGP block from a (3,4)-regular seed."""
    seed = regular_seed_girth6(n_seed, rng=random.Random(42))
    Hx, Hz = hypergraph(seed, seed)
    data = Hx.shape[1]
    ancilla = Hx.shape[0] + Hz.shape[0]
    m, n = seed.shape
    r = np.linalg.matrix_rank(seed)
    k_logical = (n - r) ** 2 + (m - r) ** 2   # K = k^2 + (k^T)^2 for HGP(H, H)
    return data, ancilla, data + ancilla, k_logical

def hgp_qubit_count(n_seed):
    """(data, ancilla, total) atoms for an HGP block from a (3,4)-regular seed."""
    data, ancilla, total, _ = hgp_block_params(n_seed)
    assert total == (3.0625 * (n_seed**2))
    return data, ancilla, total

def surface_qubits(k, d):
    """Atoms for k logical qubits in rotated surface patches, data + ancilla."""
    data = d**2
    ancilla = (d**2) - 1
    total = k * (data + ancilla)
    return total

def t_rearrange(L, tau_t=50, a_p=0.02, spacing=5.0):
    """Eq (7). L in sites, tau_t in us, a_p in um/us^2, spacing in um. Returns in microseconds."""
    time = 2*tau_t*np.log2(L)  +  (3 + 2*np.sqrt(2)) * np.sqrt(6*L*spacing/a_p)
    return time

def p_idle(L, pg=1e-3, Tc=1e7):
    return t_rearrange(L)/Tc * pg/0.005

def lfr_hgp(n_data, pg=1e-3, idling=True, Tc=1e7):
    L = np.sqrt(n_data)
    pg_eff = pg + 3*p_idle(L, pg, Tc) if idling else pg
    return 0.07 * (pg_eff/0.006)**(0.47 * n_data**0.27)

def lfr_lp(n_data, pg=1e-3, idling=True, Tc=1e7):
    L = np.sqrt(n_data)
    pg_eff = pg + 3*p_idle(L, pg, Tc) if idling else pg
    return 2.3 * (pg_eff/0.0066)**(0.11 * n_data**0.60)

def lfr_surface(k, d, pg=1e-3):
    P0 = 0.03 * (pg/0.011)**np.ceil(d/2)
    return 1 - (1 - P0)**k

def table1(k_target, lfr_target, pg=1e-3, d_max=99):
    """For each (k_target, lfr_target): the cheapest surface code and qLDPC code
    that meet it, and the ratio. Emits markdown.

    Accepts scalars (one row) or equal-length/broadcastable lists (one row each).
    """
    ks, tgts = np.broadcast_arrays(np.atleast_1d(k_target), np.atleast_1d(lfr_target))

    rows = []
    for k, tgt in zip(ks.flat, tgts.flat):
        k = int(k)

        # --- surface: smallest (odd) distance with lfr_surface(k, d) <= target ---
        d = 3
        while d <= d_max and lfr_surface(k, d, pg) > tgt:
            d += 2                     # odd distances only
        s_cost = surface_qubits(k, d) if d <= d_max else None
        d = d if s_cost is not None else None

        # --- HGP: smallest of the paper's blocks (n_s = 20, 40, 60, 80) with
        #     k_block >= k_target AND lfr_hgp(n_data) <= target ---
        n_s_hit = k_hit = q_cost = None
        for n_s in (20, 40, 60, 80):
            data, _, total, k_block = hgp_block_params(n_s)
            if k_block >= k and lfr_hgp(data, pg) <= tgt:
                n_s_hit, k_hit, q_cost = n_s, k_block, total
                break

        saving = (s_cost / q_cost) if (s_cost and q_cost) else None
        rows.append((k, tgt, d, s_cost, n_s_hit, k_hit, q_cost, saving))

    # --- emit markdown ---
    out = [
        "| k_target | lfr_target | surface d | surface atoms | HGP n_{seed} | HGP k | HGP atoms | saving over surface code (x) |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for k, tgt, d, s_cost, n_s, kb, qc, sv in rows:
        out.append("| {} | {:.0e} | {} | {} | {} | {} | {} | {} |".format(
            k, tgt,
            d if d is not None else "—",
            f"{s_cost:,}" if s_cost is not None else "—",
            n_s if n_s is not None else "—",
            kb if kb is not None else "—",
            f"{qc:,}" if qc is not None else "—",
            f"{sv:.2f}" if sv is not None else "—",
        ))
    return "\n".join(out)
