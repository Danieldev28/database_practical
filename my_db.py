import os
import pymysql
username = os.getenv('C9_USER')

# this user name is static because we are using cloud 9 environment.
# When deploying our own database server we will have to provide our own 
# user name and passoword that
# keeps all databases safe.

connection = pymysql.connect(host ='localhost',              
                            user = username,   
                            password ='',
                            db ='Chinook'
                        )

 
     addtional commands! SELECT
try:
    with connection.cursor() as cursor:
        sql = """SELECT User.User_id, User.Username, City.City_name FROM City INNER JOIN
        User ON USER.City_id = City.City_id;"""
        cursor.execute(sql)
        for item in cursor:
            print(item)
        
finally:
#     connection.close()   
    
  #  Delete all! from table command
      
# try:
#     with connection.cursor() as cursor:
#         sql = """DELETE FROM Full_Stack;"""
#         cursor.execute(sql)
#         connection.commit() 
        
# finally:
#     connection.close()              

               

#     #  Delete command
# try:
#     with connection.cursor() as cursor:
#         sql = """DELETE FROM Full_Stack WHERE
#         syllabus = 'Something'"""
#         cursor.execute(sql)
#         connection.commit() 
        
# finally:
#     connection.close()              




# update command!
# try:
#     with connection.cursor() as cursor:
#         sql = """UPDATE Full_Stack SET syllabus = 'Something'
#         WHERE name = 'Python'"""
#         cursor.execute(sql)
#         connection.commit() 
        
# finally:
#     connection.close()                         



# insert command!
# try:
#     with connection.cursor() as cursor:
#         sql = """INSERT INTO Full_Stack
#         (name, syllabus) VALUEs ('Python', 'Django');"""
#         cursor.execute(sql)
#         connection.commit() 
#         # commit command need cause you are changing some data in pipline python3 my_db.py
# finally:
#     connection.close()                        



# create a table in chinook database

# try:
#     with connection.cursor() as cursor:
#         sql = """CREATE TABLE Full_Stack (
#             id int primary key auto_increment,
#             name varchar(20),
#             syllabus varchar(30)
#             )"""
#         cursor.execute(sql)
# finally:
#     connection.close()

# output in a dictionary

# def mydata(table_name):
#     try:
#         with connection.cursor(pymysql.cursors.DictCursor) as cursor:
#             sql = "SELECT * FROM {};".format(table_name)
#             cursor.execute(sql)
#             for item in cursor:
#                 print(item)
#     finally:
#         connection.close()
        
        

# regular method query object
# try:
#     with connection.cursor() as cursor:
#         sql = "SELECT * FROM Artist;"
#         cursor.execute(sql)
#         result = cursor.fetchall()
#         print(result)
# finally:
#     connection.close()

# DESC User;**
    
    # Notes:example join inner!
#                                                               (onbehalf)
# """SELECT User.Username, City.City_name FROM City INNER JOIN User ON User.City_id = City.City_id;"""
#          table           table                table          table   table          table
        #  (they both have a city id as a foreign key at the end.)
        
        
        # # table City----
        # City_id, City_name
        #     1 toronto
        #     2 montreal
        # # # table User----  
       
        # # user_id, Username, City_id
        # 1  daniel  1
        # 2  hani     2
        # 3  mais     1
        # 4  abhay    2
    
    # OUTPUT!!!!
    # table username,city_name -----
    # hani    toronto
    # mais    montreal
    # daniel  toronto
    # abhay   montreal
            
        
        # ALTER TABLE City ADD COLUMN Population int;
        # UPDATE City Set Population = 10000 WHERE City_id = 1;
        #  UPDATE City Set Population = 10000 WHERE City_id = 2;
        
        
       
    #     SELECT User.User_id,City.City_name FROM User INNER JOIN City ON User.User_id = City.City_id;     
    #   *RETRIEVE PRIMARY KEYS USER_ID AND CITY NAME FROM SECOND TABLEDISPLAY THEM IN A TABLE TOGETHER (JOIN) 
       
    #   SELECT User.Username,City.City_name FROM User INNER JOIN City ON User.User_id = City.City_id;
    #   *RETRIEVE PRIMARY KEYS uSERNAME AND CITY NAME FROM SESOND TABLE DISPLAY THEM IN A TABLE TOGETHER(JOIN)
       
    #   PROPER SYNTAX
    #     SELECT User.Username, City.Population, City.Language FROM User INNER JOIN City ON User.City_id = City.City_id; 
    #     your ids could be different numbers 
    
    # another exmaple 
    #  SELECT User.Username, City.Language FROM User INNER JOIN City ON User.City_id = City.City_id; 