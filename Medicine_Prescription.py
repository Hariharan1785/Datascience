#Medicine Prescription Details Fetched

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

        print("Medicine Prescription Details Fetched from Hospital Management Database ")

        print("Medicine Prescription Details !!!!");
        
        result = cursor.execute("SELECT * FROM medicine")

        rows = cursor.fetchall()

        for rows in rows:

            print(rows)

    cnx.close()

else:

    print("Could not connect")

