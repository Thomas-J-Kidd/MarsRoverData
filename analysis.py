import pandas as pd

# Read the CSV file into a pandas DataFrame
csv_file = "REMS_Mars_Dataset.csv"  # Replace with the actual path to your CSV file
df = pd.read_csv(csv_file)

# Display basic information about the DataFrame
print("DataFrame Summary:")
print(df.info())

# Display the first few rows of the DataFrame (head)
print("\nFirst few rows of the DataFrame:")
print(df.head())

# Display statistical summary of numerical columns
print("\nStatistical Summary:")
print(df.describe())

# Display unique values in the 'weather' column
print("\nUnique Weather Categories:")
print(df['weather'].unique())

