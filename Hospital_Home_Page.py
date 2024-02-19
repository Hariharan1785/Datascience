# Hospital Management Front Page 

import mysql.connector
cnx = mysql.connector.connect(
     host='localhost',
    user= 'root',
    password='root',
    database= 'hospital_management',
)
if cnx.is_connected():

    with cnx.cursor() as cursor:

        print("***************************************************")

        print("*************Hospital Management System !!!***************");

        print("**************Himalayan Hospital Welcomes You!!!!****************")

        print("*************Contact Details Here !!!!!*****************************");
        
        result = cursor.execute("SELECT * FROM hospital_details")

        rows = cursor.fetchall()

        for rows in rows:

            print(rows)
        print("Thank you for Visiting!!!,,,Have a Speedy Recovery!!!")
        print("######################################################")

    cnx.close()

else:

    print("Could not connect")

