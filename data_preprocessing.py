import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Create dataset
data = {
    'Age': [20, 25, None, 30],
    'Salary': [20000, 30000, 25000, 40000],
    'City': ['Indore', 'Bhopal', 'Indore', 'Bhopal']
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Convert categorical data into numbers
le = LabelEncoder()
df['City'] = le.fit_transform(df['City'])

# Feature scaling
scaler = StandardScaler()
df[['Age', 'Salary']] = scaler.fit_transform(df[['Age', 'Salary']])

print("\nPreprocessed Data:")
print(df)
