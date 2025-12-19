import pytest
from selene import browser, be


@pytest.mark.parametrize(
    "mobile_window",
    [
        (390, 844),
        (414, 896),
        (1366, 768),  # будет пропущен
    ],
    indirect=True
)
def test_sign_in_mobile(mobile_window):
    browser.open("https://github.com/")

    browser.element("a[href='/login']").should(be.visible).click()
