import matplotlib.pyplot as plt

# Group the data by Account_Type and sum Transaction_Amount
total_transaction_by_account_type = df.groupby('Account_Type')['Transaction_Amount'].sum()

# Plot a bar plot
total_transaction_by_account_type.plot(kind='bar', color='skyblue', figsize=(8, 5))
plt.title('Total Transaction Amount per Account Type')
plt.xlabel('Account Type')
plt.ylabel('Total Transaction Amount')
plt.xticks(rotation=45)
plt.show()

#PieChart

# Group the data by Branch and count the number of transactions
transaction_count_by_branch = df['Branch'].value_counts()

# Plot a pie chart
transaction_count_by_branch.plot(kind='pie', autopct='%1.1f%%', figsize=(7, 7), startangle=90, cmap='tab20')
plt.title('Percentage of Transactions per Branch')
plt.ylabel('')  # Remove the y-axis label for better visualization
plt.show()