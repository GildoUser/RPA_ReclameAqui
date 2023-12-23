import json
def updateCheck():
    with open('./src/db/db.txt','r',encoding='utf-8') as dataBase:
        data = dataBase.readlines()
    print(data)

def updateInsert(data):
    with open('./src/db/db.txt','w+',encoding='utf-8') as dataBase:
        dataBase.write(data)
obj = {'date': '2023-12-22', 'urlEnterprises': ['https://www.reclameaqui.com.br/empresa/vivo-celular-fixo-internet-tv', 'https://www.reclameaqui.com.br/empresa/hotel-urbano', 'https://www.reclameaqui.com.br/empresa/claro', 'https://www.reclameaqui.com.br/empresa/uber', 'https://www.reclameaqui.com.br/empresa/lojas-yec', 'https://www.reclameaqui.com.br/empresa/aes-eletropaulo', 'https://www.reclameaqui.com.br/empresa/aliexpress', 'https://www.reclameaqui.com.br/empresa/caixa-economica-federal', 'https://www.reclameaqui.com.br/empresa/instagram', 'https://www.reclameaqui.com.br/empresa/colchoes-ortobom', 'https://www.reclameaqui.com.br/empresa/samsung', 'https://www.reclameaqui.com.br/empresa/estacio', 'https://www.reclameaqui.com.br/empresa/facebook', 'https://www.reclameaqui.com.br/empresa/samsung-tv-eletrodomestico', 'https://www.reclameaqui.com.br/empresa/oi-internet', 'https://www.reclameaqui.com.br/empresa/everest-group', 'https://www.reclameaqui.com.br/empresa/123-milhas', 'https://www.reclameaqui.com.br/empresa/booking-com', 'https://www.reclameaqui.com.br/empresa/microsoft', 'https://www.reclameaqui.com.br/empresa/oi-movel-fixo-tv']}
updateInsert(json.dumps(obj))