#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 23:31:50 2021

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

# filtering
sql = "SELECT * FROM users WHERE username ='Jan'"
sql1 = "SELECT * FROM users WHERE year_of_birth LIKE '%6%'"
# mycursor.execute(sql1)

# injection prevention
sql2 = "SELECT * FROM users WHERE username = %s"
address = ("Lukasz", )
mycursor.execute(sql2, address)

# execute
myresult = mycursor.fetchall()
for x in myresult:
  print(x)