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

# check if table exist
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x) 

# create table
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# create primary keys
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") 
