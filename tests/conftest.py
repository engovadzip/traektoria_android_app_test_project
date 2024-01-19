from appium import webdriver
from dotenv import load_dotenv
from selene import browser, support
import allure
import allure_commons
import os
import pytest
import traektoria_app_tests.utils.attach


def pytest_addoption(parser):
    parser.addoption("--context", default="emulator", help="Choose launch: emulator or browserstack.")
    parser.addoption("--search", default="carhartt", help="Enter search request.")


def pytest_configure(config):
    context = config.getoption("--context")
    env_file_path = f".env.{context}"

    if os.path.exists(env_file_path):
        load_dotenv(dotenv_path=env_file_path)
    else:
        print(f"Warning: Configuration file '{env_file_path}' not found.")


@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(scope='function', autouse=True)
def android_mobile_management(context):
    from config import config
    options = config.to_driver_options(context=context)

    with allure.step('setup app session'):
        browser.config.driver = webdriver.Remote(
            options.get_capability('remote_url'),
            options=options
        )

    browser.config.timeout = 15.0
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext)

    yield

    traektoria_app_tests.utils.attach.screenshot()

    traektoria_app_tests.utils.attach.page_source_xml()

    session_id = browser.driver.session_id

    with allure.step('tear down app session with id' + session_id):
        browser.quit()

    if context == 'bstack':
        traektoria_app_tests.utils.attach.bstack_video(session_id)


@pytest.fixture(scope='session', autouse=True)
def search(request):
    return request.config.getoption("--search")
