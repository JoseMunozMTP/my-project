"""
hacer un plan de pruebas de esta página https://the-internet.herokuapp.com/javascript_alerts con behave
"""


from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

use_step_matcher('re')
#driver = webdriver.Chrome()

@given('el usuario accede al portal')
def step_impl(context):
    context.driver.get("https://the-internet.herokuapp.com/javascript_alerts")


@when('el usuario clica en el boton "Click for JS Alert"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '#content > div > ul > li:nth-child(1) > button').click()


@when('el usuario clica en el boton "Click for JS Confirm"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '#content > div > ul > li:nth-child(2) > button').click()


@when('el usuario clica en el boton "Click for JS Prompt"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '#content > div > ul > li:nth-child(3) > button').click()



@when('el usuario clica en "(?P<mensaje>.+)"')
def step_impl(context, mensaje):
    if mensaje == 'Aceptar':
        Alert(context.driver).accept()
    else:
        Alert(context.driver).dismiss()




@when('el usuario escribe "Pepe" en el campo')
def step_impl(context):
    alert = Alert(context.driver)
    alert.send_keys('Pepe')
    time.sleep(1)

@then('aparece el mensaje "(?P<mensaje>.+)"')
def step_impl(context, mensaje):
    assert mensaje == context.driver.find_element(By.ID, 'result').text



