#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 01:58:03 2021

@author: lukas
"""
from tabulate import tabulate
import os

class Create_Table:
    def list_all_database(self, mycursor):
        try:
            mycursor.execute("SHOW DATABASES", multi=True)
            print(tabulate(mycursor))
        except:
            print("Failed to list databasesdata!")  
  
    # create new empty table
    def create_table(self, mycursor):
        try:
            sql = """
            DROP TABLE IF EXISTS users;
        
            CREATE TABLE users (
                id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL, 
                age INT NOT NULL
            );"""
            mycursor.execute(sql, multi=True)
        except:
            print("Failed to create table!")  
      
        
    # insert to empty table some data
    def insert_data(self, mycursor, mydb):
        try:
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
            mycursor.execute(sql, multi=True)
            mydb.commit()
        except:
            print("Failed to insert data!")  

      
           
    # insert to table new data data at the end of table
    def inse_singl_recor(self, mycursor, mydb, show_tabl_colum_data):
        try:
            if show_tabl_colum_data(mycursor):                
                self.x = input("Insert first_name:\n")
                self.y = input("Insert last_name:\n")
                
                # check if age is int
                self.age = input("Insert age:\n")
                if  self.age.isnumeric():
                     self.age = int(self.age)
                else:
                    print("You didn't enter a valid integer for age!")
                    
                # inserting single record
                self.sql = "INSERT INTO users (first_name, last_name, age) VALUES (%s, %s, %s)"
                self.val = (self.x, self.y, self.age)
                mycursor.execute(self.sql, self.val, multi=True)
                
                print(mycursor.rowcount, "record added")
                os.system('clear')
                show_tabl_colum_data(mycursor)  
                mydb.commit()
                mydb.close()
        except:
            print("Failed to insert record!")  
    
     


    
    
    
    
    