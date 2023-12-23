import json
from datetime import date

db_urlSrc = './src/db/db_urlEnterprise.txt'


def updateCheck():
    with open(db_urlSrc,'r',encoding='utf-8') as dataBase:
        data = json.load(dataBase)
            #if content
        print(data['date'],len(data['urlEnterprises']) ,"printando")
        if data['date'] != str(date.today()) or len(data['urlEnterprises']) <= 0:
            print('NOT up-to-date')
            return True
        else:
            print('entrou no else')
            return data


def updateInsert(data):
    dataSave = json.dumps(data)
    with open(db_urlSrc,'w+',encoding='utf-8') as dataBase:
        dataBase.write(dataSave)


