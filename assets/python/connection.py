import pymssql
import sys

mydb = pymssql.connect(
    host="10.10.101.96",
    port="1433",
    user="appreader",
    password="Simpang4244",
    database="MPMIT"
)

mycursor=mydb.cursor()

sql = "SELECT TOP(10)* FROM MPMIT.dbo.MPM_MENU WHERE MENU_ID LIKE '%" + sys.argv[1] + "%'"
mycursor.execute(sql)

for table_name in mycursor:
   print(table_name[0])