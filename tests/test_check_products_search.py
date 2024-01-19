import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be, query


def test_check_products_search(search):
    with allure.step('Verify app is launched'):
        browser.element((AppiumBy.CLASS_NAME, 'android.widget.EditText')).should(be.visible)

    with allure.step('Fill search string with search request'):
        browser.element((AppiumBy.CLASS_NAME, 'android.widget.EditText')).click()
        browser.element((AppiumBy.XPATH, '//*[@text="Популярные"]')).should(be.visible)
        browser.element((AppiumBy.CLASS_NAME, 'android.widget.EditText')).send_keys(f'{search}')
        browser.driver.press_keycode(66)

    with allure.step('Check search results'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Фильтры"]')).should(be.visible)
        results = browser.all((AppiumBy.XPATH, '//android.widget.TextView'))

        counter = 0

        for result in results:
            if 'carhartt' in result.get(query.text).lower():
                counter += 1

        assert counter >= 2, f'The request "{search}" was not found among the search results'
