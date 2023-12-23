from seleniumConfig.getConnection import startProcess_GettingData
from model.jsonModel import jsonCreate



urlEnterprises = startProcess_GettingData()
#return a array with all links (20)

jsonObject = jsonCreate(urlEnterprises) 
#return {date: today, urlEnterprises: [ urls, ...]}










#search = driver.find_element(By.XPATH,'//*[@id="rankings"]/div/div[3]/div/div[8]/div/ol')



#//*[@id="rankings"]/div/div[3]/div/div[8]/div/ol/li[1]

# jsonCreate(urlEnterprises)
# print(urlEnterprises)


