import numpy as np
from f2linalg import rank

def hgp(H1, H2):
    """Hypergraph product of two classical codes. Returns (Hx, Hz)."""
    H1 = H1.copy().astype(np.uint8) % 2
    H2 = H2.copy().astype(np.uint8) % 2
    r1, n1 = H1.shape
    r2, n2 = H2.shape
    def I(k):
        return np.eye(k, dtype=np.uint8)
    Hx = np.hstack([np.kron(H1, I(n2)), 
                    np.kron(I(r1), np.transpose(H2))])
    Hz = np.hstack([np.kron(I(n1), H2), 
                    np.kron(np.transpose(H1), I(r2))])
    return Hx, Hz

def css_params(Hx, Hz):
    """Return (n, k) for the CSS code defined by Hx, Hz."""
    assert Hx.shape[1] == Hz.shape[1], "Hx and Hz do not act on the same number of qubits"
    n = Hx.shape[1]
    k = n - rank(Hx) - rank(Hz)
    return n, k

def check_css(Hx, Hz):
    M = np.matmul(Hx, np.transpose(Hz)) % 2
    assert not M.any(), "not a valid CSS code"

def rep_code(d):
    """Parity check matrix of the length-d repetition code: (d-1) x d."""
    M = np.zeros((d-1, d), dtype=np.uint8)
    for i in range(d-1):
        M[i, i] = 1
        M[i, i+1] = 1
    return M

Hx, Hz = hgp(rep_code(4), rep_code(4))
print(css_params(Hx, Hz))