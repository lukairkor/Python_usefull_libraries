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
@author: lukas
"""
import mysql.connector
import os


# connecting to database
mydb = mysql.connector.connect(
  host="lukas-ThinkPad-T440",
  user="root",
  password="password",
  database="sql-kurs"
)


# count all duplicates in table and show them
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
   

# show all items from tab
def show_tab_data(mycursor):
    mycursor.execute("SELECT * FROM users")
    myresult = mycursor.fetchall() # checking all row   
    # fetch only one row
    # myresult = mycursor.fetchone()

    for x in myresult:
        print(x)
 
    
# print names of columns in table       
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
    

# finding and deliting duplicates
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
def delet_record_or_whole_tab(mycursor):    
    sql = "DELETE FROM users WHERE age = %s"
    adr = ("66", )
    
    mycursor.execute(sql, adr)   
    mydb.commit()
    
    print(mycursor.rowcount, "record(s) deleted") 


# deleting whole table
def del_table(mycursor):
    sql = "DROP TABLE customers"
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
        print("""            
            1.  (print names of columns in table).
            2.  (show all items from tab).
            3.  (count all duplicates in table and show them).
            4.  (finding and deliting duplicates).
            5.  (sorting function).
            6.  (deleting data).
            7.  (deleting tab).
            8.  (updating record in tab).
            9.  (limit tab elements for show).
            10. (limit range of displayed tabs data).
            11. (Close programm).
        """)
        value = int(input("Input value:\n"))
        return value


# clear and continue 
def any_key_clear():    
    input("press any key to continue.")
    os.system('clear')   

    
# main function
def main():
    mycursor = mydb.cursor()
    
    value = -1
    while value != 0:
        value = menu()
        if value == 1:
            tabl_colum_names(mycursor)
            any_key_clear()
            continue
        elif value == 2:
            show_tab_data(mycursor)
            any_key_clear()
            continue
        elif value == 3:
            display_duplica_rows(mycursor) 
            any_key_clear()
            continue
        elif value == 4:            
            del_duplicats(mycursor) 
            any_key_clear()
            continue
        elif value == 5:
            sort_funct(mycursor)
            any_key_clear()
            continue
        elif value == 6:
            delet_record_or_whole_tab(mycursor)
            any_key_clear()
            continue
        elif value == 7:
            del_table(mycursor)
            any_key_clear()
            continue
        elif value == 8:
            updating_record(mycursor)
            any_key_clear()
            continue
        elif value == 9:
            show_with_limits(mycursor)
            any_key_clear()
            continue
        elif value == 10:
            show_with_range(mycursor)
            any_key_clear()
            continue
        elif value == 11:
            break
        else:
            print("Incorrect chooise, try again!")
    
    
    
if __name__ == "__main__":
    main()



