import pandas as pd

# Load the CSV file
df = pd.read_csv("spacecraft_thermodynamics.csv")

# Display basic info
print(df.head())  # Show first 5 rows
print("\nDataset Summary:")
print(df.info())  # Show statistics
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

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Compute correlation matrix
correlation_matrix = df.corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

# Heatmap of correlations
plt.figure(figsize=(6,4))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Feature Correlations")
plt.show()

# Rolling average of temperature (to smooth fluctuations)
df["Internal Temp Rolling"] = df["Internal Temp (°C)"].rolling(window=10).mean()
df["External Temp Rolling"] = df["External Temp (°C)"].rolling(window=10).mean()

# Plot rolling temperatures
plt.figure(figsize=(8,5))
sns.lineplot(x="Time (s)", y="Internal Temp Rolling", data=df, label="Internal Temp", color="blue")
sns.lineplot(x="Time (s)", y="External Temp Rolling", data=df, label="External Temp", color="red")
plt.xlabel("Time (seconds)")
plt.ylabel("Smoothed Temperature (°C)")
plt.title("Smoothed Spacecraft Temperature Over Time")
plt.legend()
plt.show()

from sklearn.ensemble import IsolationForest

# Select features for anomaly detection
features = ["Internal Temp (°C)", "External Temp (°C)", "Heat Flux (W/m²)", "Power Consumption (W)"]
X = df[features]

# Train Isolation Forest model (anomaly detection)
model = IsolationForest(contamination=0.05, random_state=42)
df["Anomaly"] = model.fit_predict(X)

# Convert anomalies (-1 = anomaly, 1 = normal)
df["Anomaly"] = df["Anomaly"].apply(lambda x: "Anomaly" if x == -1 else "Normal")

# Show flagged anomalies
anomalies = df[df["Anomaly"] == "Anomaly"]
print("\nDetected Anomalies:")
print(anomalies)

# Scatter plot showing anomalies
plt.figure(figsize=(6,4))
sns.scatterplot(x="Time (s)", y="Heat Flux (W/m²)", data=df, hue="Anomaly", palette={"Normal": "blue", "Anomaly": "red"})
plt.title("Anomaly Detection in Heat Flux")
plt.show()
