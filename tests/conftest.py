import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture
def viewport(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    return width, height


@pytest.fixture(scope="function", autouse=True)
def browser_setup():
    browser.config.driver = webdriver.Chrome()
    browser.config.timeout = 10
    yield
    browser.quit()


@pytest.fixture(params=[(1366, 768), (1920, 1080)])
def desktop_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield


@pytest.fixture(params=[(390, 844), (414, 896)])
def mobile_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
