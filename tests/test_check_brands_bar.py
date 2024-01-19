import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be


def test_check_brands_bar():
    with allure.step('Verify app is launched'):
        browser.element((AppiumBy.CLASS_NAME, 'android.widget.EditText')).should(be.visible)

    with allure.step('Open "Brands" bar'):
        browser.element((AppiumBy.XPATH, '//*[@text="Бренды"]/..')).click()
        browser.element((AppiumBy.XPATH, '//*[@text="Топ-бренды"]')).should(be.visible)
        browser.element((AppiumBy.XPATH, '//*[@text="Все бренды"]')).should(be.visible)
