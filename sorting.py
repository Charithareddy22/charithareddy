sorted_by_balance = df.sort_values(by='Account_Balance', ascending=False)
print(sorted_by_balance.head(10))
df['Transaction_Rank'] = df.groupby('Branch')['Transaction_Amount'].rank(ascending=False)
print(df[['Branch', 'Transaction_Amount', 'Transaction_Rank']].head(10))