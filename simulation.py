# simulation.py
import numpy as np

def generate_regression_function(x, m):
    np.random.seed(1)
    a = np.random.normal(0, 0.16, m)
    np.random.seed(2)
    b = np.random.normal(0, 0.16, m)
    return sum(a[i] * np.sin(2 * np.pi * (i + 1) * x) + b[i] * np.cos(2 * np.pi * (i + 1) * x) for i in range(m))

def generate_observations(x, f_true, sigma, n_sim):
    n = len(x)
    epsilon = np.random.normal(0, 1, size=(n, n_sim))
    Y = f_true.reshape(-1, 1) + sigma * epsilon
    return Y
