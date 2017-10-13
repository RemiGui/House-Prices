from input_data import *
from performing_algorithm import *
from accuracy import *
from treating_data import *
from preparing_data import *

# Treating data
train_data, test_data = data_treatment(train_data, test_data)

# Preparing features and labels for algorithm
X, y, X_test = preparing_data(train_data, test_data)

# Decision tree algorithm
prediction = performing_algorithm(X, y, X_test)

# Display accuracy of prediction
print "Accuracy : average gap divided by average price"
print accuracy(prediction, validation)
