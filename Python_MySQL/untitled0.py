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

sql = "SELECT * FROM users WHERE username ='Jan'"

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)