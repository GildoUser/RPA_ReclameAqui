from seleniumConfig.getConnection import startProcess_GettingData
from model.jsonModel import jsonCreate,createJsonEnterprise
from db.db_urlControl import updateCheck, updateInsert

#check update to see if dateLastUpdate != today.   if true > update database 
response = updateCheck()

#print(response)# data nome valuev
if response == True:
    print('deu erro, entrou e vai buscar update')
    urlEnterprises = startProcess_GettingData()
    jsonObject = jsonCreate(urlEnterprises)
    updateInsert(jsonObject)

#all ok, with response
#print(type(response))
for item in response['urlEnterprises']:
    for key,value in item.items():
        createJsonEnterprise(value) #passando url
#        chamafuncaoQuerecebeurl e retorna o json criado()
#pra cada item add name e look like model 

# for item in response:
#     accessEnterpriseUrl(item)

#return {date: today, urlEnterprises: [ urls, ...]}


#reference
#updateInsert(json.dumps(obj))









#search = driver.find_element(By.XPATH,'//*[@id="rankings"]/div/div[3]/div/div[8]/div/ol')



#//*[@id="rankings"]/div/div[3]/div/div[8]/div/ol/li[1]

# jsonCreate(urlEnterprises)
# print(urlEnterprises)


