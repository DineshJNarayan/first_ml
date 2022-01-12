## please use 'conda activate test_env' before running script with 'python3 insert_mysql.py' -> 11-01-2022

import mysql.connector
import pandas as pd
# Load libraries
from pandas import read_csv

#url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
#names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
#dataset = read_csv(url, names=names)
#df = pd.DataFrame(dataset)

def insert_variables_into_table(sepal_length, sepal_width, petal_length, petal_width, iris_class):
    try:
        mydb = mysql.connector.connect(host="127.0.0.1", user="root", password="Vmcp2020Gain", database="MachineLearning")
        mycursor = mydb.cursor()
        ## sql = "INSERT INTO iris_ml (sepal_length, sepal_width, petal_length, petal_width, class) VALUES (%s, %s, %s, %s, %s)" 
        ## val = (row['sepal_length'], row['sepal_width'], row['petal_length'], row['petal_width'], row['class']) 
        ## mycursor.execute(sql, val)
        ## mydb.commit()
        print(sepal_length, sepal_width, petal_length, petal_width, iris_class) 
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))
    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()
            print("MySQL connection is closed")

#for index, row in df.iterrows():
#    insert_variables_into_table(row['sepal_length'], row['sepal_width'], row['petal_length'], row['petal_width'], row['class'])

names = ['pregnancies', 'glucose', 'bloodpressure', 'skinthickness', 'insulin', 'bmi', 'diabetespedigree', 'age', 'outcome']
dataset = read_csv("pima-indians-diabetes.csv", names=names)
df = pd.DataFrame(dataset)

print(df)

def insert_variables_into_table(pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigree, age, outcome):
    try:
        mydb = mysql.connector.connect(host="127.0.0.1", user="root", password="Vmcp2020Gain", database="DiabetesData")
        mycursor = mydb.cursor()
        ## sql = "INSERT INTO iris_ml (pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigree, age, outcome) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)" 
        ## val = (row['pregnancies'], row['glucose'], row['bloodpressure'], row['skinthickness'], row['insulin'], row['bmi'], row['diabetespedigree'], row['age'], row['outcome']) 
        ## mycursor.execute(sql, val)
        ## mydb.commit()
        print(pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigree, age, outcome) 
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))
    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()
            print("MySQL connection is closed")

#for index, row in df.iterrows():
#    insert_variables_into_table(row['pregnancies'], row['glucose'], row['bloodpressure'], row['skinthickness'], row['insulin'], row['bmi'], row['diabetespedigree'], row['age'], row['outcome'])
