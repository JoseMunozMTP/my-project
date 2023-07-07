from selenium import webdriver


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.get("https://the-internet.herokuapp.com/login")


def after_scenario(context, scenario):
    context.driver.quit()