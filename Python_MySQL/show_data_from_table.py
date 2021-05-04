#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 01:58:03 2021

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

mycursor.execute("SELECT * FROM users")

myresult = mycursor.fetchall() # checking all rows

# fetch only one row
# myresult = mycursor.fetchone()


for x in myresult:
    print(x)