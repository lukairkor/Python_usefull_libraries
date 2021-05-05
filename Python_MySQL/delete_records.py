#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 00:22:42 2021

@author: lukas
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="lukas-ThinkPad-T440",
  user="root",
  password="password",
  database="sql-kurs"
)

def del_certei_adress():
    sql = "DELETE FROM users WHERE address = 'Mountain 21'"
    return sql


def display_duplica_rows(mycursor):
    sql = """
    SELECT COUNT(*), first_name, last_name, age 
    FROM users
    GROUP BY first_name, last_name, age
    HAVING COUNT(*)>1;
    """
    mycursor.execute(sql)    

    print('Duplicate Rows:')               
    for row in mycursor.fetchall(): print(row)
   

def show_tab_data(mycursor):
    mycursor.execute("SELECT * FROM users")
    myresult = mycursor.fetchall() # checking all row   
    # fetch only one row
    # myresult = mycursor.fetchone()

    for x in myresult:
        print(x)
 
        
def tabl_colum_names(mycursor):
    # first option scheme
    sql = """SELECT COLUMN_NAME
      FROM INFORMATION_SCHEMA.COLUMNS
      WHERE TABLE_SCHEMA = 'sql-kurs' AND TABLE_NAME = 'users';
    """
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    
    for x in myresult:
        print(x)
        
    mydb.commit()
    mycursor.close()
    mydb.close()
    

def del_duplicats(mycursor):    
    sql = """
    DROP TABLE users_temp;
    
    CREATE TABLE users_temp 
    LIKE users;
    
    INSERT INTO users_temp
    SELECT * 
    FROM users 
    GROUP BY username;

    DROP TABLE users;
    
    ALTER TABLE users_temp 
    RENAME TO users;
    """
    mycursor.execute(sql)    
    mydb.commit()
    mycursor.close()
    mydb.close()
    
# main function
def main():
    mycursor = mydb.cursor()
        
    # show_tab_data(mycursor)
    display_duplica_rows(mycursor)
    # del_duplicats(mycursor)
    
    # tabl_colum_names(mycursor)
    

if __name__ == "__main__":
    main()



