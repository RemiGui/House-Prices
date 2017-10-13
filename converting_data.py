from data_preprocessing import *
from index_strings import *


def converting_data(train_data, test_data):
    """
    :param train_data: Matrix
    :param test_data: Matrix
    :return: Ints instead of strings in train & test data
    """
    # Creates an array with all columns with strings we have to change
    arr_change = index_strings(train_data)

    # Changes all strings in columns indexed arr_change into ints
    train_data, test_data = data_preprocessing(train_data, test_data, arr_change)

    return train_data, test_data
