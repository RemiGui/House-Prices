import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-T', '--train',
                    metavar='', required=True, type=str,
                    help="The train data file name")
parser.add_argument('-t', '--test',
                    metavar='', required=True, type=str,
                    help="The test data file name")
parser.add_argument('-v', '--validation',
                    metavar='', required=True, type=str,
                    help="The validation set file name")
parser.add_argument('-a', '--algorithm',
                    choices=['linear_regression', 'decision_tree', 'SVM'],
                    metavar='', required=True, type=str,
                    help="Algorithm used, linear_regression, SVM or decision_tree.")
args = parser.parse_args()
