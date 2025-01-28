import pandas as pd 
from sklearn.preprocessing import LabelEncoder

# Create the DataFrame
data = {
    "customer_id": [1, 2, 3, 4],
    "gender": ["Male", "Female", "Female", "Male"]
}
df = pd.DataFrame(data)

print("Original DataFrame")
print(df)

# Initialize the LabelEncoder
label_encoder = LabelEncoder()

# Fit and transform the 'gender' column
df['gender_encoder'] = label_encoder.fit_transform(df['gender'])

print("\nDataFrame with Encoded Gender")
print(df)