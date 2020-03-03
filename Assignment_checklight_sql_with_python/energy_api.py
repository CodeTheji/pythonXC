import pymysql.cursors, requests, datetime

#  Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='my_db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


## CREATE device table
device_codes = ["1x0d001", "1x0d002", "1x0d003", "1x0d004", "1x0d005"]

with connection.cursor() as Cursor:
    command = "CREATE TABLE IF NOT EXISTS device (id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, code varchar(60))"
    Cursor.execute(command)
    
    connection.commit()
    
    command = "CREATE TABLE IF NOT EXISTS data (device_id INT NOT NULL, FOREIGN KEY(device_id) REFERENCES device(id), post_time TIMESTAMP, status INT(2))"
    Cursor.execute(command)
    
    connection.commit()


devices = ["1x0d001", "1x0d002", "1x0d003", "1x0d004"]
all_devices = {}


# # ADD DEVICES
# with connection.cursor() as Cursor:

#     for device in devices:
       

#         command = f"INSERT INTO device (code) values('{device}')"

#         Cursor.execute(command)
        
#         connection.commit()

        
with connection.cursor() as Cursor:

    command = f"select * from device"

    print(command)
    Cursor.execute(command)
    devices = Cursor.fetchall()

    for device in devices:
        url = f"http://checklight.pythonanywhere.com/get_readings/{device['code']}/1/" 
        response = requests.get(url)
        data = response.json()

        streets = data["streets"]

        for street in streets:
            status =  street["status"]
            post_datetime = datetime.datetime.strptime(street["time"], "%b. %d, %Y, %I:%M %p.")

            command = f"INSERT INTO data (device_id, post_time,status) values({device['id']},'{str(post_datetime)[:16]}',{status})"

            # print(command)
            Cursor.execute(command)
        
            connection.commit()