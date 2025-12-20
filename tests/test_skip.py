import pytest
from selene import browser, be, have


@pytest.mark.parametrize(
    "window_size",
    [
        (390, 844),  # mobile
        (1366, 768),  # desktop → должен быть skipped
    ]
)
def test_mobile_sign_in_with_skip(window_size):
    width, height = window_size

    # если соотношение сторон десктопное — пропускаем mobile-тест
    if width > height:
        pytest.skip("Desktop aspect ratio — skip mobile test")

    browser.config.window_width = width
    browser.config.window_height = height

    browser.open("https://github.com/")
    browser.element("a[href='/login']").should(be.visible).click()


@pytest.mark.parametrize(
    "window_size",
    [
        (1366, 768),  # desktop
        (390, 844),  # mobile → должен быть skipped
    ]
)
def test_desktop_sign_in_with_skip(window_size):
    width, height = window_size

    # если соотношение сторон мобильное — пропускаем desktop-тест
    if width <= height:
        pytest.skip("Mobile aspect ratio — skip desktop test")

    browser.config.window_width = width
    browser.config.window_height = height

    browser.open("https://github.com/")
    browser.all("a[href*='login']").by(have.text("Sign in")).first.click()

