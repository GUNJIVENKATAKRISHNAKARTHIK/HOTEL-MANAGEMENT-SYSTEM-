import pandas as pd

# Read Iris dataset from the web
##url = "https://raw.githubusercontent.com//uiuc-cse//data-fa1//gh-pages//data//iris.csv"
df =pd.read_csv(

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head())
# Mean of numeric columns
print("\nMean of numeric columns:")
print(df.mean(numeric_only=True))

# Median of numeric columns
print("\nMedian of numeric columns:")
print(df.median(numeric_only=True))

# Mode of numeric columns
print("\nMode of numeric columns:")
print(df.mode(numeric_only=True).iloc[0])