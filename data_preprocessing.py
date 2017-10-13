import pandas as pd


def data_preprocessing(train_data, test_data, arr_change):
    """
    :param train_data: Matrix
    :param test_data: Matrix
    :param arr_change: Matrix
    :return: Train and test data preprocessed (with strings changes into ints)
    """
    # Browsing train data with arr_change's index
    for column in range(len(arr_change)):
        value_change = []
        index_change = []
        var = 0
        # Browsing train data's lines
        for line in range(len(train_data)):
            # Storage string in value_change and var in index_change if string is unknown and not null
            if train_data[line][arr_change[column]] not in value_change \
                    and not pd.isnull(train_data[line][arr_change[column]]):
                value_change.append(train_data[line][arr_change[column]])
                index_change.append(var)
                # Changing this string in test data into index_change's actual index (var)
                for i in range(len(test_data)):
                    if test_data[i][arr_change[column]] == train_data[line][arr_change[column]]:
                        test_data[i][arr_change[column]] = index_change[var]
                train_data[line][arr_change[column]] = index_change[var]
                var += 1
            # If string is known, changing this string in train data into index_change's
            # corresponding index (var)
            elif not pd.isnull(train_data[line][arr_change[column]]):
                var_loop3 = 0
                while train_data[line][arr_change[column]] != value_change[var_loop3]:
                    var_loop3 += 1
                train_data[line][arr_change[column]] = index_change[var_loop3]

    return train_data, test_data
