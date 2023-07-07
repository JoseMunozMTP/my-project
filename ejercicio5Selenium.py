"""
crear 10 elementos dándole a "add" en esta web

https://the-internet.herokuapp.com/add_remove_elements/

y luego borrarlos dándole a "delete"
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


URL= 'https://the-internet.herokuapp.com/add_remove_elements/'

DRIVER = webdriver.Chrome()

try:
    DRIVER.get(URL)
    boton_add_element = DRIVER.find_element(By.CSS_SELECTOR, '#content > div > button')
    for i in range(10):
        boton_add_element.click()
    for i in range (10):
        boton_Delete = DRIVER.find_element(By.CSS_SELECTOR, '#elements > button:nth-child(1)')
        boton_Delete.click()

finally:
    time.sleep(5)
    DRIVER.quit()
