import pytest
import allure
from appium import webdriver
from config import Env


def init_driver():
    """
    初始化driver, 在每个用例的setup()中创建实例
    :return:
    """
    return webdriver.Remote(Env.appium_url, Env.ios_desc)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    driver = init_driver()
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        f = driver.get_screenshot_as_png()
        allure.attach(f, '失败截图', allure.attachment_type.PNG)
