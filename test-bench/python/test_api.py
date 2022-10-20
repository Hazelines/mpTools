import requests
import pymssql
import sys

mydb = pymssql.connect(
    host="10.10.106.177",
    port="1433",
    user="appreader",
    password="Simpang4244",
    database="MPMMKT"
)

mycursor=mydb.cursor()
mycursorDealer=mydb.cursor()
mycursorAttachment=mydb.cursor()

idsalesprog1 = "B348305D-5C5A-4CF6-849F-BAAA1C82AFD1"
# idsalesprog2 = "E3AD178C-C25A-46D2-88CF-EA43AB22F68A"

sql = "SELECT * FROM MPMMKT.dbo.MPM_MASTERSALESPROGRAM WHERE IDSALESPROGRAM = '" + idsalesprog1 + "'"
mycursor.execute(sql)

sqlDealer = "SELECT KODEDEALER FROM MPMMKT.dbo.MPM_MASTERSALESPROGRAM_DETAILDEALER WHERE IDSALESPROGRAM = '" + idsalesprog1 + "'"
mycursorDealer.execute(sqlDealer)

sqlAttachment = "SELECT * FROM MPMMKT.dbo.MPM_MASTERSALESPROGRAM_DETAILDEALER WHERE IDSALESPROGRAM = '" + idsalesprog1 + "'"
mycursorAttachment.execute(sqlAttachment)

api_url = "https://api.mpm-motor.com/sdms/mulia/slsprog/api/1.0/sendclmslsprog/submitdata"

todo_doc = [
                {
                    "docType": "8",
                    "docTypeDesc": "KTP",
                    "idGambar": "a822dc86-1c30-4a81-ba73-a6ccec96c32b"
                },
                {
                    "docType": "9",
                    "docTypeDesc": "STNK motor sebelumnya (tipe motor honda)",
                    "idGambar": "4c27b754-56bc-4c12-b232-16c2cd584160"
                },
                {
                    "docType": "17",
                    "docTypeDesc": "BAST Unit",
                    "idGambar": "294f8e6f-a2ec-4acf-9005-2c4e0be8a875"
                },
                {
                    "docType": "16",
                    "docTypeDesc": "Invoice Dealer",
                    "idGambar": "4cf46d9a-359f-468b-ac2d-28079f3c6b00"
                },
                {
                    "docType": "10",
                    "docTypeDesc": "KK",
                    "idGambar": "d9e073e7-1ec5-4bcb-a46e-59c20856311e"
                }
            ]

todo_unit = {
            "type": "JXJ",
            "typeDesc": "CB150X STD JKT",
            "subAhm": 444000,
            "subMd": 333000,
            "subDealer": 111000,
            "unitPrice": 22200000,
            "subFincoy": 0,
            "color": "MS",
            "colorDesc": "MERAH SILVER",
            "idMachine": "HB32E1222727",
            "idFrame": "KCE114NK005955",
            "document": todo_doc
        }

todo = [
    {
        "idCustBuyer": "02523-N0002-2022",
        "custBuyerName": "HUA HUA HUA",
        "custIdentity": "936505400001321",
        "idCustStnk": "02523-N0002-2022",
        "custStnkName": "HUA HUA HUA",
        "custStnkIdentity": "936505400001321",
        "juklakNo": "L.MPM.MULIA/EXT/GM-ARO/MSD/ZXCZXC/VI/2022",
        "descJuklak": "Test.ABDE",
        "idProgSdms": "da7d2804-2cd8-4ce2-bc4b-121f04a5953e",
        "vsoDate": " 2022-06-13",
        "vsoNumber": "0362022-00002715",
        "uniqueCustomer": "true",
        "target": 0,
        "ivuNumber": "IVU-ASD-QWE-123",
        "ivuDate": " 2022-06-13",
        "idFlp": "108312",
        "saleTypeDesc": "Cash",
        "saleTypeId": "20",
        "dealerCode": "N0002",
        "ahmCode": "12084",
        "modifiedDate": " 2022-06-15",
        "statusCode": "",
        "statusDesc": "",
        "idTransClmSlsProgMd": "",
        "idDocBast": "",
        "docBastDate": "",
        "fincoyCode": "",
        "fincoyDesc": "",
        "unit": todo_unit
    }
]

# G1350

# for res in mycursor:
#     for resDetail in res:
#         print(resDetail)

# api_url = "https://api.mpm-motor.com/sdms/acs/slsprog/api/v1/base64gambar/read"
# todo = {
#     "ahmcode": "16841",
#     "mdcode": "H3930",
#     "idgambar": "65424a2a-3131-4b91-8d58-760ab132bedc"
# }

response = requests.post(api_url, json=todo)
itemResponse = response.json()

print(itemResponse)