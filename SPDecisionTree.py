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

from sklearn import model_selection
from sklearn.linear_model import LogisticRegression

array = df.values
X = array[:,0:8]
Y = array[:,8]
test_size = 0.33
seed = 7

x_train, x_test, y_train,y_test = model_selection.train_test_split(x, y, test_size=test_size, random_state=seed)
model = LogisticRegression()
model.fit(x_train, y_train)
result = model.score(x_test, y_test)
print("Accuracy: %.3f%%" % (result*100.0))

num_folds = 10
num_instances = len(x)
loocv = model_selection.LeaveOneOut()
model = LogisticRegression()
results = model_selection.cross_val_score(model, x, y, cv=loocv)
print("Accuracy: %.3f%% (%.3f%%)" % (results.mean()*100.0, results.std()*100.0))
