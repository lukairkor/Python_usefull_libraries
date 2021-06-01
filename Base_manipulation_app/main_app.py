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
-adding function (deleting data)s
-adding function (deleting tab)
-adding function (updating record in tab)
-adding function (limit tab elements for show)
-adding function (limit range of displayed tabs data)
-add menu and better tab show
-add possiblity to creat new tab and import it as class object
@author: lukas
"""
import mysql.connector
import os
from tabulate import tabulate
import functools
import enquiries
from creat_new_tab import Create_Table 
  

# print names of columns in table       
def show_tabl_colum_names(mycursor):
    try:
        # first option scheme
        sql = """SELECT COLUMN_NAME
          FROM INFORMATION_SCHEMA.Columns
          WHERE TABLE_SCHEMA = 'base1' AND TABLE_NAME = 'users';"""
        
        mycursor.execute(sql, multi=True)
        myresult = mycursor.fetchall()
        # create one tuple with list of tuples (all with strings)
        myresult = functools.reduce(lambda sub, ele: sub  + ele, myresult)     
    
        # mydb.commit()
        return myresult
    except:
        print("Failed to print data")    


# show all items from tab
def show_tabl_colum_data(*args):
    # try:
    len_args = len(args)
    if len_args > 1:
        args[0].execute(args[1], multi=True)      
    else: 
        args[0].execute("SELECT * FROM users", multi=True)
        
    myresult = args[0].fetchall() # checking all row   
    # fetch only one row

    tab = show_tabl_colum_names(args[0])
    a, b, c, d = tab
    print(tabulate(myresult, headers=[a, b, c, d]))
    # except:
    #     print("Failed to print data")  
        
        
# count all duplicates in table and show them
def check_if_are_row_duplicates(mycursor):
    try:
        sql = """
        SELECT COUNT(*), first_name, last_name, age 
        FROM users
        GROUP BY first_name, last_name, age
        HAVING COUNT(*) > 1;
        """
        mycursor.execute(sql)       
        
        data = mycursor.fetchall()
        print('Duplicate Rows: ')               
        for row in data: 
            print(row)
        mycursor.close()
    except:
        print("Failed to print data")
    # mycursor.close()
   
    
# finding and deliting duplicates
def del_row_duplicats(mycursor): 
    mydb = my_data_base()
    sql = """    
    delete t1 FROM users t1
    INNER JOIN users t2
    WHERE
    t1.id < t2.id AND
    t1.first_name = t2.first_name AND
    t1.last_name = t2.last_name AND
    t1.age = t2.age;
    """
    mycursor.execute(sql, multi=True)    
    mydb.commit()
    
    
# sorting ascending or descending    
def sort_funct(mycursor):
    show_tabl_colum_data(mycursor)
    options = ["Order by id [ascending]", "Order by first name [ascending]",
               "Order by last name [ascending]", "Order by age[ascending]",
               "Order by id [descending]", "Order by first name [descending]",
               "Order by last name [descending]", "Order by age[descending]"]    
     
    choice = enquiries.choose('Choose one of these options: ', options)
    # ascending
    if choice == options[0]:
        sql = "SELECT * FROM users ORDER BY id"
        show_tabl_colum_data(mycursor, sql)
        any_key_clear()
    elif choice == options[1]:
        sql = "SELECT * FROM users ORDER BY first_name"
        show_tabl_colum_data(mycursor, sql)
        any_key_clear()
    elif choice == options[2]:
        sql = "SELECT * FROM users ORDER BY last_name"
        show_tabl_colum_data(mycursor, sql)
        any_key_clear()
    elif choice == options[3]:
        sql = "SELECT * FROM users ORDER BY age"
        show_tabl_colum_data(mycursor, sql)
        any_key_clear()
    # descending
    elif choice == options[4]:
        sql = "SELECT * FROM users ORDER BY id DESC"
        show_tabl_colum_data(mycursor, sql)
        any_key_clear()
    elif choice == options[5]:
        sql = "SELECT * FROM users ORDER BY first_name DESC"
        show_tabl_colum_data(mycursor, sql)
        any_key_clear()
    elif choice == options[6]:
        sql = "SELECT * FROM users ORDER BY last_name DESC"
        show_tabl_colum_data(mycursor, sql)
        any_key_clear()
    elif choice == options[7]:
        sql = "SELECT * FROM users ORDER BY age DESC"
        show_tabl_colum_data(mycursor, sql)
        any_key_clear()
        

# deleting data support anty injection
def delet_record(mycursor):
    mydb = my_data_base()
    show_tabl_colum_data(mycursor)  
    
    y = input("Select row id for delete.")
    sql = "DELETE FROM users WHERE id= %s"
    adr = (f"{y}", )
    
    mycursor.execute(sql, adr, multi=True)   
    mydb.commit()
    
    print(mycursor.rowcount, "record deleted")
    show_tabl_colum_data(mycursor)  


# deleting whole table
def del_table(mycursor):
    sql = "DROP TABLE users"
    mycursor.execute(sql, multi=True)


# updating record in tab
def updating_record(mycursor):
    mydb = my_data_base()
    show_tabl_colum_data(mycursor, mydb) 
    
    x = input("Insert column name:\n")
    y = input("Insert old value to update:\n")
    z = input("Insert new value to update:\n")
    
    sql = f"UPDATE users SET {x} = %s WHERE id = %s"
    val = (f"{y}", f"{z}")
    
    mycursor.execute(sql, val, multi=True) 
    # required to make changes
    mydb.commit()
    
    print(mycursor.rowcount, "record(s) affected")    
    show_tabl_colum_data(mycursor)  
 
    
# limit tab elements for show
def show_with_limits(mycursor):
    mycursor.execute("SELECT * FROM users LIMIT 5", multi=True) 
    myresult = mycursor.fetchall()
    
    for x in myresult:
      print(x)     


# limit range of displayed tabs data
def show_with_range(mycursor):
    mycursor.execute("SELECT * FROM users LIMIT 3 OFFSET 2", multi=True)
    myresult = mycursor.fetchall()
    
    for x in myresult:
      print(x)  
     
      
# print menu      
def menu():
    options = [  
    "List all database.",
    "Create new table.",
    "Add data to new table.",
    "Show all items in table.",
    "Show duplicates.",
    "Delete duplicates.",
    "Sorting function.",
    "Delete record.",
    "Insert record.",
    "Deleting table.",
    "Updating record in table.",
    "Limit table elements for show.",
    "Limit range of displayed tabs data.",
    "Close programm."]

    # value = int(input("Input value:\n"))
    return options


# clear and continue 
def any_key_clear():    
    input("press any key to continue.")
    os.system('clear')   


#
def my_data_base():
    # database param
    conf ={
        'user' :'root',
        'password' :'16741674',
        'port' : 3306,
        'host' : 'localhost',
        'database' :'base1'}
    try:
        # connecting to database
        mydb = mysql.connector.connect(**conf)
        return mydb
    except:
        print("Cant connect to database")
            
        
#main function
def main():  
    mydb = my_data_base()
    # infinity loop
    while True:
        mydb.reconnect()
        mycursor = mydb.cursor(buffered=True)
        new_tab = Create_Table()
        options = menu()
        choice = enquiries.choose('Choose one of these options: ', options)
        
        if choice == options[0]:
            new_tab.list_all_database(mycursor)
            any_key_clear()
            
        elif choice == options[1]:
            new_tab.create_table(mycursor)
            any_key_clear()
            
        elif choice == options[2]:
            new_tab.insert_data(mycursor, mydb)
            any_key_clear()
            
        elif choice == options[3]:
            show_tabl_colum_data(mycursor)
            any_key_clear()
            
        elif choice == options[4]:
            check_if_are_row_duplicates(mycursor) 
            any_key_clear()
            
        elif choice == options[5]:          
            del_row_duplicats(mycursor) 
            any_key_clear()
            
        elif choice == options[6]:
            sort_funct(mycursor)
            any_key_clear()
            
        elif choice == options[7]:
            delet_record(mycursor)
            any_key_clear()
            
        elif choice == options[8]:
            new_tab.inse_singl_recor(mycursor, mydb, show_tabl_colum_data)
            any_key_clear()   
                        
        elif choice == options[9]:
            del_table(mycursor)
            any_key_clear()
            
        elif choice == options[10]:
            updating_record(mycursor)
            any_key_clear()
            
        elif choice == options[11]:
            show_with_limits(mycursor)
            any_key_clear()
            
        elif choice == options[12]:
            show_with_range(mycursor)
            any_key_clear()
            mycursor.close()
            mydb.close()
            
        elif choice == options[13]:
            break
        else:
            print("Incorrect chooise, try again!")
            mydb.close()
            
                
if __name__ == "__main__":
    main()



