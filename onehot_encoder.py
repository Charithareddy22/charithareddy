import pandas as pd
from sklearn.preprocessing import OneHotEncoder
data = {
    "customer_id": [1, 2, 3, 4],
    "gender": ["Male", "Female", "Female", "Male"],
    "city": ["New York", "Los Angeles", "New York", "Chicago"]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
one_hot_encoder = OneHotEncoder(sparse_output=False)
columns_to_encode = ["gender", "city"]
encoded_data = one_hot_encoder.fit_transform(df[columns_to_encode])
encoded_columns = one_hot_encoder.get_feature_names_out(columns_to_encode)
encoded_df = pd.DataFrame(encoded_data, columns=encoded_columns)
print("\nEncoded DataFrame:")
print(encoded_df)
final_df = pd.concat([df, encoded_df], axis=1)
print("\nFinal DataFrame with Encoded Columns:")
print(final_df)