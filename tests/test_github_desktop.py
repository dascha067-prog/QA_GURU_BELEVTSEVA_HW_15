import pytest
from selene import browser, have


@pytest.mark.parametrize(
    "window_size",
    [
        (1366, 768),
        (1920, 1080),
        (390, 844),  # mobile
    ]
)
def test_sign_in_desktop(window_size):
    width, height = window_size

    if width < 768:
        pytest.skip("Mobile resolution is not applicable for desktop test")

    browser.config.window_width = width
    browser.config.window_height = height

    browser.open("https://github.com/")

    browser.all("a[href*='login']").by(have.text("Sign in")).first.click()
    browser.should(have.url_containing("/login"))
