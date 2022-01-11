## please use 'conda activate test_env' before running script 'python3 iris.py' -> 11-01-2022

# make predictions
import pandas
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import mysql.connector

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

# Split-out validation dataset
array = dataset.values
X = array[:,0:4]
y = array[:,4]
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)
# Make predictions on validation dataset
model = SVC(gamma='auto')
model.fit(X_train, Y_train)
predictions = model.predict(X_validation)
# Evaluate predictions
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))