import pymssql
import sys

mydb = pymssql.connect(
    host="10.10.101.96",
    port="1433",
    user="appreader",
    password="Simpang4244",
    database="MPMIT"
)
f = open("sql/1. Insert Menu.sql", "x")
f.close
mycursor=mydb.cursor()

result = ""

for data in mycursor:
    result += ("<option value='" + data[0] + "'>" + data[0] + "</option>")

# data = [
#     "FLP338",
#     "FLP339",
#     "FLP340",
#     "FLP341",
#     "FLP342",
#     "FLP343",
#     "FLP344",
#     "FLP345",
#     "FLP346",
#     "FLP347",
#     "FLP348",
#     "FLP349",
#     "FLP350",
#     "FLP351",
#     "FLP352",
#     "FLP353",
#     "FLP354",
# ]

data = [
    "FLP353",
    "FLP354",
    "FLP355"
]

f = open("sql/1. Insert Menu.sql", "a")

for menu_id in data:
    sql = "SELECT * FROM MPMIT.dbo.MPM_MENU WHERE MENU_ID = '" + menu_id + "'"
    mycursor.execute(sql)
    for mpm_menu in mycursor:
        # print("INSERT INTO MPMIT.dbo.MPM_MENU")
        f.write("INSERT INTO MPMIT.dbo.MPM_MENU\n")
        result = "VALUES ('" + menu_id + "','FLPSUB001','MPM01'," + str(mpm_menu[3]) + ",'" + mpm_menu[4] + "','" + mpm_menu[5] + "','" + mpm_menu[6] + "','" + mpm_menu[7] + "', null,'SRV-0001','N','N','2016-01-01 00:00:00','2035-01-01 00:00:00','mpTools',GETDATE(),null,null)\n\n"
        f.write(result)

        # print(result)

    sql = "SELECT * FROM MPMIT.dbo.MPM_ROLES_LINE WHERE MENU_ID = '" + menu_id + "'"
    mycursor.execute(sql)
    for mpm_menu in mycursor:
        # print("INSERT INTO MPMIT.dbo.MPM_ROLES_LINE\n")
        f.write("INSERT INTO MPMIT.dbo.MPM_ROLES_LINE\n")
        result = "VALUES ('RO_FLP','" + menu_id + "','SRV-0001','Y','Y','Y','Y','Y','2016-01-01 00:00:00','2035-01-01 00:00:00','mpTools',GETDATE(),null,null)\n\n\n"
        f.write(result)
        # print(result)
        # print("\n")
    
f.close()