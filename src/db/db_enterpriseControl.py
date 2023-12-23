import json
from datetime import date

db_enterpriseLocal = './src/db/db_enterpriseData.txt'

def saveEnterprisesData(enterpriseData):
    array = {"empresas": enterpriseData}
    dataSave = json.dumps(array)
       # loadData = readEnterprisesData()
    with open(db_enterpriseLocal,'w+',encoding='utf-8') as dataBase:
        dataBase.write(dataSave)


"""if response == True:
    print('deu erro, entrou e vai buscar update')
    with open('./src/db/db_enterpriseData.txt','w+') as dataBase:
        dataBase.write('')
    urlEnterprises = startProcess_GettingData()
    jsonObject = jsonCreate(urlEnterprises)
    updateInsert(jsonObject)"""
# def readEnterprisesData():
#     try:
#         with open(db_enterpriseLocal,'r', encoding='utf-8') as dataBase:
#             data = json.load(dataBase)
#             print(data)
#         return data
#     except: 
#         print('...')


