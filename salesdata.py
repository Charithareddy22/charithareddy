import pandas as pd
import matplotlib.pyplot as plt
try:
    data = pd.read_csv('"C:\Users\G.CHARITHA\Downloads\Day_7_sales_data.csv"')
except FileNotFoundError:
    print("The file 'sales_data.csv' was not found.")
    exit()
print("First 5 rows of the dataset:")
print(data.head())
print("\nBasic statistics of numerical columns:")
print(data.describe())
print("\nMissing values in each column:")
print(data.isnull().sum())
region_sales = data.groupby('Region')['Sales'].sum()
print("\nTotal sales for each region:")
print(region_sales)
most_sold_product = data.groupby('Product')['Quantity'].sum().idxmax()
print("\nMost sold product (based on quantity):", most_sold_product)
data['Profit Margin'] = (data['Profit'] / data['Sales']) * 100
average_profit_margin = data.groupby('Product')['Profit Margin'].mean()
print("\nAverage profit margin for each product:")
print(average_profit_margin)
region_sales.plot(kind='bar', title='Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.show()
average_profit_margin.to_csv('average_profit_margin.csv')