from appium import webdriver
from config import Env
from Public.actions import ElementAction


def init_action():
    driver = webdriver.Remote(Env.appium_url, Env.android_desc)
    action = ElementAction(driver)
    return action
