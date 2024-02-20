#Physician Details Fetched

import mysql.connector
cnx = mysql.connector.connect(
     host='localhost',
    user= 'root',
    password='root',
    database= 'hospital_management',
)
if cnx.is_connected():

    with cnx.cursor() as cursor:

        print("******Hospital Management System !!!*******");

        print("MYSQL DB is Connected with Python Code and Physician Details Fetched from Hospital Management Database ")

        print("Physician Details !!!!");
        
        result = cursor.execute("SELECT * FROM Physician_details")

        rows = cursor.fetchall()

        for rows in rows:

            print(rows)

    cnx.close()

else:

    print("Could not connect")

