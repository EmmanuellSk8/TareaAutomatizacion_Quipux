import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

texto_capital = '//*[@id="rso"]/div[1]/div/block-component/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/a'
buscador_text_area = '//*[@id="APjFqb"]'
capitales = []

paises = pd.read_excel('paises.xlsx')

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.google.com/')

for pais in paises['País']:
  
    driver.find_element(By.XPATH, buscador_text_area).send_keys("Capital de " + pais)

    driver.find_element(By.XPATH, buscador_text_area).submit()
    
    time.sleep(2)

    if len(driver.find_elements(By.XPATH, texto_capital)) > 0:
       
        capitales.append(driver.find_element(By.XPATH, texto_capital).text)
    else:
      
        capitales.append('Capital no encontrada')
  
    driver.find_element(By.XPATH, buscador_text_area).clear()

driver.close()

pd.DataFrame({'País': paises['País'], 'capital': capitales}).to_excel('Capitales.xlsx', index=False)
