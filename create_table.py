import mysql.connector
mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="storemart"
)
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE customer (cust_id int, cust_name CHAR(25),cust_mob VARCHAR(15), cust_email CHAR(25),cust_address CHAR(20))")
mydb.close()
