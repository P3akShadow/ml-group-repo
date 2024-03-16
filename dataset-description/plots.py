#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt
import os

with open(os.path.join('..', 'datasets', 'electricity-normalized.arff'), 'r') as file:
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


with open(os.path.join('..', 'datasets', 'dataset_42_soybean.arff'), 'r') as file:
    arff_content = file.readlines()

# Find the start of the data section
data_start_index = arff_content.index('@DATA\n') + 1
data_lines = arff_content[data_start_index:]

# Parse the data lines into a DataFrame
data = [line.strip().split(',') for line in data_lines if line.strip() != '']
df_soybean = pd.DataFrame(data, columns=['date',
                                        'plant-stand',
                                        'precip',
                                        'temp',
                                        'hail',
                                        'crop-hist',
                                        'area-damaged',
                                        'severity',
                                        'seed-tmt',
                                        'germination',
                                        'plant-growth',
                                        'leaves',
                                        'leafspots-halo',
                                        'leafspots-marg',
                                        'leafspot-size',
                                        'leaf-shread',
                                        'leaf-malf',
                                        'leaf-mild',
                                        'stem',
                                        'lodging',
                                        'stem-cankers',
                                        'canker-lesion',
                                        'fruiting-bodies',
                                        'external-decay',
                                        'mycelium',
                                        'int-discolor',
                                        'sclerotia',
                                        'fruit-pods',
                                        'fruit-spots',
                                        'seed',
                                        'mold-growth',
                                        'seed-discolor',
                                        'seed-size',
                                        'shriveling',
                                        'roots',
                                        'class'])

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

def histogram(xValues='nswdemand'):

    plt.hist(df[xValues], color='skyblue', edgecolor='black')
    plt.xlabel(xValues)
    plt.ylabel('frequency')
    plt.title(f'frequency of {xValues}')
    plt.show()

def soybean_histogram(xValues="date"):

    #reset index takes different indices and makes them the first line
    counts = df_soybean[xValues].value_counts().reset_index().set_axis(["value", "count"], axis=1)
    print(counts)
    
    plt.bar(counts["value"], counts["count"], color='green')
    plt.xlabel(xValues)
    plt.ylabel('frequency')
    plt.title(f'frequency of {xValues}')
    plt.show()


def main():
    #plot("nswdemand", "nswprice")
    #plot("vicdemand", "vicprice")
    #histogram()
    soybean_histogram()

if __name__ == "__main__":
    main()
