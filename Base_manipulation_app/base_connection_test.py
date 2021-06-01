#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 16 23:37:01 2021

@author: lukas
"""
import mysql.connector

# connecting to database
mydb = mysql.connector.connect(user='root', password='16741674',
port = 3306,
host = 'localhost',
database = 'base1'
# auth_plugin = 'mysql_native_password' 
)