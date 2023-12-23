
def updateCheck():
    with open('db.txt','r',encoding='utf-8') as dataBase:
        data = dataBase.readlines()
    print(data)


updateCheck()