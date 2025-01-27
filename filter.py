filtered_transactions = df[df['Transaction_Amount'] > 2000]
print(filtered_transactions)
loan_payment_high_balance = df[(df['Transaction_Type'] == 'Loan Payment') & (df['Account_Balance'] > 5000)]
print(loan_payment_high_balance)
uptown_transactions = df[df['Branch'] == 'Uptown']
print(uptown_transactions)