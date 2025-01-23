import pandas as pd 
data = {
    'Name': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob'],
    'Age':[25,30,35,20,39],
    'City':['hyd','goa','banglore','hyd','chennai']
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

duplicates = df[df.duplicated()]
print("\nIdentified Duplicates: ")
print(duplicates)

df_cleaned = df.drop_duplicates()
print("\nDataFrame After with Duplicates Removed:")
print(df_cleaned)