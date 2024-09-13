import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


url = 'https://cvv.org.br/'
driver.get(url)


wait = WebDriverWait(driver, 10)

botao_aceitartodos = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'aceitar-todos')))
botao_aceitartodos.click()

estado_select = wait.until(EC.presence_of_element_located((By.ID, 'estado')))
estado_dropdown = Select(estado_select)
estado_dropdown.select_by_value('MG')


cidade_select = wait.until(EC.presence_of_element_located((By.ID, 'cidade')))
cidade_dropdown = Select(cidade_select)
cidade_dropdown.select_by_value('UBERLÂNDIA')


buscar_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="submit"]')))
buscar_button.click()


time.sleep(2) 


elementos_p = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'p')))


elementos_p = elementos_p[25:29]

for elementos in elementos_p:
    print(elementos.text)

time.sleep(1)

# Feche o navegador
driver.quit()
