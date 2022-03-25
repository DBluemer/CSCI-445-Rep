import pandas as pd
newdf = pd.read_csv("datasetf.csv", delimiter=",")

import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
import matplotlib.pyplot as plt


df = newdf.dropna(axis=0)

y = df['Source']
x = df[['DNS_TTL','IP_TTL','Time','Length']].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=3)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

offenseTree = DecisionTreeClassifier(criterion="entropy", max_depth=4)

df = df.reset_index()

offenseTree.fit(x_train, y_train)
predicted = offenseTree.predict(x_test)

print(predicted)

print("\nDecisionTrees's Accuracy: ", metrics.accuracy_score(y_test, predicted))

model = DecisionTreeClassifier()

model.fit(x_train, y_train)

predictions = model.predict(x_train)

from sklearn.metrics import classification_report

from sklearn.metrics import confusion_matrix

print(classification_report(y_train, predictions))

print(confusion_matrix(y_train, predictions))

from sklearn import preprocessing

x_train = np.array([[ 1., -1.,  2.],
                    [ 2.,  0.,  0.],
                   [ 0.,  1., -1.]])
scaler = preprocessing.StandardScaler().fit(x_train)
scaler

X_scaled = scaler.transform(x_train)
X_scaled

from sklearn.linear_model import LogisticRegression
from sklearn import model_selection

kfold = model_selection.KFold(n_splits=10, random_state=None)
model = LogisticRegression()
results = model_selection.cross_val_score(model, x_test, y_test, cv=kfold)
print("Accuracy: %.3f%% (%.3f%%)" % (results.mean()*100.0, results.std()*100.0))
