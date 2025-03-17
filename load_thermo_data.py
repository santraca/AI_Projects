import pandas as pd

# Load the CSV file
df = pd.read_csv("spacecraft_thermodynamics.csv")

# Display basic info
print(df.head())  # Show first 5 rows
print("\nDataset Summary:")
print(df.describe())  # Show statistics
# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Find when the spacecraft reaches extreme temperatures
extreme_hot = df[df["External Temp (°C)"] > 5]  # High external temp
extreme_cold = df[df["External Temp (°C)"] < -60]  # Low external temp

print("\nExtreme Heat Events:\n", extreme_hot)
print("\nExtreme Cold Events:\n", extreme_cold)
import matplotlib.pyplot as plt
import seaborn as sns

# Line plot of temperature over time
plt.figure(figsize=(8, 5))
sns.lineplot(x="Time (s)", y="Internal Temp (°C)", data=df, label="Internal Temp", color="blue")
sns.lineplot(x="Time (s)", y="External Temp (°C)", data=df, label="External Temp", color="red")
plt.xlabel("Time (seconds)")
plt.ylabel("Temperature (°C)")
plt.title("Spacecraft Temperature Over Time")
plt.legend()
plt.show()

# Scatter plot: Heat Flux vs. Power Consumption
plt.figure(figsize=(6, 4))
sns.scatterplot(x="Heat Flux (W/m²)", y="Power Consumption (W)", data=df, color="green")
plt.xlabel("Heat Flux (W/m²)")
plt.ylabel("Power Consumption (W)")
plt.title("Heat Flux vs. Power Consumption")
plt.show()
