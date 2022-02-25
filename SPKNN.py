from re import X
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn 

raw_data = pd.read_csv('datasetf.csv')
print(raw_data)

def convertToFloat(row):
    X = raw_data[['Destination','Length','Qname','QType','DNS_TTL']].values
    
    newArray = []
    for i, r in enumerate(row):
            if i == 0:
                newArray.append(r)
                continue
            if i == len(row) - 1:
                newArray.append(r)
                break
            newArray.append(float(r))
    return newArray

def convertToFloat(column):
    y = raw_data[['Source']].values
    newArray = []
    for i, c in enumerate(column):
            if i == 0:
                newArray.append(c)
                continue
            if i == len(column) - 1:
                newArray.append(c)
                break
            newArray.append(float(c))
    return newArray

from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X, y)