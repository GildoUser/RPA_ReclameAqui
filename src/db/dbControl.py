
def updateCheck():
    with open('db.txt','r') as dataBase:
        data = dataBase.readlines()
    print(data)

    
updateCheck()