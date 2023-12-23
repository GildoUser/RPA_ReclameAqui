from seleniumConfig.getConnection import startProcess_GettingData
from model.jsonModel import jsonCreate
from db.dbControl import updateCheck, updateInsert


if updateCheck():
    print('entrou')
    urlEnterprises = startProcess_GettingData()
    jsonObject = jsonCreate(urlEnterprises)
    updateInsert(jsonObject)


#return a array with all links (20)

#return {date: today, urlEnterprises: [ urls, ...]}


#reference
#updateInsert(json.dumps(obj))









#search = driver.find_element(By.XPATH,'//*[@id="rankings"]/div/div[3]/div/div[8]/div/ol')



#//*[@id="rankings"]/div/div[3]/div/div[8]/div/ol/li[1]

# jsonCreate(urlEnterprises)
# print(urlEnterprises)


