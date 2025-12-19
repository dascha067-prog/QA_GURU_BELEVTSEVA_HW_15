import pytest
from selene import browser, have


@pytest.mark.parametrize(
    "window_size",
    [
        (1366, 768),
        (1920, 1080),
    ]
)
def test_sign_in_desktop(window_size):
    width, height = window_size
    browser.config.window_width = width
    browser.config.window_height = height

    browser.open("https://github.com/")

    #  click Sign in
    browser.all("a[href*='login']").by(have.text("Sign in")).first.click()

    # verify redirect
    browser.should(have.url_containing("/login"))
