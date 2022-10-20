from argparse import _MutuallyExclusiveGroup
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

menuExist = 0
sqlCheckMenuExist = "SELECT COUNT(*) AS COUNTERS FROM MPMIT.dbo.MPM_MENU WHERE MENU_ID LIKE '%" + sys.argv[1] + "%'"
mycursor.execute(sqlCheckMenuExist)
for num in mycursor:
    menuExist += int(str(num[0]))

runningNumber = 1
orderedNumber = 1
if (menuExist > 0):
    #Get Menu ID Running Number
    sqlRunningNumberId = "SELECT MAX(CAST(SUBSTRING(MENU_ID, LEN('" + sys.argv[1] + "') + 1, LEN(MENU_ID)) AS INT)) AS number"
    sqlRunningNumberId += " FROM MPMIT.dbo.MPM_MENU "
    sqlRunningNumberId += " WHERE MENU_ID LIKE '%" + sys.argv[1] + "%' "
    mycursor.execute(sqlRunningNumberId)

    for number in mycursor:
        runningNumber += int(str(number[0]))

    #Get Max Ordered Number
    sqlOrderedNumber = "SELECT COALESCE(MAX(ORDERED_NUMBER), 0) "
    sqlOrderedNumber += " FROM MPMIT.dbo.MPM_MENU "
    sqlOrderedNumber += " WHERE MENU_ID LIKE '%" + sys.argv[1] + "%' "
    sqlOrderedNumber += " AND PROCESS_GROUP_NAME LIKE '%" + sys.argv[4] + "%' "
    
    mycursor.execute(sqlOrderedNumber)
    for number in mycursor:
        orderedNumber += int(str(number[0]))
else:
    print(menuExist)

sqlInsertMenu = "INSERT INTO MPMIT.dbo.MPM_MENU " + \
    " VALUES " + \
    " ('" + sys.argv[1] + str(runningNumber) + "', " + \
    "'" + sys.argv[2] + "'," + \
    "'" + sys.argv[3] + "'," + \
    str(orderedNumber) + "," + \
    "'" + sys.argv[4] + "'," + \
    "'" + sys.argv[5] + "'," + \
    "'" + sys.argv[6] + "'," + \
    "'" + str(sys.argv[1]).lower() + "/" + sys.argv[5] + "'," + \
    "null, " + \
    "'SRV-0001', " + \
    "'N', " + \
    "'N', " + \
    "'2020-01-01 10:36:48.000', " + \
    "'2045-01-01 10:36:48.000', " + \
    "'mpTools', " + \
    "GETDATE(), " + \
    "null, " + \
    "null " + \
    ")"
mycursor.execute(sqlInsertMenu)
mydb.commit()

sqlInsertRolesLine = "INSERT INTO MPMIT.dbo.MPM_ROLES_LINE " + \
    " VALUES " + \
    " ('" + sys.argv[7] + "', " + \
    "'" + sys.argv[1] + str(runningNumber) + "', " + \
    "'SRV-0001', " + \
    "'Y', " + \
    "'Y', " + \
    "'Y', " + \
    "'Y', " + \
    "'Y', " + \
    "'2020-01-01 10:36:48.000', " + \
    "'2045-01-01 10:36:48.000', " + \
    "'mpTools', " + \
    "GETDATE(), " + \
    "null, " + \
    "null " + \
    ")"
mycursor.execute(sqlInsertRolesLine)
mydb.commit()