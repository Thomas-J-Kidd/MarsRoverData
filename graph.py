import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt
from dateutil.parser import parse

# Read the CSV file into a pandas DataFrame
csv_file = "REMS_Mars_Dataset.csv"  # Replace with the actual path to your CSV file
df = pd.read_csv(csv_file)

# Extract the date part of the "earth_date_time" column
df['earth_date_time'] = df['earth_date_time'].apply(lambda x: x.split(', ')[1])

# Create the plot
plt.figure(figsize=(10, 6))

# Plot "max_ground_temp(°C)" against time (date component)
plt.plot(df['earth_date_time'], df['max_ground_temp(°C)'], marker='o', linestyle='-')

# Set the axis labels and title
plt.xlabel('Date')
plt.ylabel('Max Ground Temperature (°C)')
plt.title('Max Ground Temperature over Time')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()
