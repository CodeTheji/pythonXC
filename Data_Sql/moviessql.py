import pymysql.cursors, random
import datetime

import csv
# import sys

# maxint = (sys.maxsize)
# decrement = True

# while decrement:

#     decrement = False

#     try:
#         csv.field_size_limit(maxint)
#     except OverflowError:
#         maxint = int(maxint/10)
#         decrement = True


# Connect to the database
# connection = pymysql.connect(host='checklight.mysql.pythonanywhere-services.com',
                            #  user='checklight',
                            #  password='lightapppass',
                            #  db='checklight$light_app_db',
                            #  charset='utf8mb4',
                            #  cursorclass=pymysql.cursors.DictCursor)

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='my_db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


##############################  INSERT SINGLE USER  ###############################

# with connection.cursor() as cursor:
#         # Create a new record
        
#         sql_cmd = 'INSERT into student (stu_name, age, address, email) values ("clint ramore", 26, "wuse, abuja", "clint_ram@gmail.com")'

#         cursor.execute(sql_cmd)
#         connection.commit()



##############################  INSERT MULTIPLE FROM FILE ###############################
# with connection.cursor() as cursor:
#     # Create a new record
    
#     filename  = "C:/Users/INYANG/Desktop/PERSONAL WORK/PYTHON_CLASS/database/names.csv"
#     raw_data = open(filename, "r").read()

#     for name in raw_data.splitlines():
#         # print(name) # PRINT LINE WHICH CONTAINGS INDIVIDUAL FULL NAME

#         f_name, l_name = name.split()

#         base_email = "@gmail.com"
#         user_mail = f_name[:4] + l_name[:4]+base_email
#         user_age = random.randint(10, 50)

#         if not f_name.lower().startswith("."):
#             print(f"Firstname - {f_name}, Lastname - {l_name}, Age - {user_age}, Email - {user_mail}")
            
#             sql_cmd = f'INSERT into student (stu_name, age, address, email) values ("{name}", {user_age}, "abuja", "{user_mail}")'

#             cursor.execute(sql_cmd)
#             connection.commit()

###########CREATE PRODUCT TABLE#######
# with connection.cursor() as cursor:
#     # Create a new record

#     sql_cmd = f'create table product (id int(3) AUTO_INCREMENT PRIMARY KEY NOT NULL, name varchar(30), price int(5), weight float(5,5))'

#     cursor.execute(sql_cmd)
#     connection.commit()

##########CREATE ORDERS TABLE#######
# with connection.cursor() as cursor:
#     # Create a new record

#     # sql_cmd = f'create table orders (person_id int, FOREIGN KEY (person_id) REFERENCES person(person_id), product_id int, FOREIGN KEY (product_id) REFERENCES product(id), order_date Date, qty int(5))'
#     # sql_cmd = f'create table orders (person_id int, FOREIGN KEY (person_id) REFERENCES person(person_id), product_id int, FOREIGN KEY (product_id) REFERENCES product(id), primary key (person_id, product_id), order_date Date, qty int(5))'

#     cursor.execute(sql_cmd)
#     connection.commit()

# products = ["apple", "orange", "shoes", "knife", "cream"]
# prices = [10, 4, 50, 10, 20]
# weights = [5, 6, 7, 8, 8]

# # ###########ADD TO ORDERS TABLE#######
# with connection.cursor() as cursor:
#     # Create a new record

#     for item in zip(products, prices, weights):
#         pname = item[0]
#         pprice = item[1]
#         pweight = item[2]

#         sql_cmd = f'INSERT INTO product (name, price, weight) values ("{pname}", "{pprice}", {float(pweight)})'

#         cursor.execute(sql_cmd)
#         connection.commit()



###########FETCH FROM ORDERS TABLE#######
# with connection.cursor() as cursor:
#     # Create a new record


#         sql_cmd = f'SELECT fname FROM person'

#         cursor.execute(sql_cmd)
#         result = cursor.fetchall()
#         print(result)





def insert_sql(fname, lname, age, email):

    with connection.cursor() as cursor:
        # Create a new record
        
        sql_cmd = 'INSERT into person (fname, lname, age, email) values ("fname", "lname", age, "email")'

        cursor.execute(sql_cmd)
        connection.commit()


def insert_csv(fname, lname, age, email):
    filename  = "C:/Users/INYANG/Desktop/PERSONAL WORK/PYTHON_CLASS/database/rand_names.csv"
    file = open(filename, "a")
    
    file.writelines(f"{f_name}, {l_name}, {user_age}, {user_mail}\n")
    file.close()









