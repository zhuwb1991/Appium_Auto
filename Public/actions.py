import time
import os
from .page import BasePage
from appium.common.exceptions import NoSuchContextException
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class ElementAction(BasePage):
    """元素操作"""
    def click(self, loc, index=-1):
        """
        点击操作
        :param loc:
        :param index: 一组元素时的index值
        :return:
        """
        if index != -1:
            self.find_element(loc)[index].click()
        else:
            self.find_elements(loc).click()

    def send_keys(self, loc, value, index=-1):
        """
        输入操作
        :param loc:
        :param value:
        :param index: 一组元素时的index值
        :return:
        """
        if index != -1:
            self.find_elements(loc)[index].clear()
            self.find_elements(loc)[index].send_keys(value)
        else:
            self.find_element(loc).clear()
            self.find_element(loc).send_keys(value)

    def press_keycode(self, code):
        """
        模拟点击系统按键
        :param code:
        :return:
        """
        self.driver.press_keycode(code)

    def get_screen_size(self):
        """
        获取屏幕尺寸
        :return:
        """
        x = self.get_window_size()['width']
        y = self.get_window_size()['height']
        return (x, y)

    def swipe_left(self):
        """
        左滑屏幕
        :return:
        """
        size = self.get_screen_size()
        y1 = int(size[1] * 0.5)
        x1 = int(size[0] * 0.75)
        x2 = int(size[0] * 0.05)
        self.swipe(x1, y1, x2, y1, 600)
        time.sleep(1)

    def swipe_up(self):
        """
        上滑屏幕
        :return:
        """
        size = self.get_screen_size()
        self.driver.swipe(size[0]/2, size[1]*3/4, size[0]/2, size[1]/4)
        time.sleep(1)

    def swipe_down(self):
        """
        下拉屏幕
        :return:
        """
        size = self.get_screen_size()
        self.driver.swipe(size[0]/2, size[1]/4, size[0]/2, size[1]*3/4)
        time.sleep(1)

    def switch_webview(self):
        try:
            n = 1
            while n < 10:
                time.sleep(3)
                n = n + 1
                print(self.driver.contexts)
                for cons in self.driver.contexts:
                    if cons.lower().startswith("webview"):
                        self.driver.switch_to.context(cons)
                        self.driver.execute_script('document.querySelectorAll("html")[0].style.display="block"')
                        self.driver.execute_script('document.querySelectorAll("head")[0].style.display="block"')
                        self.driver.execute_script('document.querySelectorAll("title")[0].style.display="block"')
                        return {"result": True}
            return {"result": False}
        except NoSuchContextException:
            # log.error("切换webview失败")
            pass

    def switch_native(self):
        self.driver.switch_to.context("NATIVE_APP")

    def swipe_to_show(self, element):
        """
        判断元素是否在当前页面，无则滑动屏幕查找
        :param element: 传入元素的id或text属性
        :return:
        """
        for i in range(5):
            if element not in self.driver.page_source:
                size = self.get_screen_size()
                self.driver.swipe(size[0]/2, size[1]/2, size[0]/2, size[1]/4)
            break

    def get_activity(self):
        """
        获取当前页面activity
        :return:
        """
        return self.driver.current_activity

    def get_value(self, loc, index=-1):
        """
        获取元素的值
        :param loc:
        :param index:
        :return:
        """
        if index != -1:
            value = self.find_elements(loc)[index].get_attribute("text")
        else:
            value = self.find_element(loc).get_attribute("text")
        return value

    def long_press(self, loc, duration=1800, index=-1):
        """
        :param loc:
        :param duration: 持续时间
        :param index: 多个元素时的index
        :return:
        """
        if index != -1:
            self.__touch_action().long_press(self.find_elements(loc)[index], duration=duration).release().perform()
            return {"result": True}
        else:
            self.__touch_action().long_press(self.find_element(loc), duration=duration).release().perform()

    @staticmethod
    def adb_tap(x='50', y='250'):
        """
        adb命令点击屏幕
        :return:
        """
        cmd = "adb shell input tap " + x + " " + y
        print(cmd)
        os.system(cmd)

    def __touch_action(self):
        return TouchAction(self.driver)

    def get_toast(self, text, timeout=5, poll_frequency=0.01):
        """
        描述：获取Toast的文本信息
        参数：text需要检查的提示信息  time检查总时间  poll_frequency检查时间间隔
        返回值：返回与之匹配到的toast信息
        异常描述：none
        """
        try:
            toast_element = (By.XPATH, "//*[contains(@text, " + "'" + text + "'" + ")]")
            toast = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.presence_of_element_located(toast_element))
            return toast.text
        except TimeoutException:
            pass

    def is_exist(self, loc):
        """
        判断元素是否存在
        :param loc:
        :return:
        """
        try:
            self.find_element(loc)
            return True
        except NoSuchElementException:
            return False

    def screen_shot(self, text=''):
        """
        截图方法
        :return:
        """
        now = time.strftime("%y%m%d%H%M%S")
        PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p)
        )
        shot_path = PATH('../report/screenshoot')
        if not os.path.exists(shot_path):
            os.makedirs(shot_path)
        self.driver.get_screenshot_as_file(shot_path + "/" + text + now + '.png')

    def permission_btn(self):
        """
        处理权限弹窗
        """
        button1 = "com.android.packageinstaller:id/permission_allow_button"
        button2 = ""
        button3 = ""
        button4 = ""
        list_btn = [button1, button2, button3, button4]
        for btn in list_btn:
            if btn in self.driver.page_source:
                try:
                    self.driver.find_element_by_id(btn).click()
                    break
                except:
                    pass

    def click_alert(self, is_accept=True):
        """
        处理iOS弹窗
        :param is_accept:
        :return:
        """
        action = 'accept' if is_accept is True else 'dismiss'
        try:
            self.driver.execute_script("mobile: alert", {"action": action})
        except RuntimeError:
            print('no alert')

    def close_app(self):
        self.driver.close_app()
