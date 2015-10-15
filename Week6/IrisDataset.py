# load datasets
from sklearn import datasets

# load the iris datasets
iris = datasets.load_iris()
print iris.keys()
print iris.target_names
print iris['target_names']

# Iris features
c = 0
print "\n", iris.feature_names 
for data in iris.data:
	print data
	if c == 4: break
	else: c = c + 1
	
# Iris targets
c = 0
print "\n", iris.target_names
for data in iris.target:
	print data
	if c == 4: break
	else: c = c + 1
	
##show plot
import numpy as np
import matplotlib.pyplot as plt

x_index = 2
y_index = 3

# this formatter will label the colorbar with the correct target names
formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])

plt.scatter(iris.data[:, x_index], iris.data[:, y_index],
            c=iris.target)
plt.colorbar(ticks=[0, 1, 2], format=formatter)
plt.xlabel(iris.feature_names[x_index])
plt.ylabel(iris.feature_names[y_index])
plt.show()
