import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('Launch chrome browser')
def launchBrowser(context):
     context.driver = webdriver.Chrome()

@when('Open Orange Hrm Home page')
def openHomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

@then('verifythat the logo prasent on page')
def verifyLogo(context):
    time.sleep(2)
    status = context.driver.find_element(By.XPATH, "//img[@alt='company-branding']").is_displayed()
    assert status is True

@then('close browser')
def closeBrowser(context):
    context.driver.close()


