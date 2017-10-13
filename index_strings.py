import numpy as np


def index_strings(matrix):
    """
    :param matrix: Matrix
    :return: Array of column's with strings index
    """
    arr_change = []

    for column in range(len(matrix[0])):
        line = 0
        while line < len(matrix):
            if type(matrix[line][column]) == str:
                line += 1
                arr_change.append(column)
            else:
                line += 1

    arr_change = np.array(arr_change)
    arr_change = np.unique(arr_change)

    return arr_change
