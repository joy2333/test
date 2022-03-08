import logging
import allure
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from base.project_path import screenshot_path
from selenium.webdriver.support.select import Select


def open_driver(type_):  # 入参为浏览器的名称：谷歌Chrome
    try:
        driver = getattr(webdriver, type_)()
    except Exception as e:
        print(e)
        driver = webdriver.Chrome()
    return driver


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # 访问URL
    def open(self, url):
        logging.info('正在打开URL:{}'.format(url))
        self.driver.get(url)

    # 用显示等待查找元素,返回元素
    def locator(self, loc, display):
        if display:
            try:
                logging.info('元素{}显示等待10秒'.format(loc))
                return WebDriverWait(self.driver, 10, 0.5).until(lambda el: self.driver.find_element(*loc),
                                                                 message='TimeoutException')
            except Exception as e:
                logging.info('找不到元素，异常原因：{}'.format(e))
                raise
        else:
            try:
                element = self.driver.find_element(*loc)
                return element
            except Exception as e:
                logging.info('找不到元素，异常原因：{}'.format(e))
                raise

                # 输入

    def input(self, loc, txt, display=False):
        element = self.locator(loc, display)

        try:
            element.clear()
            logging.info('清除文本框{}中已有的内容'.format(loc))
        except Exception as e:
            logging.info('清除文本框中已有的内容失败，异常原因：{}'.format(e))
            raise
        try:
            element.send_keys(txt)
            logging.info('在元素:{}中输入:{}'.format(loc, txt))
        except Exception as e:
            logging.info('在元素中输入内容失败，异常原因：:{}'.format(e))
            raise

    # 点击
    def click(self, loc, display=False):
        try:
            logging.info('点击元素:{}'.format(loc))
            self.locator(loc, display).click()
        except Exception as e:
            logging.info('点击元素失败，异常原因为:{}'.format(e))
            raise

    # js点击
    def click_(self, loc, display=False):
        try:
            logging.info('js方式点击元素:{}'.format(loc))
            self.driver.execute_script("arguments[0].click();", self.locator(loc, display))
        except Exception as e:
            logging.info('js方式点击元素失败，异常原因为:{}'.format(e))
            raise

    # 等待
    @staticmethod
    def wait(time_):
        logging.info('等待:{}秒钟'.format(str(time_)))
        time.sleep(int(time_))

    # 切换Iframe
    def switch_frame(self, loc, display=False):
        if type(loc) is tuple:
            logging.info('切换Iframe：{}'.format(loc))
            self.driver.switch_to.frame(self.locator(loc, display))
        else:
            logging.info('切换Iframe：{}'.format(loc))
            self.driver.switch_to.frame(loc)

    # 切换default窗体（返回到最外层）
    def switch_default(self):
        logging.info('切换default窗体')
        self.driver.switch_to.default_content()

    # 切换句柄,是否关闭当前窗体，切换到哪个窗体
    def switch_handle(self, close=False, index=1):
        handles = self.driver.window_handles
        if close:
            logging.info('关闭当前窗体')
            self.driver.close()
        logging.info('切换到第{}个窗体'.format(index))
        self.driver.switch_to.window(handles[index])

    # 断言具体元素的文本
    def assert_element(self, loc, expect, display=False):
        try:
            reality = self.locator(loc, display).text
            logging.info('正在断言，预期结果:{}，实际结果:{}'.format(expect, reality))
            assert expect == reality, '断言失败，预期结果:{}，实际结果为:{}'.format(expect, reality)
        except Exception as e:
            logging.info('断言失败，失败原因：{}'.format(e))
            self.save_image_to_allure()
            raise

    # 断言元素的文本
    def assert_text(self, expect, display=False):
        loc = ('xpath', "//*[contains(text(),'{}')]".format(expect))
        self.assert_element(loc, expect, display)

    def save_scree_image(self):
        """
        对当前页面进行截图
        :return:
        """
        start_time = time.time()
        filename = '/{}.png'.format(start_time)
        file_path = screenshot_path + filename
        self.driver.save_screenshot(file_path)
        logging.info("错误页面截图成功，图表保存的路径:{}".format(file_path))
        return file_path

    def save_image_to_allure(self):
        """
        保存失败的截图到allure报告中
        :return:
        """
        file_path = self.save_scree_image()
        with open(file_path, "rb") as f:
            file = f.read()
            allure.attach(file, "失败截图", allure.attachment_type.PNG)

    def close_popup(self):
        logging.info("关闭弹出框")
        self.driver.switch_to.alert.accept()

    def scroll_to(self, y, x=0):
        js_str = "window.scrollTo({},{})".format(x, y)
        self.driver.execute_script(js_str)

    def select_text(self, loc, text, display=False):
        try:
            Select(self.locator(loc, display)).select_by_visible_text(text)
        except Exception as e:
            logging.info('下拉选择框出现异常，异常原因为：{}'.format(e))
            raise
