from pytesseract import image_to_string
import pytesseract
import pymysql.connections

pytesseract.pytesseract.tesseract_cmd='C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
img='bill2.gif'
text=image_to_string(img,config=pytesseract.pytesseract.tesseract_cmd)


##Find merchant name
merchant_find=text.find("AROMA")
Merchantname=text[merchant_find+0:merchant_find+35 ]
print(Merchantname)

###Find date
ind_date=text.find("DATE")
Date=text[ind_date+6:ind_date+16 ]
print(Date)

###Find total
find_total=text.find('779.0')
Total=text[find_total+0:find_total+6 ]
print(Total)

# # Connect to the database.
connection = pymysql.connect(host='localhost',user='root',password='kushal14320',db='test')
print("connect successful!!")
cursor=connection.cursor()
sql = ("INSERT INTO COMPANY(COMPANY_NAME,DATE, TOTAL) VALUES (%s, %s, %s)")
VALUES=(Merchantname,Date, Total)
cursor.execute(sql,VALUES)
print('DATA inserted')