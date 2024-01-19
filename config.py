from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from pydantic import BaseModel
import os
import traektoria_app_tests.utils.file


class Config(BaseModel):
    context: str
    remote_url: str = os.getenv('REMOTE_URL')
    device_name: str = os.getenv('DEVICE_NAME')
    udid: str = os.getenv('UDID')
    appWaitActivity: str = os.getenv('APP_WAIT_ACTIVITY')
    app_local: str = traektoria_app_tests.utils.file.abs_path_from_project(os.getenv('APP'))
    app_bstack: str = os.getenv('APP')
    platformName: str = os.getenv('PLATFORM_NAME')
    platformVersion: str = os.getenv('PLATFORM_VERSION')
    load_dotenv(dotenv_path=traektoria_app_tests.utils.file.abs_path_from_project('.env.credentials'))
    userName: str = os.getenv('USER_NAME')
    accessKey: str = os.getenv('ACCESS_KEY')

    def to_driver_options(self, context):
        options = UiAutomator2Options()

        if context == 'emulator':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('udid', self.udid)
            options.set_capability('app', self.app_local)
            options.set_capability("autoGrantPermissions", "true")

        if context == 'bstack':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('deviceName', self.device_name)
            options.set_capability('platformName', self.platformName)
            options.set_capability('platformVersion', self.platformVersion)
            options.set_capability("autoGrantPermissions", "true")
            options.set_capability('app', self.app_bstack)
            options.set_capability(
                'bstack:options', {
                    'projectName': 'Mobile autotests',
                    'buildName': 'traektoria_app_build',
                    'sessionName': 'Traektoria shop autotest',
                    'userName': self.userName,
                    'accessKey': self.accessKey,
                },
            )

        return options


config = Config(context="emulator")
