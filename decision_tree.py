from sklearn import tree
import numpy as np


def decision_tree(X, y, X_test):
    """
    :param X: Matrix
    :param y: Matrix
    :param X_test: Matrix
    :return: Prediction using decision tree algorithm
    """
    clf = tree.DecisionTreeClassifier(max_depth=4).fit(X, y)

    return clf.predict(X_test).astype(np.int)
