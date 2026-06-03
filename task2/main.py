import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\decodelabs_intership\task2\StudentsPerformance.csv")

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values with 0
df = df.fillna(0)

# Display cleaned data
print("CLEANED DATA")
print(df.head())

# Check missing values
print("\nMISSING VALUES AFTER CLEANING")
print(df.isnull().sum())