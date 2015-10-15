from sklearn.ensemble import RandomForestClassifier
import pandas as pd
# credit goes to Ben Solecki
# https://github.com/bensolucky/Amazon/blob/master/SklearnDemo.ipynb
# pandas makes reading csv data very easy
train = pd.read_csv('train.csv')
valid = pd.read_csv('test.csv', index_col='id') # Test data has an id column, train does not.

# Break the training data into a target ("dependent") and inputs ("inpedendents")
y = train.ACTION
X = train.drop(["ACTION"], axis=1)
print X.head()
print y.head()
# Define the model random forest's defaults and then fit it to the training data
model = RandomForestClassifier()
model.fit(X, y)

print "Train Dimensions:", train.shape[0], "rows and", train.shape[1], "columns"
print "Valid Dimensions:", valid.shape[0], "rows and", valid.shape[1], "columns"
# Predict the fitted model on the test data and output predictions to a csv
submission = pd.DataFrame(columns=['ACTION'], index=valid.index, data=model.predict_proba(valid)[:, 1])
submission.to_csv("simple_submission.csv")

# Now submit to Kaggle - the score should almost crack the top 1000 and 0.80
# The scoring metric used is "Area Under the ROC Curve". It is bounded by 0 and 1
# For one of many online explanations try http://gim.unmc.edu/dxtests/roc3.htm
