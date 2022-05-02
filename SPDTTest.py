import SPDecisionTree
from SPDecisionTree import df, x_test, x_train, y_test, y_train, x, y
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