import numpy as np
import pandas as pd
from argparse_func import *

# Extracting data from csv file
train_data = pd.read_csv(args.train)
# Converting array to Numpy array
train_data = np.array(train_data)
# Deleting 1st column
train_data = np.delete(train_data, 0, 1)

# Extracting data from csv file
test_data = pd.read_csv(args.test)
# Converting array to Numpy array
test_data = np.array(test_data)
# Deleting 1st column
test_data = np.delete(test_data, 0, 1)

# Extracting data from csv
validation = pd.read_csv(args.validation)
# Converting array to Numpy array
validation = np.array(validation)
# Taking the data's 2nd column
validation = validation[:, 1]
# Converting data into float
validation = validation.astype(np.float)
