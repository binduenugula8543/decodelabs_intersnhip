import pandas as pd
import matplotlib.pyplot as plt

# ---------------- TASK 1 ----------------
# Dataset Understanding

# Load dataset
df = pd.read_csv(r"C:\Users\bindu\Downloads\archive\StudentsPerformance.csv")

# Display first 5 rows
print("FIRST 5 ROWS")
print(df.head())

# Dataset shape
print("\nDATASET SHAPE")
print(df.shape)

# Column names
print("\nCOLUMNS")
print(df.columns)

# Data types
print("\nDATA TYPES")
print(df.dtypes)

# Missing values
print("\nMISSING VALUES")
print(df.isnull().sum())


