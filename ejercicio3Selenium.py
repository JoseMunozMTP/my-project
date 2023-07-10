"""
Imprimir por pantalla la temperatura en Madrid y añadir un mensaje indicando en cual de estas franjas está:
franja 1:  < 25ºC
franja 2:  25ºC < x < 30ºC
franja 3:  > 30ºC
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

T_B = 25
T_A = 30
CIUDAD = 'Riosa'

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get('https://www.google.com/search?q=tiempo+en+riosa&source=hp&ei=N9-rZLSnCP-lkdUPxeuNyA4&iflsig=AD69kcEAAAAAZKvtRxnID0nx5H-vSovAtiA_d0jFz8ZV&ved=0ahUKEwj0nvz1-IOAAxX_UqQEHcV1A-kQ4dUDCAs&uact=5&oq=tiempo+en+riosa&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOhAIABADEI8BEOoCEIwDEOUCOhAILhADEI8BEOoCEIwDEOUCOgsIABCABBCxAxCDAToLCC4QgAQQsQMQgwE6CwgAEIoFELEDEIMBOgsILhCKBRCxAxCDAToLCC4QgAQQxwEQ0QM6EAgAEIAEELEDEIMBEEYQgAI6DggAEIAEELEDEIMBEMkDOggIABCABBCSAzoICAAQigUQkgM6CAgAEIAEELEDUJsEWJ8QYI0RaAFwAHgAgAGZAYgBywySAQQxLjEzmAEAoAEBsAEK&sclient=gws-wiz')

    texto_temperatura = float(driver.find_element(By.ID, 'wob_tm').text)

    print (f'La temperatura en', CIUDAD,'es: ',texto_temperatura, 'grados')

    if texto_temperatura < T_B:
        print ('La temperatura es baja para la época')
    elif texto_temperatura > T_A:
        print ('La temperatura es alta')
    else:
        print ('La temperatura es la adecuada para la época')

finally:
    time.sleep(3)
    driver.close()
