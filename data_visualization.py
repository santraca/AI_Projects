import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create the DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 70000]}

df = pd.DataFrame(data)

# Add new columns
df["Bonus"] = df["Salary"] * 0.10
df["Bruto"] = df["Salary"] + df["Bonus"]

# Create a bar chart (Salary vs Name)
plt.figure(figsize=(6, 4))
sns.barplot(x="Name", y="Salary", data=df, palette="viridis")
plt.title("Salary Distribution")
plt.ylabel("Salary ($)")
plt.xlabel("Employees")
plt.show()
# Histogram of Salaries
plt.figure(figsize=(6, 4))
sns.histplot(df["Salary"], bins=5, kde=True, color="blue")
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Count")
plt.show()

# Scatter Plot (Age vs Salary)
plt.figure(figsize=(6, 4))
sns.scatterplot(x="Age", y="Salary", data=df, color="red", s=100)
plt.title("Salary vs Age")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()
