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
df["vicprice"]=pd.to_numeric(df["vicprice"])

plt.figure(figsize=(12, 6))

plt.scatter(df['nswdemand'], df['vicprice'], color='blue', label='NSW and VIC price relation', alpha=0.5)


plt.title('Price vs. Demand by Class')
plt.xlabel('NSW Price')
plt.ylabel('VIC Price')
plt.legend()
plt.grid(True)
plt.show()
