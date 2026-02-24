import numpy as np

from aif360.datasets import GermanDataset
from aif360.metrics import BinaryLabelDatasetMetric
from aif360.algorithms.preprocessing import Reweighing

np.random.seed(0)


# Load the German Credit dataset
# We define 'age' as the protected attribute.
# Privileged group: Age >= 25
# Unprivileged group: Age < 25
dataset_orig = GermanDataset(
    protected_attribute_names=['age'],           
    privileged_classes=[lambda x: x >= 25],      
    features_to_drop=['personal_status', 'sex'] 
)

dataset_orig_train, dataset_orig_test = dataset_orig.split([0.7], shuffle=True)


# Define privileged and unprivileged groups
privileged_groups = [{'age': 1}]
unprivileged_groups = [{'age': 0}]

metric_orig_train = BinaryLabelDatasetMetric(dataset_orig_train,
                                            unprivileged_groups=unprivileged_groups,
                                            privileged_groups=privileged_groups)

print("\n \n --- Original Training Dataset ---")
print("Difference in mean outcomes (Mean Difference) = %f" % metric_orig_train.mean_difference())

# Positive outcome rate for privileged and unprivileged groups in the original training dataset before applying the Reweighing algorithm
privileged_positive_rate = metric_orig_train.base_rate()
unprivileged_positive_rate = metric_orig_train.base_rate(privileged=False)

# Display the positive outcome rates for privileged and unprivileged groups in the original training dataset before applying the Reweighing algorithm.
print("Positive outcome rate for privileged group = %.2f%%" % (privileged_positive_rate * 100))
print("Positive outcome rate for unprivileged group = %.2f%%" % (unprivileged_positive_rate * 100))


# Apply the Reweighing algorithm to the training dataset to mitigate bias before classification.
RW = Reweighing(unprivileged_groups=unprivileged_groups,
                privileged_groups=privileged_groups)
dataset_transf_train = RW.fit_transform(dataset_orig_train)

# Calculate the mean difference metric after reweighing the training dataset to check the bias in the transformed training dataset
metric_transf_train = BinaryLabelDatasetMetric(dataset_transf_train,
                                              unprivileged_groups=unprivileged_groups,
                                              privileged_groups=privileged_groups)

print("\n \n --- Transformed Training Dataset (After Reweighing) ---")
print("Difference in mean outcomes (Mean Difference) = %f" % metric_transf_train.mean_difference())

# Positive outcome rate for privileged and unprivileged groups in the transformed training dataset after applying the Reweighing algorithm
privileged_positive_rate_transf = metric_transf_train.base_rate()   
unprivileged_positive_rate_transf = metric_transf_train.base_rate(privileged=False)

print("Positive outcome rate for privileged group = %.2f%%" % (privileged_positive_rate_transf * 100))
print("Positive outcome rate for unprivileged group = %.2f%%" % (unprivileged_positive_rate_transf * 100))
print("\n \n ")