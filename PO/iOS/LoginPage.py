from appium.webdriver.common.mobileby import MobileBy
from Public.actions import ElementAction


class LoginPage(ElementAction):

    skip_btn = (MobileBy.ACCESSIBILITY_ID, "跳过")
    input_account = (MobileBy.CLASS_NAME, "XCUIElementTypeTextField")

    def login(self):
        pass
