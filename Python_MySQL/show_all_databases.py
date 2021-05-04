#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 00:26:51 2021

@author: lukas
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="lukas-ThinkPad-T440",
  user="root",
  password="password"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x) 