import pytest
from selene import browser, have


@pytest.mark.parametrize(
    "viewport",
    [(1366, 768), (1920, 1080)],
    indirect=True
)
def test_desktop_sign_in_indirect(viewport):
    width, height = viewport

    if width <= height:
        pytest.skip("Mobile viewport — skip desktop test")

    browser.open("https://github.com/")
    browser.all("a[href*='login']").by(have.text("Sign in")).first.click()
    browser.should(have.url_containing("/login"))

