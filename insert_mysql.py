import mysql.connector
import pandas as pd
# Load libraries
from pandas import read_csv

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
dataset = read_csv(url, names=names)
df = pd.DataFrame(dataset)

def insert_variables_into_table(sepal_length, sepal_width, petal_length, petal_width, iris_class):
    try:
        mydb = mysql.connector.connect(host="127.0.0.1", user="root", password="Vmcp2020Gain", database="MachineLearning")
        mycursor = mydb.cursor()
        sql = "INSERT INTO iris_ml (sepal_length, sepal_width, petal_length, petal_width, class) VALUES (%s, %s, %s, %s, %s)" 
        val = (row['sepal_length'], row['sepal_width'], row['petal_length'], row['petal_width'], row['class']) 
        mycursor.execute(sql, val)
        mydb.commit()
        print(sepal_length, sepal_width, petal_length, petal_width, iris_class) 
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))
    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()
            print("MySQL connection is closed")

for index, row in df.iterrows():
    insert_variables_into_table(row['sepal_length'], row['sepal_width'], row['petal_length'], row['petal_width'], row['class'])
