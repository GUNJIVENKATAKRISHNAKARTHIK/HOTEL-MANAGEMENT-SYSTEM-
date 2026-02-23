import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("C:\\Users\\poorn\\OneDrive\\Desktop\\diabetes_merged_date-time-sorted-includes-patient-id.csv")
print(df.head())
print(df.describe())

print(df['glucose'].mean())
print(df.median())
print(df.mode())
print(df.var())
print(df.skew())
print(df.kurtosis())
