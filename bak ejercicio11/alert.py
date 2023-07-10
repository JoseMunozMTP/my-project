"""
hacer un plan de pruebas de esta página https://the-internet.herokuapp.com/javascript_alerts con behave
"""


from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

step_matcher('re')
driver = webdriver.Chrome()


@given('el usuario accede al portal')
def step_impl(context):
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")


@when('el usuario clica en el boton "Click for JS Alert"')
def step_impl(context):
    driver.find_element(By.CSS_SELECTOR, '#content > div > ul > li:nth-child(1) > button').click()


@when('el usuario clica en el boton "Click for JS Confirm"')
def step_impl(context):
    driver.find_element(By.CSS_SELECTOR, '#content > div > ul > li:nth-child(2) > button').click()


@when('el usuario clica en "(?P<mensaje>.+)"')
def step_impl(mensaje):
    if mensaje == 'Aceptar':
        Alert(driver).accept()
    else:
        Alert(driver).dismiss()


@then('aparece el mensaje "(?P<mensaje>.+)"')
def step_impl(context, mensaje):
    assert mensaje == driver.find_element(By.ID, 'result').text