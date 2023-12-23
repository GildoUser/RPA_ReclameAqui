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
        urlEnterprises.append(item.get_attribute('href'))

    driver.close()
    return urlEnterprises
