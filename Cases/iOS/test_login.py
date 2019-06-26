from PO.iOS.LoginPage import LoginPage
from Public.actions import ElementAction
from .conftest import driver


class TestLogin:

    def setup(self):
        self.driver = driver()
        self.Action = ElementAction(self.driver)
        self.login_page = LoginPage(self.driver)

    def test_login(self):
        self.Action.click(self.login_page.input_account)

    def test_login2(self):
        self.Action.click(self.login_page.input_account)
