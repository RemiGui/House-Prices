from sklearn import linear_model
import numpy as np


def linear_regression(X, y, X_test):
    """
    :param X: Matrix
    :param y: Matrix
    :param X_test: Matrix
    :return: Prediction using linear regression algorithm
    """
    reg = linear_model.LinearRegression().fit(X, y)

    return reg.predict(X_test).astype(np.int)
