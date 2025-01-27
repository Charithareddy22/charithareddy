df['Transaction_Fee'] = df['Transaction_Amount'] * 0.02
print(df[['Transaction_Amount', 'Transaction_Fee']].head())
df['Balance_Status'] = df['Account_Balance'].apply(lambda x: 'High Balance' if x > 5000 else 'Low Balance')
print(df[['Account_Balance', 'Balance_Status']].head())