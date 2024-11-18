from behave import *
from selenium import webdriver


@given(u'I launch Browser')
def step_impl(context):
    driver = webdriver.Edge()

@when(u'I Open application')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I Open application')


@when(u'Enter valid username and password')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Enter valid username and password')


@when(u'click on login')
def step_impl(context):
    raise NotImplementedError(u'STEP: When click on login')


@then(u'User must login to the Dashboard Page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User must login to the Dashboard Page')


@when(u'navigate to seacrh Page')
def step_impl(context):
    raise NotImplementedError(u'STEP: When navigate to seacrh Page')


@then(u'Search Page should be display')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Search Page should be display')


@when(u'navigate to Advance seacrh Page')
def step_impl(context):
    raise NotImplementedError(u'STEP: When navigate to Advance seacrh Page')


@then(u'Advance Page should be display')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Advance Page should be display')
