# Support Vector Machine
from sklearn import datasets
from sklearn import metrics
from sklearn.svm import SVC
# load the iris datasets
iris = datasets.load_iris()
print iris.keys()
print iris.target_names

# fit a SVM model to the data
model = SVC()
model.fit(iris.data, iris.target)
#print(model)
# make predictions
expected = iris.target
predicted = model.predict(iris.data)
# summarize the fit of the model
#print(metrics.classification_report(expected, predicted))
#print(metrics.confusion_matrix(expected, predicted))
