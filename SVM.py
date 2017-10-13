from sklearn.svm import SVC
import numpy as np


def SVM(X, y, X_test):
    """
    :param X: Matrix
    :param y: Matrix
    :param X_test: Matrix
    :return: Prediction using decision tree algorithm
    """
    clf = SVC().fit(X, y)

    return clf.predict(X_test).astype(np.int)
