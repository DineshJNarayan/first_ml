## please use 'conda activate test_env' before running script with 'python3 iris.py'

import pandas
import mysql.connector

# Load libraries
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Load dataset
mydb = mysql.connector.connect  (   host="127.0.0.1", user="root", password="Vmcp2020Gain", database="MachineLearning"  )
mycursor = mydb.cursor()
query = "SELECT sepal_length, sepal_width, petal_length, petal_width, class FROM iris_ml"
mycursor.execute(query)
records = mycursor.fetchall()
dataset = pandas.DataFrame(records)
dataset.columns = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset['sepal-length'] = pandas.to_numeric(dataset['sepal-length'])
dataset['sepal-width'] = pandas.to_numeric(dataset['sepal-width'])
dataset['petal-length'] = pandas.to_numeric(dataset['petal-length'])
dataset['petal-width'] = pandas.to_numeric(dataset['petal-width'])

# shape
print(dataset.shape)
# head
print(dataset.head(20))
# descriptions
print(dataset.describe())

# box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
pyplot.show()

# histograms
dataset.hist()
pyplot.show()

# scatter plot matrix
scatter_matrix(dataset)
pyplot.show()

# Split-out validation dataset
array = dataset.values
# Extract all data from columns sepal_length, sepal_width, petal_length, petal_width 
X = array[:,0:4]
# Extract all data from column class 
Y = array[:,4]
# Split the data set into training data & validation data - 80% training, 20% testing
X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y, train_size=0.80, test_size=0.20, random_state=1)
# X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y, train_size=0.80, test_size=0.20)

# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))

# evaluate each model in turn
results = []
names = []
for name, model in models:
	kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
	cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
	results.append(cv_results)
	names.append(name)
	print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))

# Compare Algorithms
pyplot.boxplot(results, labels=names)
pyplot.title('Algorithm Comparison')
pyplot.show()

# Make predictions on validation dataset
model = SVC(gamma='auto')
model.fit(X_train, Y_train)
predictions = model.predict(X_validation)

# Evaluate predictions
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))