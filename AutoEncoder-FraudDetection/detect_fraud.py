from pyod.models.auto_encoder import AutoEncoder
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
dataFrame = pd.read_csv('creditcard.csv')    

# print(dataFrame)


model_features = dataFrame.columns.drop('Class')
x = dataFrame[model_features]
y = dataFrame['Class']

contamination = 0.01  # ~1 % of data is fraud (close to true ratio ~0.17 %) 
epochs = 30


# Define the structure of the AutoEncoder. The list contains the number of neurons in each hidden layer.
# 64 neurons in the first hidden layer, 30 neurons in the second hidden layer, 30 neurons in the third hidden layer, and 64 neurons in the fourth hidden layer.
# The input and output layers will automatically have the same number of neurons as the number of features in the dataset (30 in this case).
hidden_neurons = [64, 30, 30, 64]

# Instantiate AutoEncoder and start training
# batch_size is set to 256, which means the model will process 256 samples at a time during training. This can help speed up training and improve convergence.
# contamination is set to 0.01, which means the model will assume that 1% of the data is anomalous. This is close to the true ratio of fraud in the dataset (~0.17%).
clf = AutoEncoder(hidden_neuron_list=hidden_neurons, 
                  epoch_num=epochs, 
                  contamination=contamination, 
                  batch_size=256)
# Train the model
clf.fit(x)
# Predict the outliers
outliers = clf.predict(x)

# Filter outliers and print their indices in the original dataset
anomaly = np.where(outliers==1)
# print(anomaly)


# Calculate outlier scores of the training data. Higher scores means higher severity of abnormalities
y_scores = clf.decision_scores_ 

print(y_scores)
# Visualize a scatter plot of the outlier scores with respect to 'Time' and 'Amount' features.
sns.scatterplot(x="Time", y="Amount", hue= y_scores, data=dataFrame, palette="RdBu_r", size=y_scores);
plt.xlabel('Time (seconds elapsed from first transaction)')
plt.ylabel('Amount')
plt.legend(title='Anomaly Scores')
plt.savefig("outlier-scores.png", dpi=150)
plt.show()