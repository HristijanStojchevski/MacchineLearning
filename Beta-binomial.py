from scipy.stats import beta
import numpy as np
import matplotlib.pyplot     as plt

def Beta_binom(N_1, N_0, a, b):
    fig, ax = plt.subplots(1, 1)
    plt.xlabel(r"$\dot{\theta}$")
    plt.xlim(0, 1)
    plt.ylim(0.5, 7)

    x = np.linspace(beta.ppf(0.01, a, b),
                    beta.ppf(0.99, a, b), 100)
    ax.plot(x, beta.pdf(x, a, b), lw=2, alpha=0.6, label='prior')

    x = np.linspace(beta.ppf(0.01, N_1, N_0),
                    beta.ppf(0.99, N_1, N_0), 100)
    ax.plot(x, beta.pdf(x, N_1, N_0), lw=2, alpha=0.6, label='likelihood')

    x = np.linspace(beta.ppf(0.01, a + N_1, b + N_0),
                    beta.ppf(0.99, a + N_1, b + N_0), 100)
    ax.plot(x, beta.pdf(x, a + N_1, b + N_0), lw=2, alpha=0.6, label='posterior')

    mean, var, skew, kurt = beta.stats(a + N_1, b + N_0, moments='mvsk')
    plt.axvline(mean, color="red")  # , label = "Mean Posterior")
    MedianPosterior = beta(a + N_1, b + N_0).median()
    plt.axvline(MedianPosterior, color="green")  # , label = "Mode Posterior")

    #     plt.plot(-1, 1, color = "navyblue", label = "Mode Posterior")

    print("Mean:", np.round(mean, 2))

    #    print("Variance:", np.round(var,2))
    #    print("Mode:", np.round(MedianPosterior,2))

    plt.legend()
    plt.show()
