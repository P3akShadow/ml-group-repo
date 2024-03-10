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

df["nswdemand"]=pd.to_numeric(df["nswdemand"])
df["nswprice"]=pd.to_numeric(df["nswprice"])

plt.figure(figsize=(12, 6))

# Filtering the DataFrame for 'UP' and 'DOWN' classes
up_df = df[df['class'] == 'UP']
down_df = df[df['class'] == 'DOWN']

# Plotting 'UP' points in pink
plt.scatter(up_df['nswdemand'], up_df['nswprice'], color='pink', label='Class UP', alpha=0.5)

# Plotting 'DOWN' points in blue
plt.scatter(down_df['nswdemand'], down_df['nswprice'], color='blue', label='Class DOWN', alpha=0.5)

plt.title('Price vs. Demand by Class')
plt.xlabel('Demand')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()
