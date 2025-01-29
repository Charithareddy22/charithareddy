import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import KNNImputer

# Load the dataset
df = pd.read_csv('C:/Users/G.CHARITHA/Downloads/Day_15_Healthcare_Data.csv')

# Overview of the dataset
print(df.info())
print(df.describe())

# Missing data percentage
missing_percentage = (df.isna().sum() / len(df)) * 100
print("Missing Data Percentage:")
print(missing_percentage)

# Heatmap of missing data
sns.heatmap(df.isna(), cbar=False, cmap='viridis')
plt.title("Missing Data Heatmap")
plt.show()

# Basic imputation
df['numerical_column'] = df['numerical_column'].fillna(df['numerical_column'].mean())
df['categorical_column'] = df['categorical_column'].fillna(df['categorical_column'].mode()[0])

# KNN imputation
knn_imputer = KNNImputer(n_neighbors=5)
df_imputed_knn = pd.DataFrame(knn_imputer.fit_transform(df.select_dtypes(include=['float64', 'int64'])), columns=df.select_dtypes(include=['float64', 'int64']).columns)

# Check for remaining missing values
print("Remaining missing values after KNN Imputation:")
print(df_imputed_knn.isna().sum())

# Comparison of statistics
print("Before KNN Imputation:")
print(df.describe())
print("After KNN Imputation:")
print(df_imputed_knn.describe())

# Boxplot comparison
sns.boxplot(data=[df['numerical_column'], df_imputed_knn['numerical_column']])
plt.xticks([0, 1], ['Before', 'After KNN Imputation'])
plt.title("Comparison of Numerical Column Before and After KNN Imputation")
plt.show()