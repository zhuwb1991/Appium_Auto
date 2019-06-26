from PO.iOS.LoginPage import LoginPage
from Public.actions import ElementAction
from .conftest import init_driver


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.Action = ElementAction(self.driver)
        self.login_page = LoginPage(self.driver)

    def test_login(self):
        """登录1"""
        self.Action.click(self.login_page.input_account)

    def test_login2(self):
        self.Action.click(self.login_page.input_account)