##############################  INSERT MULTIPLE RANDOM VALUES ###############################
with connection.cursor() as cursor:
    # Create a new record

    then = datetime.datetime.now()
    for i in range(10000):

        f_name, l_name = random.choice(list("abcd")), random.choice(list("abcd"))

        base_email = "@gmail.com"
        user_mail = f_name + l_name +base_email
        user_age = random.randint(10, 50)
        
        insert_sql(f_name, l_name, user_age, user_mail)

    now = datetime.datetime.now()
    duration = now - then

    then = datetime.datetime.now()
    print(f"SQL DURATION : {duration.seconds}")

    for i in range(10000):
        f_name, l_name = random.choice(list("abcd")), random.choice(list("abcd"))

        base_email = "@gmail.com"
        user_mail = f_name + l_name +base_email
        user_age = random.randint(10, 50)
        
        insert_csv(f_name, l_name, user_age, user_mail)

    now = datetime.datetime.now()

    duration = now - then
    print(f"CSV DURATION : {duration.seconds}")














# SELECT * from (SELECT person.fname, person.lname, person.age, person.salary, orders.product_id from person inner JOIN orders on person.person_id = orders.person_id) as Mine
# INNER JOIN product
# ON Mine.product_id = product.id


# #############################  CREATE DATABASE  ###############################
# try:
#     with connection.cursor() as cursor:
#         # Create a new record

#         sql = """CREATE TABLE films 
#                 (id int NOT NULL KEY AUTO_INCREMENT,
#                 adult VARCHAR(500), 
#                 genres VARCHAR(500), 
#                 title VARCHAR(500), 
#                 vote_avg DOUBLE(5,0), 
#                 popularity DOUBLE(5,0), 
#                 production_co VARCHAR(500), 
#                 production_stu VARCHAR(500), 
#                 language VARCHAR(500), 
#                 release_date DATE, 
#                 runtime INT, 
#                 revenue INT, 
#                 budget int)"""

#         cursor.execute(sql)
#         connection.commit()
# except:
#     # connection is not autocommit by default. So you must commit to save
#     # your changes.

#     print('Table Exists')


# with open('films2.csv',errors = 'ignore') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0

#     with connection.cursor() as cursor:
#         # Create a new record




#         for row in csv_reader:
#             # print(row)
#             sql = """insert into films (adult,  budget, popularity, release_date, revenue, runtime, title, vote_avg) 
#                 values ("{}", "{}","{}", "{}","{}", "{}","{}","{}")""".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6], row[7])
#             cursor.execute(sql)
#             # print('got here')
#             # print(cursor.fetchall())
#             # connection is not autocommit by default. So you must commit to save
#             # your changes.
#             # connection.commit()
#             # if line_count == 0:
#             #     print(f'Column names are {", ".join(row)}')
#             #     line_count += 1
#             # else:
#             #     print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#             #     line_count += 1
        

#     # print(f'Processed {line_count} lines.')








# # Connect to the database
# connection = pymysql.connect(host='localhost',
#                              user='root',
#                              password='',
#                              db='db',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)


# # CREATE DATABASE
# try:
#     with connection.cursor() as cursor:
#         # Create a new record

#         sql = """CREATE TABLE films 
#                 (id int NOT NULL KEY AUTO_INCREMENT,
#                 adult VARCHAR(100), 
#                 genres VARCHAR(100), 
#                 title VARCHAR(100), 
#                 vote_avg DOUBLE(5,0), 
#                 popularity DOUBLE(5,0), 
#                 production_co VARCHAR(100), 
#                 production_stu VARCHAR(100), 
#                 language VARCHAR(100), 
#                 release_date DATE, 
#                 runtime INT, 
#                 revenue INT, 
#                 budget int)"""

#         cursor.execute(sql)
#         connection.commit()
# except:
    # connection is not autocommit by default. So you must commit to save
    # your changes.

#     print('Table Exists')



#CREATE DATABASE
# try:
#     with connection.cursor() as cursor:
#         # Create a new record

        # sql = """CREATE TABLE users 
        #         (id int NOT NULL KEY AUTO_INCREMENT,
        #         email VARCHAR(20), 
        #         username VARCHAR(20))"""

#         cursor.execute(sql)
#         connection.commit()
# except:
#     # connection is not autocommit by default. So you must commit to save
#     # your changes.

#     print('Table Exists')



# with connection.cursor() as cursor:
#     # Create a new record
#     sql = """insert into users (username, email) 
#                 values ("{}", "{}")""".format('inyang@gmail.com','attah')
#     cursor.execute(sql)
#     print('got here')
#     # print(cursor.fetchall())
#     # connection is not autocommit by default. So you must commit to save
#     # your changes.
# connection.commit()

# with connection.cursor() as cursor:
#     # Read a single record
#     sql = '''SELECT username FROM users WHERE username="{}"'''.format('ola')
#     cursor.execute(sql)
#     result = cursor.fetchmany(2)
#     print(result)
# connection.close()