import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Healthcare Data
data = {
    'Age': [45, 50, 36, 29, 60],
    'Blood_Pressure': [140, 130, 150, 120, 160],
    'Cholesterol': [220, 210, 240, 180, 260]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display Data
print("Healthcare Dataset:")
print(df)

# Basic Statistics
print("\nStatistical Summary:")
print(df.describe())

# Plot Age Distribution
plt.figure(figsize=(6,4))
sns.histplot(df['Age'], bins=5, kde=True)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")

plt.show()

print("\nHealthcare Data Analysis Completed Successfully.")
