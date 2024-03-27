import pandas as pd
#from sklearn.ensemble._forest import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

with open(os.path.join('..', 'datasets', 'dataset_42_soybean.arff'), 'r') as file:
    arff_content = file.readlines()

# Find the start of the data section
data_start_index = arff_content.index('@DATA\n') + 1
data_lines = arff_content[data_start_index:]

# Parse the data lines into a DataFrame
data = [[value.strip() for value in line.strip().split(',')] for line in data_lines if line.strip() != '' and line[0] != "%"]
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

# data preparation first



# X = df_soybean.drop(columns="class")
# Y = df_soybean["class"]
# X_train, Y_train, X_test, Y_test = train_test_split(X, Y, test_size=0.3)

# machine = DecisionTreeClassifier()
# machine.fit(X_train.values, Y_train.values)

# predictions = machine.predict([X_test])
# precision = accuracy_score(Y_test, predictions)
# predictions
# precision

