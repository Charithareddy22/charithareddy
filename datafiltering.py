filtered_sales = df[df['Sales'] > 1000]
region_sales = df[df['Region'] == 'East']

#DataPreprocessing

df['Profit_Per_Unit'] = df['Profit'] / df['Quantity']
df['High_Sales'] = df['Sales'].apply(lambda x: 'Yes' if x > 1000 else 'No')