import pymssql
import sys

mydb = pymssql.connect(
    host="10.10.101.96",
    port="1433",
    user="appreader",
    password="Simpang4244",
    # database="MPMHC3"
    database="MPMFLP"
)

mycursor=mydb.cursor()

# sql = "sp_help MPMHC3SURVEY"
# sql = "sp_help MPMFLPTESTINGCREATEWITHPRIMARY"
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

    data = str(data).replace("\\r\\n", "")
    data = str(data).replace("('", "")
    data = str(data).replace("\\t", " ")
    data = str(data).replace("',)", "")
    print(data)


# mycursor.nextset()
# columnInfo = mycursor.fetchall()
# for column in columnInfo:
#     print(column[0] + ", " + column[1])
# mycursor.nextset()
# mycursor.nextset()
# mycursor.nextset()
# error ndek sini
# mycursor.nextset()
# primaryInfo = mycursor.fetchall()
# if len(primaryInfo) > 0:
#     for primary in primaryInfo:
#         print(primary[2])

# error ndek sini ?
# mycursor.nextset()