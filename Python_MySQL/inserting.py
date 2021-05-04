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

# inserting single record
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
