# plots.py
import matplotlib.pyplot as plt
import numpy as np

def plot_bias_variance(bias, variance):
    plt.figure(figsize=(14, 6))
    plt.subplot(1, 2, 1)
    plt.plot(range(1, len(bias)+1), bias, label='Bias^2', color='blue')
    plt.title("Bias^2 vs m")
    plt.grid(True, linestyle=':')

    plt.subplot(1, 2, 2)
    plt.plot(range(1, len(variance)+1), variance, label='Variance', color='green')
    plt.title("Variance vs m")
    plt.grid(True, linestyle=':')
    plt.tight_layout()
    plt.show()

def plot_aic_distribution(m_empirical, MAX_M):
    plt.figure(figsize=(12, 6))
    plt.hist(m_empirical, bins=np.arange(0, MAX_M+1), color='orange', edgecolor='black', alpha=0.7)
    plt.title("Empirical Distribution of AIC-selected m")
    plt.xlabel("m")
    plt.ylabel("Frequency")
    plt.grid(True, linestyle=':')
    plt.show()
