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

sql = "SELECT CATEGORY_ID FROM MPMIT.dbo.MPM_MENU GROUP BY CATEGORY_ID ORDER BY CATEGORY_ID"
mycursor.execute(sql)

result = ""

for data in mycursor:
    result += ("<option value='" + data[0] + "'>" + data[0] + "</option>")

print(result)