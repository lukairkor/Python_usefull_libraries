#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 16 23:37:01 2021

@author: lukas
"""
import pymysql.cursors

# connecting to database
mydb = pymysql.connect(user='root', password='password',
port = 3306,
host = 'localhost',
database = 'base1',
cursorclass=pymysql.cursors.DictCursor
)