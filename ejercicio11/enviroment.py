from selenium import webdriver


def before_scenario(Context, scenario):
    Context.driver = webdriver.Chrome()


def after_scenario(Context, scenario):
    Context.driver.quit()