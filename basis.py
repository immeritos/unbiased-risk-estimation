# basis.py
import numpy as np

def chi(x, u, v):
    return np.where((x >= u) & (x < v), 1.0, 0.0)

def knots(m, degree):
    t = np.linspace(0, 1, m + 1)
    pad = degree + 1
    return np.pad(t, (pad, pad), mode='constant', constant_values=(0, 1))

def delta_vector(t, k):
    return np.where(t[:-k] < t[k:], t[k:] - t[:-k], 1.0)

def basis_matrix(x, m, degree):
    t = knots(m, degree)
    n_basis = m + degree + 1
    B = np.zeros((n_basis, len(x)))

    if degree == 0:
        for i in range(n_basis):
            B[i] = chi(x, t[i], t[i + 1])
    else:
        B_lower = basis_matrix(x, m, degree - 1)
        delta = delta_vector(t, degree)
        for i in range(n_basis - 1):
            left = (x - t[i]) / delta[i] * B_lower[i] if delta[i] != 0 else 0
            right = (t[i + degree + 1] - x) / delta[i + 1] * B_lower[i + 1] if delta[i + 1] != 0 else 0
            B[i] = left + right
    return B

def basis_matrix_bspline(x, m, degree):
    return basis_matrix(x, m, degree)

def basis_matrix_linear(x, m):
    """Constructs piecewise linear spline basis (degree = 1)."""
    t = np.linspace(0, 1, m + 1)
    t = np.pad(t, (1, 1), mode='constant', constant_values=(0, 1))
    n_basis = m + 1
    B = np.zeros((n_basis, len(x)))
    for i in range(n_basis):
        left = (x - t[i]) / (t[i + 1] - t[i]) * ((x >= t[i]) & (x < t[i + 1]))
        right = (t[i + 2] - x) / (t[i + 2] - t[i + 1]) * ((x >= t[i + 1]) & (x < t[i + 2]))
        B[i] = left + right
    return B

def get_spline_basis(x, m, degree=3, spline_type="bspline"):
    """Unified interface to get spline basis of specified type."""
    if spline_type == "bspline":
        return basis_matrix_bspline(x, m, degree)
    elif spline_type == "linear":
        return basis_matrix_linear(x, m)
    else:
        raise ValueError(f"Unknown spline type: {spline_type}")
