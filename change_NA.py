import pandas as pd


def change_NA(matrix):
    """
    :param matrix: Matrix
    :return: Change 'NA' into 'O' in input matrix
    """
    for line in range(len(matrix)):
        for column in range(len(matrix[0])):
            if pd.isnull(matrix[line, column]):
                matrix[line, column] = '0'
