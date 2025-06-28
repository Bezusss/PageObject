import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from classes import browser_init
from classes.browser_init import Browser

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = Browser()
    yield browser
    print("\nquit browser..")
    browser.close_page()