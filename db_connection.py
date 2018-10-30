import pymysql.cursors
import pymysql.connections


# Connect to the database.
connection = pymysql.connect(host='localhost',user='root',password='kushal14320',db='test')
print("connect successful!!")

##Create table
cursor = connection.cursor()

sql = """CREATE TABLE COMPANY (

    ID INT NOT NULL AUTO_INCREMENT,
    COMPANY_NAME varchar(100) NOT NULL,
    DATE CHAR(12) NOT NULL,
    TOTAL CHAR(20) NOT NULL,
    PRIMARY KEY (ID)
);
   """
print('Table created succesfully ')
try:
    cursor.execute(sql)
except Exception as ex:
    print(ex)

