import mysql.connector
# Load libraries
from pandas import read_csv

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Vmcp2020Gain",
  database="MachineLearning"
)

mycursor = mydb.cursor()

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
dataset = read_csv(url, names=names)

sql = "INSERT INTO customers (name, address) VALUES (%s, %s, %s, %s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")