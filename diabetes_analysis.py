## please use 'conda activate test_env' before running script with 'python3 diabetes_analysis.py'

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
query = "SELECT pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigree, age, outcome FROM diabetes_data"
mycursor.execute(query)
records = mycursor.fetchall()
dataset = pandas.DataFrame(records)
dataset.columns = ['pregnancies', 'glucose', 'bloodpressure', 'skinthickness', 'insulin', 'bmi', 'diabetespedigree', 'age', 'outcome']
dataset['pregnancies'] = pandas.to_numeric(dataset['pregnancies'])
dataset['glucose'] = pandas.to_numeric(dataset['glucose'])
dataset['bloodpressure'] = pandas.to_numeric(dataset['bloodpressure'])
dataset['skinthickness'] = pandas.to_numeric(dataset['skinthickness'])
dataset['insulin'] = pandas.to_numeric(dataset['insulin'])
dataset['bmi'] = pandas.to_numeric(dataset['bmi'])
dataset['diabetespedigree'] = pandas.to_numeric(dataset['diabetespedigree'])
dataset['age'] = pandas.to_numeric(dataset['age'])
dataset['outcome'] = pandas.to_numeric(dataset['outcome'])

# shape
print(dataset.shape)
# head
print(dataset.head(20))
# descriptions
print(dataset.describe())

# box and whisker plots
dataset.plot(kind='density', subplots=True, layout=(3,3), sharex=False)
pyplot.show()

# histograms
dataset.hist()
pyplot.show()

# scatter plot matrix
scatter_matrix(dataset)
pyplot.show()

# box plot
dataset.plot(kind='box', subplots=True, layout=(3,3), sharex=False,sharey=False)
pyplot.show()