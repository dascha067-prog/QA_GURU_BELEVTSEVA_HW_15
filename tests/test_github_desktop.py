import pytest
from selene import browser, have


@pytest.mark.parametrize(
    "desktop_window",
    [
        (1366, 768),
        (1920, 1080),
        (390, 844),  # будет пропущен
    ],
    indirect=True
)
def test_sign_in_desktop(desktop_window):
    browser.open("https://github.com/")

    browser.all("a[href*='login']").by(have.text("Sign in")).first.click()
    browser.should(have.url_containing("/login"))
