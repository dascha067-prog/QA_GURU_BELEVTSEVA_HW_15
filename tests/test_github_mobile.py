import pytest
from selene import browser, be


@pytest.mark.skip(reason="Mobile layout does not require separate test for Sign in")
@pytest.mark.parametrize(
    "window_size",
    [
        (390, 844),
        (414, 896),
    ]
)
def test_sign_in_mobile(window_size):
    width, height = window_size
    browser.config.window_width = width
    browser.config.window_height = height

    browser.open("https://github.com/")
    browser.element("a[href='/login']").should(be.visible).click()

