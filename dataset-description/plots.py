#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt

with open('../datasets/electricity-normalized.arff', 'r') as file:
    arff_content = file.readlines()

# Find the start of the data section
data_start_index = arff_content.index('@data\n') + 1
data_lines = arff_content[data_start_index:]

# Parse the data lines into a DataFrame
data = [line.strip().split(',') for line in data_lines if line.strip() != '']
df = pd.DataFrame(data, columns=['date',
                                 'day',
                                 'period',
                                 'nswprice',
                                 'nswdemand',
                                 'vicprice',
                                 'vicdemand',
                                 'transfer',
                                 'class'])

df["date"]=pd.to_numeric(df["date"])
df["day"]=pd.to_numeric(df["day"])
df["period"]=pd.to_numeric(df["period"])
df["nswprice"]=pd.to_numeric(df["nswprice"])
df["nswdemand"]=pd.to_numeric(df["nswdemand"])
df["vicprice"]=pd.to_numeric(df["vicprice"])
df["vicdemand"]=pd.to_numeric(df["vicdemand"])
df["transfer"]=pd.to_numeric(df["transfer"])



def plot(xValues='nswdemand', yValues='nswprice'):
    plt.figure(figsize=(12, 6))
    
    # Filtering the DataFrame for 'UP' and 'DOWN' classes
    up_df = df[df['class'] == 'UP']
    down_df = df[df['class'] == 'DOWN']
    
    # Plotting 'UP' points in pink
    plt.scatter(up_df[xValues], up_df[yValues], color='pink', label='Class UP', alpha=0.5)
    
    # Plotting 'DOWN' points in blue
    plt.scatter(down_df[xValues], down_df[yValues], color='blue', label='Class DOWN', alpha=0.5)
    
    plt.title(f'{yValues} vs. {xValues} by Class')
    plt.xlabel(xValues)
    plt.ylabel(yValues)
    plt.legend()
    plt.grid(True)
    plt.show()

plot("nswdemand", "nswprice")
plot("vicdemand", "vicprice")
