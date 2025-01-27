import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("banking_data.csv")
print(df.head())
print(df.describe())
print(df.isnull().sum())