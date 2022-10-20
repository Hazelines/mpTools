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

sql = "SELECT * FROM MPMIT.dbo.MPM_MENU"
mycursor.execute(sql)

result = ""

for table_name in mycursor:
    result += "<tr>"
    result += ("<td>" + table_name[0] + "</td>")
    result += ("<td>" + table_name[1] + "</td>")
    result += ("<td>" + table_name[2] + "</td>")
    result += ("<td>" + str(table_name[3]) + "</td>")
    result += ("<td>" + table_name[4] + "</td>")
    result += ("<td>" + table_name[5] + "</td>")
    result += ("<td>" + table_name[6] + "</td>")
    result += ("<td>" + table_name[7] + "</td>")
    result += "</tr>"

print(result)