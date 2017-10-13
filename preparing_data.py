import numpy as np


def preparing_data(train_data, test_data):
    """
    :param train_data: Matrix
    :param test_data: Matrix
    :return: 3 matrices ready to be used by an algorithm
    """
    X = np.delete(train_data, [len(train_data[0]) - 1], 1)
    X = np.array(X)
    X = X.astype(np.float)
    y = train_data[:, -1]
    y = np.array(y)
    y = y.astype(np.float)
    X_test = test_data
    X_test = np.array(X_test)
    X_test = X_test.astype(np.float)

    return X, y, X_test
