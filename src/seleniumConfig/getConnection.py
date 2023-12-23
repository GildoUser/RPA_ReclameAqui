from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


urlEnterprises = []


def startProcess_GettingData():
    driver = webdriver.Chrome()
    driver.get("https://www.reclameaqui.com.br/ranking/")
    lenDriver = len(driver.find_elements(By.XPATH,'//*[@id="rankings"]/div/div[3]/div/div[8]/div/ol/li'))

    for i in range(lenDriver):
        id = f'link-topBadStatusOf30DaysCompanyMore{str(i)}-ranking'
        item = driver.find_element(By.ID,id)
        keyValue = {item.get_attribute('title'):item.get_attribute('href')}
        urlEnterprises.append(keyValue)
    driver.close()
    return urlEnterprises


def getEnterpriseInfo(urlEnterprise):
        driver = webdriver.Chrome()
        driver.get(urlEnterprise)
        driver.find_element(By.XPATH,'//*[@id="reputation-tab-5"]').click()

        #print(data,data.innerText)
        # for item in range(0,-1,-1):
        #      print(data[item].get_attribute('innerText'))
        try:
            nome = driver.find_element(By.XPATH,'//*[@id="hero"]/div[2]/div/div[2]/div[1]/h1').get_attribute('innerText')
        except:
            nome = "Not find"
        try:
            recomendado =  driver.find_element(By.XPATH,'//*[@id="reputation"]/div[1]/div[1]/div[2]/span[1]').get_attribute('innerText')
        except:          
            recomendado = "Not find"
        try:
             nota = driver.find_element(By.XPATH,'//*[@id="reputation"]/div[1]/div[1]/div[2]/span[2]/b').get_attribute('innerText') + "/10"
        except:
             nota = "Not find"
        try:
            setUpData = driver.find_elements(By.XPATH,'//*[@id="reputation"]/div[2]/div[2]/div[1]/a/div/b')
            data = setUpData[0].get_attribute('innerText')
            naoRespondido = data[1:]
        except:
             naoRespondido = 'Not find'

        try:
             avaliadas = driver.find_element(By.XPATH,'//*[@id="reputation"]/div[2]/div[2]/div[2]/a/div/b').get_attribute('innerText')
        except:
             avaliadas = 'Not find'
        jsonEnterprise = {
             "nome": nome,
             "recomendado": recomendado,
             "nota": nota,
             "naoRespondido": naoRespondido,
             "avaliadas": avaliadas

        }

        print(jsonEnterprise, 'ESSE É O JSON')
        return jsonEnterprise
