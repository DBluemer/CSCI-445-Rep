import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn 

from sklearn.model_selection import train_test_split

raw_data = pd.read_csv('datasetf.csv')

y = raw_data['Source']

x = raw_data[['Destination','Time','Length','domain_length']].values

x_training_data, x_test_data, y_training_data, y_test_data = train_test_split(x, y, test_size = 0.3)

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3)

model.fit(x_training_data, y_training_data)

predictions = model.predict(x_test_data)
