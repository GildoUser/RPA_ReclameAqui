from datetime import date
from seleniumConfig.getConnection import getEnterpriseInfo
from db.db_enterpriseControl import saveEnterprisesData
def jsonCreate(urlEnterprises):
    jsonList = {
        "date":f'{date.today()}',
        "urlEnterprises": urlEnterprises,
    }

    return jsonList

arrayData = []
def createJsonEnterprise(urlEnterprise):
    print('url recebida', urlEnterprise)
    dataInfo = getEnterpriseInfo(urlEnterprise) #recebe jsonEnterprise json configurado e pronto
    arrayData.append(dataInfo)
    if len(arrayData) >= 20:
        saveEnterprisesData(arrayData)
