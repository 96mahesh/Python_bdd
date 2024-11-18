import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()

@when('I open orangeHrm Homepage')
def openHomePage(context):
    time.sleep(2)
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.driver.maximize_window()

@when(u'Enter username "{user}" and password "{pwd} "')
def setUserName(context,user , pwd):
    time.sleep(2)
    context.driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys(user)
    context.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(pwd)

@when(u'Click on login button')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()

@then(u'User must successfully login to the Dashboard page')
def step_impl(context):
    time.sleep(2)
    try:
        text = context.driver.find_element(By.XPATH, "// h6[text() = 'Dashboard']").text
    except:
        context.driver.close()
        assert False,"Test failed"
    if(text=="Dashboard"):
        context.driver.close()
        assert True,"Test passed"


