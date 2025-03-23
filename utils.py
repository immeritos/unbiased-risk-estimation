# utils.py
import numpy as np

def chi(x, u, v):
    return np.where((x >= u) & (x < v), 1.0, 0.0)

def delta_vector(t, k):
    return np.where(t[:-k] < t[k:], t[k:] - t[:-k], 1.0)

def knots(m, degree):
    t = np.linspace(0, 1, m + 1)
    pad = degree + 1
    return np.pad(t, (pad, pad), mode='constant', constant_values=(0, 1))
