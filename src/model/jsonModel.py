from datetime import date

def jsonCreate(urlEnterprises):
    jsonList = {
        "date":f'{date.today()}',
        "urlEnterprises": urlEnterprises,
    }
    print(jsonList)

    return jsonList

