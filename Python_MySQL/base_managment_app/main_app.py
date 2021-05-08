#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 00:04:36 2021
-adding function (connecting to database)
-adding function (count all duplicates in table and show them)
-adding function (show all items from tab)
-adding function (print names of columns in table)
-adding function (finding and deliting duplicates)
-adding function (sorting function)
-adding function (deleting data)
-adding function (deleting tab)
-adding function (updating record in tab)
-adding function (limit tab elements for show)
-adding function (limit range of displayed tabs data)
-add menu and better tab show
-add possiblity to creat new tab and import it as classe object
@author: lukas
"""
import mysql.connector
import os
from tabulate import tabulate
import functools
from creat_new_tab import Create_Table 
  

# connecting to database
mydb = mysql.connector.connect(
  host="lukas-ThinkPad-T440",
  user="root",
  password="password",
  database="sql-kurs"
)


# print names of columns in table       
def show_tabl_colum_names(mycursor):
    # first option scheme
    sql = """SELECT COLUMN_NAME
      FROM INFORMATION_SCHEMA.Columns
      WHERE TABLE_SCHEMA = 'sql-kurs' AND TABLE_NAME = 'users';"""
    
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    # create one tuple with list of tuples (all with strings)
    myresult = functools.reduce(lambda sub, ele: sub  + ele, myresult)     

    mydb.commit()
    return myresult
    

# show all items from tab
def show_tabl_colum_data(mycursor):
    mycursor.execute("SELECT * FROM users")
    myresult = mycursor.fetchall() # checking all row   
    # fetch only one row

    tab = show_tabl_colum_names(mycursor)
    a, b, c, d = tab
    print(tabulate(myresult, headers=[c, b, d, a]))

        
# count all duplicates in table and show them
def check_if_are_row_duplicates(mycursor):
    sql = """
    SELECT COUNT(*), first_name, last_name, age 
    FROM users
    GROUP BY first_name, last_name, age
    HAVING COUNT(*)>1;
    """
    mycursor.execute(sql)    
    
    row = None
    for row in mycursor.fetchall(): row
    print('Duplicate Rows: ', row)               
    
   
    
# finding and deliting duplicates
def del_row_duplicats(mycursor):    
    sql = """
    DROP TABLE IF EXISTS users_temp;
    
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
    
    
# sorting ascending or descending    
def sort_funct(mycursor):   
    sql = "SELECT * FROM users ORDER BY id"
    # sql = "SELECT * FROM users ORDER BY first_name"
    # sql = "SELECT * FROM users ORDER BY last_name"
    # sql = "SELECT * FROM users ORDER BY age"
    
    # sql = "SELECT * FROM users ORDER BY id DESC"
    # sql = "SELECT * FROM users ORDER BY first_name DESC"
    # sql = "SELECT * FROM users ORDER BY last_name DESC"
    # sql = "SELECT * FROM users ORDER BY age DESC"
    
    mycursor.execute(sql)    
    myresult = mycursor.fetchall()
    
    for x in myresult:
      print(x)


# deleting data support anty injection
def delet_record(mycursor):    
    sql = "DELETE FROM users WHERE age = %s"
    adr = ("66", )
    
    mycursor.execute(sql, adr)   
    mydb.commit()
    
    print(mycursor.rowcount, "record(s) deleted") 


# deleting whole table
def del_table(mycursor):
    sql = "DROP TABLE users"
    mycursor.execute(sql)


# updating record in tab
def updating_record(mycursor):   
    sql = "UPDATE users SET age = %s WHERE id = %s"
    val = ("22", "15")
    
    mycursor.execute(sql, val) 
    # required to make changes
    mydb.commit()
    
    print(mycursor.rowcount, "record(s) affected")    
 
    
# limit tab elements for show
def show_with_limits(mycursor):
    mycursor.execute("SELECT * FROM users LIMIT 5") 
    myresult = mycursor.fetchall()
    
    for x in myresult:
      print(x)     


# limit range of displayed tabs data
def show_with_range(mycursor):
    mycursor.execute("SELECT * FROM users LIMIT 3 OFFSET 2")
    myresult = mycursor.fetchall()
    
    for x in myresult:
      print(x)  
     
      
# print menu      
def menu():    
    print(           
"""
1.  Create new tab.
2.  Add data to new tab.
3.  Show all items from tab.
4.  Count all duplicates in table and show them.
5.  Finding and deliting duplicates.
6.  Sorting function.
7.  Delete record.
8.  Deleting tab.
9.  Updating record in tab.
10. Limit tab elements for show.
11. Limit range of displayed tabs data.
12. Close programm.
""")
    value = int(input("Input value:\n"))
    return value


# clear and continue 
def any_key_clear():    
    input("press any key to continue.")
    os.system('clear')   

# # main function test
# def main():    
#     mycursor = mydb.cursor()    
#     new_tab = Create_Table()


#main function
def main():    
    value = -1
    while value != 0:
        mycursor = mydb.cursor()
        new_tab = Create_Table()
        value = menu()
        if value == 1:
            new_tab.create_table(mycursor)
            any_key_clear()
            continue
        elif value == 2:
            new_tab.insert_data(mycursor, mydb)
            any_key_clear()
            continue
        elif value == 3:
            show_tabl_colum_data(mycursor)
            any_key_clear()
            continue
        elif value == 4:
            check_if_are_row_duplicates(mycursor) 
            any_key_clear()
            continue
        elif value == 5:            
            del_row_duplicats(mycursor) 
            any_key_clear()
            continue
        elif value == 6:
            sort_funct(mycursor)
            any_key_clear()
            continue
        elif value == 7:
            delet_record(mycursor)
            any_key_clear()
            continue
        elif value == 8:
            del_table(mycursor)
            any_key_clear()
            continue
        elif value == 9:
            updating_record(mycursor)
            any_key_clear()
            continue
        elif value == 10:
            show_with_limits(mycursor)
            any_key_clear()
            continue
        elif value == 11:
            show_with_range(mycursor)
            any_key_clear()
            mycursor.close()
            mydb.close()
            continue
        elif value == 12:
            break
        else:
            print("Incorrect chooise, try again!")
       
if __name__ == "__main__":
    main()



