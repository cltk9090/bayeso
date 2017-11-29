import numpy as np
import scipy.stats

def pi(pred_mean, pred_std, Y_train):
    return scipy.stats.norm.cdf((np.min(Y_train) - pred_mean) / pred_std)

def ei(pred_mean, pred_std, Y_train):
    val_z = (np.min(Y_train) - pred_mean) / pred_std
    return (np.min(Y_train) - pred_mean) * scipy.stats.norm.cdf(val_z) + pred_std * scipy.stats.norm.pdf(val_z)

def ucb(pred_mean, pred_std, Y_train=None):
    kappa = 2.0
    return -pred_mean + kappa * pred_std


if __name__ == '__main__':
    pass

