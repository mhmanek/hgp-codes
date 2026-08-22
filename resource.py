from seeds import regular_seed_girth6
import random
from hgp import hypergraph
import numpy as np

def hgp_qubit_count(n_seed):
    """(data, ancilla, total) atoms for an HGP block from a (3,4)-regular seed."""
    # TODO do NOT hardcode 3.0625. build the actual seed, call hgp(), and read
    seed = regular_seed_girth6(n_seed,rng=random.Random(42))
    Hx, Hz = hypergraph(seed, seed)
    data = Hx.shape[1]
    ancilla = Hx.shape[0] + Hz.shape[0]
    total = data + ancilla
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

def p_idle(L, pg=1e-3, Tc=10.0):
    p_i = t_rearrange(L)/Tc * pg/0.005

def lfr_hgp(n_data, pg=1e-3, idling=True):
    L = np.sqrt(n_data)
    pg_eff = pg + 3*p_idle(L) if idling else pg
    return 0.07 * (pg_eff/0.006)**(0.47 * n_data**0.27)

def lfr_lp(n_data, pg=1e-3, idling=True):
    L = np.sqrt(n_data)
    pg_eff = pg + 3*p_idle(L) if idling else pg
    return 2.3 * (pg_eff/0.0066)**(0.11 * n_data**0.60)

def lfr_surface(k, d, pg=1e-3):
    P0 = 0.03 * (pg/0.011)**np.ceil(d/2)
    return 1 - (1 - P0)**k

def table1(k_target, lfr_target, pg=1e-3):
    """For each (k_target, lfr_target): the cheapest surface code and qLDPC code
    that meet it, and the ratio. Emits markdown."""

    # TODO surface: smallest d with lfr_surface(k, d) <= target; cost surface_qubits(k, d)
    # TODO hgp: the smallest of the paper's codes (n_s = 20, 40, 60, 80) with
    #      k_block >= k_target AND lfr_hgp <= target; cost from hgp_qubit_count
    # TODO saving = surface cost / qLDPC cost
    raise NotImplementedError