# AutoEncoder for Fraud Detection

This project uses an AutoEncoder neural network to detect fraudulent credit card transactions.

## High-Level Explanation

The `detect_fraud.py` script loads a dataset of credit card transactions from `creditcard.csv`. It then builds and trains an AutoEncoder model using the `pyod` library. The trained model is used to identify outliers in the dataset, which are considered potentially fraudulent transactions. Finally, the script generates a scatter plot to visualize the outlier scores.

## Packages Needed

To run the script, you will need to have the following Python packages installed:

*   pandas
*   numpy
*   matplotlib
*   seaborn
*   pyod

You can install these packages using pip:

```bash
pip install pandas numpy matplotlib seaborn pyod
```

## Execution Instructions

1.  Make sure you have the required packages installed.
2.  Download the `creditcard.csv` dataset and place it in the same directory as the `detect_fraud.py` script.
3.  Run the script from your terminal:

```bash
python detect_fraud.py
```

The script will train the model, print the outlier scores, and save a scatter plot of the results as `outlier-scores.png`.
