from selene import browser, be, have


def test_sign_in_desktop_with_fixture(desktop_browser):
    browser.open("https://github.com/")
    browser.all("a[href*='login']").by(have.text("Sign in")).first.click()
    browser.should(have.url_containing("/login"))


def test_sign_in_mobile_with_fixture(mobile_browser):
    browser.open("https://github.com/")
    browser.element("a[href='/login']").should(be.visible).click()
    browser.should(have.url_containing("/login"))
