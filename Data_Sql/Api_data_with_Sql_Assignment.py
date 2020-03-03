import pymysql.cursors
import requests

connection = pymysql.connect(host = "localhost",
                            user = "root",
                            password = "",
                            db = "checklight",
                            charset = "utf8mb4",
                            cursorclass = pymysql.cursors.DictCursor)


# ''' CREATING TABLES'''

# with connection.cursor() as cs:
#     sql_cmd = f'create table devices (id int(3) AUTO_INCREMENT PRIMARY KEY NOT NULL, name varchar(30))'

#     cs.execute(sql_cmd)
#     connection.commit()

# ''' CREATE DATA TABLE '''

# with connection.cursor() as cs:
#     sql_cmd = f'create table data (device_id int AUTO_INCREMENT NOT NULL, FOREIGN KEY (device_id) REFERENCES devices(id), id int(11), status int, time varchar(30))'

#     cs.execute(sql_cmd)
#     connection.commit()

with connection.cursor() as cs:

    devices = ["1x0d001", "1x0d002", "1x0d003", "1x0d004","1x0d005"]

    for device in devices:

        url - f'http://checklight.pythonanywhere.com/get_readings/{device}/2/'

        response = requests.get(url)
        data = response.json()
        streets = data["streets"]
    