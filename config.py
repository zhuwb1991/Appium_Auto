

class Env:

    appium_url = 'http://localhost:4723/wd/hub'

    android_desc = {
        'automationName': 'UiAutomator2',
        'platformName': 'Android',
        'platformVersion': '7.0',
        'deviceName': 'Android device',
        'udid': 'emulator-5554',
        'appPackage': '',
        'appActivity': '',
        'noReset': True
    }

    ios_desc = {
        'automationName': 'XCUITest',
        'platformName': 'iOS',
        'platformVersion': '12.2',
        'deviceName': 'iPhone',
        'udid': 'xxxx',
        'newCommandTimeout': '3600',
        'bundleId': ''
    }
