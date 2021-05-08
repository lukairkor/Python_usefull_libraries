#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 01:58:03 2021

@author: lukas
"""
from tabulate import tabulate


class Create_Table:
    def list_all_database(self, mycursor):
        mycursor.execute("SHOW DATABASES")
        print(tabulate(mycursor))
  
    # create new empty table
    def create_table(self, mycursor):
        sql = """
        DROP TABLE IF EXISTS users;
    
        CREATE TABLE users (
            id INT PRIMARY KEY AUTO_INCREMENT,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL, 
            age INT NOT NULL
        );"""
        mycursor.execute(sql)
      
        
    # insert to empty table some data
    def insert_data(self, mycursor, mydb):
        sql = """
        INSERT INTO users (first_name,last_name,age) 
        VALUES ('Carine ','Schmitt',18),
           ('Jean','King',24),
           ('Jean','King',24),
           ('Peter','Ferguson',65),
           ('Janine ','Labrune',34),
           ('Jonas ','Bergulfsen',73),
           ('Janine ','Labrune',52),
           ('Susan','Nelson',33),
           ('Zbyszek ','Piestrzeniewicz',34),
           ('Roland','Keitel',53),
           ('Julie','Murphy',66),
           ('Kwai','Lee',24),
           ('Jean','King',63),
           ('Susan','Nelson',45),
           ('Roland','Keitel',33); """
        mycursor.execute(sql)
        mydb.commit()  
      
           
    # insert to table specific data
    def inse_singl_recor(self, mycursor):
        # inserting single record
        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        val = ("John", "Highway 21")
        mycursor.execute(sql, val)
           
    


        



    
    
    
    
    