import pandas as pd
import matplotlib.pyplot as plt

with open('electricity-normalized.arff', 'r') as file:
    arff_content = file.readlines()

# Find the start of the data section
data_start_index = arff_content.index('@data\n') + 1
data_lines = arff_content[data_start_index:]

# Parse the data lines into a DataFrame
data = [line.strip().split(',') for line in data_lines if line.strip() != '']
df = pd.DataFrame(data, columns=['date', 'day', 'period', 'nswprice', 'nswdemand', 'vicprice', 'vicdemand', 'transfer', 'class'])

# Convert 'period', 'nswdemand', and 'day' to numeric for plotting
df['period'] = pd.to_numeric(df['period'])
df['nswdemand'] = pd.to_numeric(df['nswdemand'])
df['day'] = pd.to_numeric(df['day'])

# Creating a figure for the plot
plt.figure(figsize=(12, 6))

# Code snipped for coloring points for different days with different colors
# Define a color for each day
# colors = {1: 'red', 2: 'orange', 3: 'yellow', 4: 'green', 5: 'blue', 6: 'indigo', 7: 'violet'}
# Loop through each day, plotting demand vs. period points with the corresponding day color
#for day, group in df.groupby('day'):
#   plt.scatter(group['period'], group['nswdemand'], label=f'Day {day}', alpha=0.5, color=colors[day])

plt.scatter(df['period'], df['nswdemand'])

plt.title('Demand over Period by Day of the Week')
plt.xlabel('Normalized Period (0-1)')
plt.ylabel('Demand')
plt.legend(title='Day of the Week', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()



