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

def create_table(mycursor):
    sql = """
    DROP TABLE IF EXISTS users;

    CREATE TABLE users (
        id INT PRIMARY KEY AUTO_INCREMENT,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL, 
        age INT NOT NULL
    );"""
    mycursor.execute(sql)
    

def insert_data(mycursor):
    sql = """
    INSERT INTO users (first_name,last_name,age) 
    VALUES ('Carine ','Schmitt',18),
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
       

def inse_singl_recor(mycursor):
    # inserting single record
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = ("John", "Highway 21")
    mycursor.execute(sql, val)
           
    
def execute_(mycursor):          
    mydb.commit()    
    print(mycursor.rowcount, "record inserted.")


# main function
def main():
    mycursor = mydb.cursor()
    
    ## add new table
    # create_table(mycursor)
    ## add data to table
    insert_data(mycursor)
    # inse_singl_recor(mycursor)
        
    execute_(mycursor)
    

if __name__ == "__main__":
    main()
    
    
    
    
    