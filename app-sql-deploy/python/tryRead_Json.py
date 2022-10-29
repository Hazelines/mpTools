import json
from re import L
from venv import create
import pymssql
import sys
import os

with open('../json/tempData.json', 'r') as data:
    data = json.load(data)

    projectName = ""
    for projectname in data["projectname"]:
        projectName = projectname

    dbSchema = ""

    for schema in data["schema"]:
        dbSchema = schema

    mydb = pymssql.connect(
        host="10.10.101.96",
        port="1433",
        user="appreader",
        password="Simpang4244",
        database=dbSchema
    )
    mycursor=mydb.cursor()
    
    for table in data["table"]:
        sql = "sp_help " + table
        mycursor.execute(sql)
        mycursor.nextset()
        createTableSql = "USE " + dbSchema + "\n\n CREATE TABLE " + table + " ( \n"
        columnInfo = mycursor.fetchall()
        for column in columnInfo:
            addColumn = ""
            nullable = " NULL,\n"
            if column[6] == "no":
                nullable = " NOT NULL,\n"
            if column[1] == "varchar" or column[1] == "nvarchar":
                addColumn = " " + column[0] + " " + column[1] + "(" + str(column[3]) + ")" + nullable
            else:
                addColumn = " " + column[0] + " " + column[1] + nullable
            createTableSql += addColumn

        l = len(createTableSql)
        createTableSql = createTableSql[:l-2]
        createTableSql += "\n"

        mycursor.nextset()
        mycursor.nextset()
        mycursor.nextset()
        # Checking Primary Key
        mycursor.nextset()
        primaryInfo = mycursor.fetchall()
        if len(primaryInfo) > 0:
            for primary in primaryInfo:
                addPrimary = " PRIMARY KEY (" + primary + ") )"
                createTableSql += addPrimary
        else:
            createTableSql += ");\n"
        
        # print(createTableSql)

        if not os.path.exists("sql/" + projectName):
            os.mkdir("sql/" + projectName)

        if not os.path.exists("sql/" + projectName + "/table"):
            os.mkdir("sql/" + projectName + "/table")

        pathWithTable = "sql/" + projectName + "/table/" + table + ".sql"

        if os.path.exists(pathWithTable):
            os.remove(pathWithTable)

        f = open(pathWithTable, "x")
        f.close

        f = open(pathWithTable, "a")
        f.write(createTableSql)
        f.close

        print("Table : " + table + " created")

    for storedprocedure in data["storedprocedure"]:
        sql = "sp_helptext " + storedprocedure
        mycursor.execute(sql)

        storedProcedureQuery = "USE " + dbSchema + "\n"

        for data in mycursor:
            data = str(data).replace("\\r\\n", "")
            data = str(data).replace("('", "")
            data = str(data).replace("\\t", " ")
            data = str(data).replace("',)", "")
            storedProcedureQuery += data + "\n"
        
        if not os.path.exists("sql/" + projectName + "/storedprocedure"):
            os.mkdir("sql/" + projectName + "/storedprocedure")

        pathWithTable = "sql/" + projectName + "/storedprocedure/" + storedprocedure + ".sql"

        if os.path.exists(pathWithTable):
            os.remove(pathWithTable)

        f = open(pathWithTable, "x")
        f.close

        f = open(pathWithTable, "a")
        f.write(storedProcedureQuery)
        f.close

        print("Stored Procedure : " + storedprocedure + " created")