from converting_data import *
from change_NA import *


def data_treatment(train_data, test_data):
    """
    :param train_data: Matrix
    :param test_data: Matrix
    :return: Preprocessed test data & train data
    """
    # Converting strings to ints in train data & test data (except 'NA')
    train_data, test_data = converting_data(train_data, test_data)

    # Changing NA into 0 for index in array_change_NA in train and test data
    change_NA(train_data)
    change_NA(test_data)

    return train_data, test_data
