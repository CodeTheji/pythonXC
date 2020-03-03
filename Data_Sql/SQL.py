import pymysql.cursors

connection = pymysql.connect(host= "localhost",
                            user="root",
                            password="",
                            db="my_db",
                            charset="utf8mb4",
                            cursorclass=pymysql.cursors.DictCursor)



# ##############################      INSERT SINGLE USER ###################

# with connection.cursor() as cs:

#             #create a new record
#         sql_cmd = 'INSERT into person (frame, lname, age, address, email, salary) values ("clint", "ramore", 26, "wuse,abuja", "clint_ram42@gmail.com", 150000)'

#         cs.execute(sql_cmd)
#         connection.commit()

# print("Successfully added")


# with connection.cursor() as cs:
#     #Create a new record

#     filename = "C:/Users/MY PC/Desktop/Prog_python/lists_of_random_names.txt"
#     raw_data = open(filename, "r").read()

#     for name in raw_data.splitlines():
#         #print(name) #PRINT LINE WHICH CONTAINGS INDIVIDUAL FULL NAME

#         frame, lname = name.split()

       
#         domain = random.choice(["@gmail.com", "@yahoo.com", "@live.com"])
#         user_mail = frame[:3] + lname[:3] + domain
#         user_age = random.randint(10,50)
#         salary = random.randint(10000, 50000)

#         print(f"Firstname - {frame}, Lastname - {lname}, Age - {user_age}, Email - {user_mail}, Salary - {salary}")

#         sql_cmd = f'INSERT into person(frame, lname, age, address, email, salary) values ("{frame}", "{lname}", {user_age}, "abuja", "{user_mail}", "{salary}")' #Note the f'INSERT, the approstophy is a single quote


#         cs.execute(sql_cmd)
#         connection.commit()


# ''' Segun code '''
# with connection.cursor() as cursor:

#     import random

#     data = open("random_names.txt", 'r')
#     names = data.read()
#     splitted_names = names.splitlines()
#     emails = ["@gmail.com", "@yahoo.com", "@live.com"]

#     print("\nUsers : \n")



#     for name in splitted_names:
#         fname, lname = name.split()
#         random_email = random.choice(emails)
#         email = f"{fname[:3]}{lname[:3]}{random_email}"
#         age = random.randint(10, 50)
#         salary = random.randint(10000, 50000)
#         # print(name)
#         # print(f"\tfirstname : {fname}")
#         # print(f"\tlastname : {lname}")
#         # print(f"\temail : {email}")
#         # print(f"\tage : {age}")
#         # print(f"\tsalary : {salary}\n")

#         sql_cmd = f'INSERT INTO person (fname, lname, age, address, email, salary) VALUES ("{fname}", "{lname}", "{age}","mushin lagos", "{email}", "{salary}")'

#         cursor.execute(sql_cmd)
#         connection.commit()


#################### KEY GUIDES #############################


# CREATE DATABASE my_db # Creating a database(my_db = database name)
# select/SELECT COUNT(*) from person where age > 30  # Counting the amount of ages greater than 30
# CREATE TABLE person (person_id INT(8) NOT NULL AUTO_INCREMENT PRIMARY KEY, stu_name VARCHAR(100), fname VARCHAR(100), lname VARCHAR(100), age INT(3) NOT NULL, address VARCHAR(100), email VARCHAR(50)) # Creating a table
# INSERT INTO student (stu_name, age, address, email) VALUES('Shegs', '21', 'Ilupeju-Onipanu', 'daevheed13@gmail.com') # inserting the corresponding values into the columns
#### WILD CARDS (VIEWING ROWS WITH SPECIFIC LETTERS) ####
# select * from student # to view the whole table
# select * from student where fname = "Kristine" # Viewing only rows that have firstname as Kristine
# select * from student where fname != "Kristine" # Viewing only rows that do not have firstname as Kristine
# select * from person where fname like "A%" # displaying all names that start with A (They are wild cards)
# select COUNT(*) from person where fname like "A%" # counting all names that start with A
# select * from person where fname like "%A" # displaying all names that end with A
# select * from person where fname like "%A%" # displaying all names that contains with A


