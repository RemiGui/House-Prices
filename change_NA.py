import pandas as pd


def change_NA(matrix):
    """
    :param matrix: Matrix
    :return: Change 'NA' into 'O' in input matrix
    """
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if pd.isnull(matrix[j, i]):
                matrix[j, i] = '0'
