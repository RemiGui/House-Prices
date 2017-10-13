from argparse_func import *
from decision_tree import *
from SVM import *
from linear_regression import *


def performing_algorithm(X, y, X_test):
    """
    :param X: Matrix
    :param y: Matrix
    :param X_test: Matrix
    :return: Prediction of chosen algorithm
    """
    if args.algorithm == "linear_regression":
        return linear_regression(X, y, X_test)
    elif args.algorithm == "decision_tree":
        return decision_tree(X, y, X_test)
    elif args.algorithm == "SVM":
        return SVM(X, y, X_test)
