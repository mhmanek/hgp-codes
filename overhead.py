from hgp import css_params
import math
from f2linalg import nullspace, in_rowspace

def surface_cost(d, k_wanted):
    """Physical qubits for k_wanted logical qubits at distance d, surface code."""
    one_patch_cost = 2*(d**2) - 2*d + 1
    k_cost = k_wanted * one_patch_cost
    return k_cost 

def hgp_cost(n_qubits, k_block, k_wanted):
    """Physical qubits for k_wanted logical qubits using blocks of this HGP code."""
    blocks = math.ceil(k_wanted / k_block)
    n_physical = blocks * n_qubits
    return n_physical

def crossover(n_qubits, d):
    """Smallest k_wanted at which one HGP block beats that many surface patches."""
    s = surface_cost(d, 1) # cost of surface code for one logical qubit
    crossing = math.ceil(n_qubits / s)
    return crossing

def logical_weight_bound(Hx, Hz, tries=4000):
    """Upper bound on the Z-distance: the lightest logical operator we could find."""
    # logical_operators = set([L in nullspace(Hx) and L not in in_rowspace(Hz, L)==False])

    # TODO repeatedly add a random subset of the rows of Hz to it (same logical class)
    # TODO keep the lowest nonzero weight you ever see, and return it
    # TODO name the return value so nobody can mistake it for the true distance
    raise NotImplementedError