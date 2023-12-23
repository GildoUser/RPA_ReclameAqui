import json
from datetime import date
def updateCheck():
    with open('./src/db/db.txt','r',encoding='utf-8') as dataBase:
        data = json.load(dataBase)
        print(data['date'])
        if data['date'] != str(date.today()):
            print('NOT up-to-date')
            return True
        else:
            return False

def updateInsert(data):
    dataSave = json.dumps(data)
    with open('./src/db/db.txt','w+',encoding='utf-8') as dataBase:
        dataBase.write(dataSave)
