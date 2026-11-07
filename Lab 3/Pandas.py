import pandas as pd

# Create a dictionary
data = {
    'Name': ['Amit', 'Riya', 'Rahul', 'Priya'],
    'Age': [20, 21, 22, 20],
    'Marks': [85, 90, 75, 95]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display complete data
print("Student Data:")
print(df)

# Display first two rows
print("\nFirst Two Rows:")
print(df.head(2))

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Display a particular column
print("\nStudent Names:")
print(df['Name'])

# Calculate average marks
print("\nAverage Marks:", df['Marks'].mean())

# Find maximum marks
print("Maximum Marks:", df['Marks'].max())





