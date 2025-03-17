import pandas as pd

# Create a simple dataset
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 70000]}

df = pd.DataFrame(data)

df["Bonus"] = df["Salary"] * 0.10

df["Bruto"] = df["Salary"] + df["Bonus"]

print("\nUpdated DataFrame:\n", df)
print("\n")