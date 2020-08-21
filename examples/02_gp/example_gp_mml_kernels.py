# example_gp_mml_kernel_matern32
# author: Jungtaek Kim (jtkim@postech.ac.kr)
# last updated: August 07, 2020

import numpy as np
import os

from bayeso.gp import gp
from bayeso.utils import utils_common
from bayeso.utils import utils_plotting

PATH_SAVE = '../figures/gp/'
list_str_covs = [
    'se',
    'eq',
    'matern32',
    'matern52'
]

def main(str_cov):
    np.random.seed(42)
    X_train = np.array([
        [-3.0],
        [-1.0],
        [3.0],
        [1.0],
        [2.0],
    ])
    Y_train = np.cos(X_train) + np.random.randn(X_train.shape[0], 1) * 0.2
    num_test = 200
    X_test = np.linspace(-3, 3, num_test)
    X_test = X_test.reshape((num_test, 1))
    Y_test_truth = np.cos(X_test)

    mu, sigma, Sigma = gp.predict_optimized(X_train, Y_train, X_test, str_cov=str_cov, is_fixed_noise=False, debug=True)
    utils_plotting.plot_gp(X_train, Y_train, X_test, mu, sigma, Y_test_truth, path_save=PATH_SAVE, str_postfix='cos_' + str_cov)

if __name__ == '__main__':
    if not os.path.isdir(PATH_SAVE):
        os.makedirs(PATH_SAVE)

    for str_cov in list_str_covs:
        main(str_cov)

