# main.py
import numpy as np
from config import N_SAMPLES, N_GRID, N_SIMULATIONS, SIGMA, MAX_M
from simulation import generate_regression_function, generate_observations
from estimation import compute_bias, compute_risk, compute_AIC_risk
from plots import plot_bias_variance, plot_aic_distribution

if __name__ == "__main__":
    # Select spline type: "bspline" or "linear"
    spline_type = "bspline"
    degree = 3  # Only used for bspline

    # Create evaluation and sample grids
    z = np.linspace(0, 1, N_GRID, endpoint=False)
    x = np.linspace(0, 1, N_SAMPLES, endpoint=False)

    # Generate true function and noisy observations
    f_true = generate_regression_function(z, m=10)
    f_obs = generate_regression_function(x, m=10)
    Y = generate_observations(x, f_obs, SIGMA, N_SIMULATIONS)

    # Estimate bias, variance, and risk
    bias = compute_bias(f_true, x, z, Y, MAX_M, spline_type=spline_type)
    risk = compute_risk(f_true, x, z, Y, MAX_M, spline_type=spline_type)
    variance = risk - bias

    # Visualization
    plot_bias_variance(bias, variance)

    AIC_risk = compute_AIC_risk(Y, SIGMA, x, MAX_M, spline_type=spline_type)
    m_empirical = np.argmin(AIC_risk, axis=0)

    plot_aic_distribution(m_empirical, MAX_M)
