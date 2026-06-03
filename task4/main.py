import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\decodelabs_intership\task4\StudentsPerformance.csv")

# Create histogram
df["math score"].hist()

# Add labels
plt.title("Math Score Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

# Show graph
plt.show()