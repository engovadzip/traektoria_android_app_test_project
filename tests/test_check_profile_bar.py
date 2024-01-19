import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be


@allure.story('Check "Profile" bar opens correct')
def test_check_profile():
    with allure.step('Verify app is launched'):
        browser.element((AppiumBy.CLASS_NAME, 'android.widget.EditText')).should(be.visible)

    with allure.step('Open "Profile" bar'):
        browser.element((AppiumBy.XPATH, '//*[@text="Профиль"]/..')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'AccountsButton_TouchableOpacity')).should(be.visible)

    with allure.step('Check "Profile" content'):
        browser.element((AppiumBy.XPATH, '//*[@text="История уведомлений"]')).should(be.visible)
        browser.element((AppiumBy.XPATH, '//*[@text="Настройки уведомлений"]')).should(be.visible)
        browser.element((AppiumBy.XPATH, '//*[@text="История заказов"]')).should(be.visible)
        browser.element((AppiumBy.XPATH, '//*[@text="История просмотров"]')).should(be.visible)
        browser.element((AppiumBy.XPATH, '//*[@text="Моя информация"]')).should(be.visible)
        browser.element((AppiumBy.XPATH, '//*[@text="Программа лояльности"]')).should(be.visible)
        browser.element((AppiumBy.XPATH, '//*[@text="Акции"]')).should(be.visible)
