#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 23:41:20 2021
DESCRIBE
@author: lukas
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="lukas-ThinkPad-T440",
  user="root",
  password="password",
  database="sql-kurs"
)

mycursor = mydb.cursor()

# first option scheme
sql = """SELECT COLUMN_NAME
  FROM INFORMATION_SCHEMA.COLUMNS
  WHERE TABLE_SCHEMA = 'sql-kurs' AND TABLE_NAME = 'users';
"""

# second option
sql1 = "SHOW COLUMNS FROM users;"


mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  
