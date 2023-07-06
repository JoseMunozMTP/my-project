"""
marcar los checks de esta url https://the-internet.herokuapp.com/checkboxes con el resultado de hacer una petición GET
 a esta otra url: https://mtp.alejmans.dev/maas/proxy/test/checkbox . true => debe estar marcado,
 false => debe estar desmarcado
"""

import requests, json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://mtp.alejmans.dev/maas/proxy/test/checkbox"
response = requests.get(url)
data = response.json()

print('checkbox 1:', data['checkbox 1'])# json
print('checkbox 2:', data['checkbox 2'])# json


CheckBox_1 = data['checkbox 1']
CheckBox_2 = data['checkbox 2']

driver = webdriver.Chrome()
driver.maximize_window()


try:
    driver.get('https://the-internet.herokuapp.com/checkboxes')

    element_CheckBox_1 =driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[1]')
    element_CheckBox_2 =driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[2]')

    """if CheckBox_1 == True and driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[1]').is_selected() != True:
        elemento_checkbox_1 = driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[1]').click()
    elif CheckBox_1 == False and driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[1]').is_selected() == True:
        elemento_checkbox_1 = driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[1]').click()"""

# Lógica reducida
    if CheckBox_1:
        if element_CheckBox_1.is_selected() != True:
            element_CheckBox_1.click()
    else:
        if element_CheckBox_1.is_selected():
           element_CheckBox_1.click()

    """if CheckBox_2 == True and driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[2]').is_selected() != True:
        elemento_checkbox_2 = driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[2]').click()
    elif CheckBox_2 == False and driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[2]').is_selected() == True:
        elemento_checkbox_2 = driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[2]').click()"""

# Lógica reducida
    if CheckBox_2:
        if element_CheckBox_2.is_selected() != True:
            element_CheckBox_2.click()
    else:
        if element_CheckBox_2.is_selected():
            element_CheckBox_2.click()
finally:
    time.sleep(3)
    driver.quit()