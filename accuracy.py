import numpy as np


def accuracy(prediction, validation):
    """
    :param prediction: Matrix
    :param validation: Matrix
    :return: Accuracy between the prediction and the validation set,
             using average gap between prediction & validation divided by average prediction.
    """
    sum_gap_avg = 0.0
    sum_avg = 0.0
    for line in range(len(validation)):
        sum_gap_avg += np.absolute(prediction[line] - validation[line])
        sum_avg += prediction[line]

    return sum_gap_avg / sum_avg
