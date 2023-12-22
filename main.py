from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime

buscar = []
driver = webdriver.Chrome()
driver.get("https://www.reclameaqui.com.br/ranking/")
#search = driver.find_element(By.XPATH,'//*[@id="rankings"]/div/div[3]/div/div[8]/div/ol')


for i in range(0,20,1):
    id = f'link-topBadStatusOf30DaysCompanyMore{str(i)}-ranking'
    item = driver.find_element(By.ID,id)
    print(item.get_attribute('href'))
#//*[@id="rankings"]/div/div[3]/div/div[8]/div/ol/li[1]
    
driver.close()
print(buscar)