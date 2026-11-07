import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a dataset
data = {
    'Name': ['Amrita', 'Reeya', 'Rahul', 'Piya', 'Nehal'],
    'Age': [22,24,26,21,20],
    'Marks': [85,88,57,68,80]
}

df = pd.DataFrame(data)

# Display dataset
print("Dataset:")
print(df)

# Display first five rows
print("\nFirst 5 rows are:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate values
print("\nDuplicate Values:")
print(df.duplicated().sum())

# Visualize data using histogram
plt.hist(df['Marks'], bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# Visualize data using boxplot
sns.boxplot(x=df['Marks'])
plt.title("Marks Boxplot")
plt.show()
