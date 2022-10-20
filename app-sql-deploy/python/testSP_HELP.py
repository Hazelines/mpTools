import pymssql
import sys

mydb = pymssql.connect(
    host="10.10.101.96",
    port="1433",
    user="appreader",
    password="Simpang4244",
    database="MPMFLP"
)

mycursor=mydb.cursor()

# sql = "sp_help MPMFLPREALISASIBIAYA"
sql = "sp_helptext MPM_FLP_SP_BLUE_FEFTRAINING_LIST_TRAINER_PRINT"
mycursor.execute(sql)

for data in mycursor:
    # while(str(data).find("('")):
    #     data = str(data).replace("('", "")
    #     print("1. " + data)
    # while(str(data).find("\\r\\n")):
    #     data = str(data).replace("\\r\\n", "")
    #     print("2. " + data)
    # while(str(data).find("\\t")):
    #     data = str(data).replace("\\t", " ")
    #     print("3. " + data)
    # while(str(data).find("',)")):
    #     data = str(data).replace("',)", "")
    #     print("4. " + data)
    " ".join(data.splitlines())
    print(data)

# tableInfo = mycursor.fetchall()
# print(tableInfo)

# mycursor.nextset()

# columnInfo = mycursor.fetchall()
# print(columnInfo)