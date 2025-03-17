import pandas as pd

# Load the CSV file
df = pd.read_csv("spacecraft_thermodynamics.csv")

# Display basic info
print(df.head())  # Show first 5 rows
print("\nDataset Summary:")
print(df.describe())  # Show statistics