#### MINIMUM AND MAXIMUM ########
# select max(age) from person # viewing the maximum age on the table
# select * from person where age = (select max(age) from person) # viewing row / person with the maximum age on the table
# select * from person where age = (select min(age) from person) # viewing row / person with the minimum age on the table
# select * from person where salary = (select max(salary) from person) # viewing row / person with the maximum salary on the table
# select * from person where age BETWEEN 19 AND 35 # Those with ages 35 <= x >= 19 
# select * from person where age > 19 AND age < 35 # Those with ages 35 <= x >= 19 
# SELECT * FROM person ORDER BY length(fname) DESC # viewing the names by their length in descending order
# SELECT * FROM person ORDER BY length(fname) ASC # viewing the names by their length in ascending order
# SELECT length(fname) FROM person # displaying the length of all the firstnames
# SELECT max(length(fname)) FROM person # displaying the maximum length of firstname
# SELECT * FROM person WHERE length(fname) = (SELECT max(length(fname)) FROM person) # displaying the person(s) maximum length of firstname
# SELECT * FROM person WHERE length(lname) = (SELECT max(length(lname)) FROM person) # displaying the person(s) maximum length of lastname
# SELECT * FROM person WHERE length(lname) = (SELECT min(length(lname)) FROM person) # displaying the person(s) minimum length of lastname


###### CREARE PRODUCT TABLE (1ST TABLE) #######

# with connection.cursor() as cs:

#     sql_cmd = f'create table product (id int(3) AUTO_INCREMENT PRIMARY KEY NOT NULL, name varchar(30), price int(5), weight float(5,5))'
#     # create a new record

#     cs.execute(sql_cmd)
#     connection.commit()



# # ##### CREATE ORDERS TABLE  (2nd Table) ######



# with connection.cursor() as cs:

#     # create a new cursor

#     sql_cmd = f'create table orders (person_id int, FOREIGN KEY (person_id) REFERENCES person(person_id), product_id int, FOREIGN KEY (product_id) REFERENCE product(id), order_date Date, qty int)'
#     cs.execute(sql_cmd)
#     connection.commit()

# products = ["apple", "orange", "shoes", "knife", "cream"]
# prices = [10, 4, 50, 10, 20]
# weights = [5,6,7,8,8]


# for  details in product.split():
#     product = details.split()

#     all_products = details.split()[0:5]

# print(all_products)
# '''CORRECTION'''

# #######     ADD TO ORDERS TABLE    ####
# with connection.cursor() as cs:

#     #create a new record


    
#     for item in zip(product, prices, weights):
#         pname = item[0]
#         pprice = item[1]
#         pweight = item[2]

#         sql_cmd = f'INSERT INTO product (name, price, weight) value ("{pname}", "{pprice}", "{pweight}")'

#         cs.execute(sql_cmd)
#         connection.commit







### ASSIGNMENT GAP##########

from datetime import datetime, timedelta
import random


min_year =2019
max_year = datetime.now().year

start = datetime(min_year, 1, 1, 00,00,00)
years = max_year - min_year + 1
end = start + timedelta(days = 365 * years)

my_date = []

the_quantity = [] # after the print(my_date below)

persons_id = []

#Date Generator
for i in range(20):
    random_date = (start + (end - start) * random.random()).strftime("%d/%m/%y")
    my_date.append(random_date)

# print(my_date)

# Generating quantity

for q in range(20):
    quantity = random.randint(2, 100)
    the_quantity.append(quantity)

# Generating Persons id
for p in range(20):
    persons_list = random.randint(42,61)
    persons_id.append(persons_list)

zipped = zip(persons_id, my_date, the_quantity)

product_idd = [1,2,3,4,5]

with connection.cursor() as cs:

    for real in zipped:

        person_id = real[0]
        order_date = real[1]
        qty = real[2]
        product_id = random.choice(product_idd)


        # print(f'Person ID: {person_id}\nProduct ID: {product_id}\nOrder Date: {order_date}\nQuantity: {qty}')
        # print("")
        # print("### NEW DETAILS ####")
        sql_cmd = f'INSERT into orders (person_id, product_id, order_date, qty) values ("{person_id}", "{product_id}", "{order_date}", "{qty}")'

        print(sql_cmd)

        cs.execute(sql_cmd)
        connection.commit()



########TO FETCH FROM ORDERS TABLE ######

with connection.cursor() as cs:

    sql_cmd = f'SELECT frame FROM person'

    cursor.execute(sql_cmd)
    result = cursor.fetchall()
    print(result)