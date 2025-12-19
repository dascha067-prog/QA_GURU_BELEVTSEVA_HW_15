import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="function", autouse=True)
def browser_setup():
    browser.config.driver = webdriver.Chrome()
    browser.config.timeout = 10

    yield

    browser.quit()
