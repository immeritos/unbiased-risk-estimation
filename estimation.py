# estimation.py
import numpy as np
from basis import get_spline_basis

def projection_estimate(B_sample, B_eval, Y):
    B_pinv = np.linalg.inv(B_sample @ B_sample.T) @ B_sample
    theta = B_pinv @ Y
    return B_eval.T @ theta

def prediction_f(m, k, x, z, Y, degree=3, spline_type="bspline"):
    Bx = get_spline_basis(x, m, degree, spline_type)
    Bz = get_spline_basis(z, m, degree, spline_type)
    return projection_estimate(Bx, Bz, Y[:, k])

def mean_prediction(m, x, z, Y, degree=3, spline_type="bspline"):
    preds = np.array([prediction_f(m, k, x, z, Y, degree, spline_type) for k in range(Y.shape[1])])
    return preds.mean(axis=0)

def compute_bias(f_true, x, z, Y, MAX_M, spline_type="bspline"):
    bias = np.zeros(MAX_M)
    for m in range(MAX_M):
        f_bar = mean_prediction(m, x, z, Y, spline_type=spline_type)
        bias[m] = np.sum((f_true - f_bar) ** 2)
    return bias

def compute_risk(f_true, x, z, Y, MAX_M, spline_type="bspline"):
    risk = np.zeros(MAX_M)
    for m in range(MAX_M):
        total = 0
        for k in range(Y.shape[1]):
            f_hat = prediction_f(m, k, x, z, Y, spline_type=spline_type)
            total += np.sum((f_true - f_hat) ** 2)
        risk[m] = total / Y.shape[1]
    return risk

def compute_projection_operator(x, m, degree=3, spline_type="bspline"):
    Bx = get_spline_basis(x, m, degree, spline_type)
    return Bx.T @ np.linalg.inv(Bx @ Bx.T) @ Bx

def compute_AIC_risk(Y, sigma, x, MAX_M, spline_type="bspline"):
    AIC_risk = np.zeros((MAX_M, Y.shape[1]))
    for m in range(MAX_M):
        Pi = compute_projection_operator(x, m, spline_type=spline_type)
        for k in range(Y.shape[1]):
            residual = Y[:, k] - Pi @ Y[:, k]
            AIC_risk[m, k] = np.sum(residual ** 2) + 2 * sigma * (m + 3)
    return AIC_risk
