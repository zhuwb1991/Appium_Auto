from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, WebDriverException


class BasePage:
    """PO模式页面基类"""
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc, timeout=30):
        """
        查找单个元素
        :param loc: 元素tuple  (MobileBy.ID, '...')
        :param timeout: 超时时间
        :return:
        """
        try:
            WebDriverWait(self.driver, timeout, poll_frequency=2).until(lambda dr: dr.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except TimeoutException:
            print("元素 {} 定位超时".format(loc))
        except WebDriverException:
            print("driver出问题了")

    def find_elements(self, loc, timeout=30):
        """
        查找一组元素
        :param loc:
        :param timeout:
        :return:
        """
        try:
            WebDriverWait(self.driver, timeout, poll_frequency=2).until(lambda dr: dr.find_elements(*loc))
            return self.driver.find_elements(*loc)
        except TimeoutException:
            print("元素 {} 定位超时".format(loc))
        except WebDriverException:
            print("driver出问题了")

    def get_window_size(self):
        return self.driver.get_window_size()

    def swipe(self, start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)
