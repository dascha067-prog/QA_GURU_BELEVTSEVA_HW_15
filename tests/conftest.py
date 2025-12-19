import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="function", autouse=True)
def browser_setup():
    browser.config.driver = webdriver.Chrome()
    browser.config.timeout = 10
    yield
    browser.quit()


@pytest.fixture
def desktop_window(request):
    width, height = request.param
    aspect_ratio = width / height

    # если соотношение сторон мобильное — пропускаем desktop-тест
    if aspect_ratio <= 1:
        pytest.skip("Mobile aspect ratio is not applicable for desktop test")

    browser.config.window_width = width
    browser.config.window_height = height

    return width, height


@pytest.fixture
def mobile_window(request):
    width, height = request.param
    aspect_ratio = width / height

    # если соотношение сторон десктопное — пропускаем mobile-тест
    if aspect_ratio > 1:
        pytest.skip("Desktop aspect ratio is not applicable for mobile test")

    browser.config.window_width = width
    browser.config.window_height = height

    return width, height
