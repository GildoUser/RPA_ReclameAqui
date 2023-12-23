from datetime import date

def jsonCreate(urlEnterprises):
    jsonList = {
        "date":f'{date.today()}',
        "urlEnterprises": urlEnterprises,
    }

    return jsonList


def jsonEnterprise():
    js= {
"name": "nomeEmpresa",
"recommended": "Não recomendada",
"score": "notaEmpresa/10",
"url": "urlEmpresa",
"unawnseredMsg": 0,
"avaliada": 0


}