# example_gp_prior_cosine
# author: Jungtaek Kim (jtkim@postech.ac.kr)
# last updated: June 24, 2018

import numpy as np

from bayeso import gp
from bayeso.utils import utils_plotting


def linear_up(X):
    return np.cos(X)

def main():
    X_train = np.array([
        [-3.0],
        [-2.0],
        [-1.0],
    ])
    Y_train = np.cos(X_train) + 2.0
    num_test = 200
    X_test = np.linspace(-3, 6, num_test)
    X_test = X_test.reshape((num_test, 1))
    Y_test_truth = np.cos(X_test) + 2.0
    prior_mu = linear_up
    mu, sigma = gp.predict_optimized(X_train, Y_train, X_test, prior_mu=prior_mu)
    utils_plotting.plot_gp(X_train, Y_train, X_test, mu, sigma, Y_test_truth, '../results/gp/', 'test_optimized_prior_cosine')


if __name__ == '__main__':
    main()

