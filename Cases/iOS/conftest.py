from appium import webdriver
from config import Env


def driver():
    """
    初始化driver, 在每个用例的setup()中创建实例
    :return:
    """
    return webdriver.Remote(Env.appium_url, Env.ios_desc)
