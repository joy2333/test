import logging
import allure
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from base.project_path import screenshot_path
from selenium.webdriver.support.select import Select


def open_driver(type_):
    """
    param type_: 浏览器的名称：例如谷歌：Chrome
    return: 浏览器驱动对象
    """
    try:
        driver = getattr(webdriver, type_)()
    except Exception as e:
        print(e)
        driver = webdriver.Chrome()
    return driver


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        """param url: 打开网址"""
        logging.info('正在打开URL:{}'.format(url))
        self.driver.get(url)

    def locator(self, loc, display):
        """
        查找元素
        param loc: 元素的定位方式，例如：(By.ID, ’id‘)
        param display: 是否使用显示等待的方式查找元素，入参为True/False
        return: 元素对象
        """
        try:
            if display:
                logging.info('元素{}显示等待10秒'.format(loc))
                return WebDriverWait(self.driver, 10, 0.5).until(lambda el: self.driver.find_element(*loc),
                                                                 message='TimeoutException')
            else:
                return self.driver.find_element(*loc)
        except Exception as e:
            logging.info('找不到元素，异常原因：{}'.format(e))
            raise

    # 输入
    def input(self, loc, txt, display=False):
        """
        在元素中输入文本内容
        param loc: 元素的定位方式，例如：(By.ID, ’id‘)
        param txt: 输入的文本
        param display: 是否使用显示等待的方式查找元素，入参为True/False
        """
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
        """
        loc: 元素的定位方式，例如：(By.ID, ’id‘)
        display: 是否使用显示等待的方式查找元素，入参为True/False
        """
        try:
            logging.info('点击元素:{}'.format(loc))
            self.locator(loc, display).click()
        except Exception as e:
            logging.info('点击元素失败，异常原因为:{}'.format(e))
            raise

    # js点击
    def click_js(self, loc, display=False):
        """
        使用js脚本点击元素
        param loc: 元素的定位方式，例如：(By.ID, ’id‘)
        param display: 是否使用显示等待的方式查找元素，入参为True/False
        """
        try:
            logging.info('js方式点击元素:{}'.format(loc))
            self.driver.execute_script("arguments[0].click();", self.locator(loc, display))
        except Exception as e:
            logging.info('js方式点击元素失败，异常原因为:{}'.format(e))
            raise

    @staticmethod
    def wait(time_):  # 等待
        logging.info('等待:{}秒钟'.format(str(time_)))
        time.sleep(int(time_))

    def switch_frame(self, loc, display=False):
        """
        切换Iframe
        param loc: 元素的定位方式，例如：(By.ID, ’id‘)
        param display: 是否使用显示等待的方式查找元素，入参为True/False
        """
        logging.info('切换Iframe：{}'.format(loc))
        self.driver.switch_to.frame(self.locator(loc, display))

    def switch_default(self):
        """切换到最外层Iframe"""
        logging.info('切换default窗体')
        self.driver.switch_to.default_content()

    def switch_handle(self, close=False, index=1):
        """
        切换句柄/窗口
        param close: 是否关闭当前窗体 True/False
        param index: 切换到哪个窗体 int
        """
        handles = self.driver.window_handles
        if close:
            logging.info('关闭当前窗体')
            self.driver.close()
        logging.info('切换到第{}个窗体'.format(index))
        self.driver.switch_to.window(handles[index])

    def assert_element(self, loc, expect, equal=False, display=False):
        """
        断言具体元素的文本是否与预期结果一致
        param equal: 预期结果是否模糊匹配实际结果，入参为True/False
        param loc: 元素的定位方式，例如：(By.ID, ’id‘)
        param expect: 预期结果
        param display: 是否使用显示等待的方式查找元素，入参为True/False
        """
        try:
            reality = self.locator(loc, display).text
            logging.info('正在断言，预期结果:{}，实际结果:{}'.format(expect, reality))
            if equal:
                assert expect == reality, '断言失败，预期结果:{}，实际结果为:{}'.format(expect, reality)
            else:
                assert expect in reality, '断言失败，预期结果:{}，实际结果为:{}'.format(expect, reality)
        except Exception as e:
            logging.info('断言失败，失败原因：{}'.format(e))
            self.save_image_to_allure()
            raise

    def assert_text(self, expect, equal=False, display=False):
        """
        断言页面上是否存在与预期结果文本一致的元素
        param equal: 预期结果是否模糊匹配实际结果，入参为True/False
        param expect: 预期结果
        param display: 是否使用显示等待的方式查找元素，入参为True/False
        """
        loc = ('xpath', "//*[contains(text(),'{}')]".format(expect))
        self.assert_element(loc, expect, equal, display)

    def save_scree_image(self):
        """
        对当前页面进行截图
        return:截图的存放路径
        """
        # start_time = time.time()
        # filename = '/{}.png'.format(start_time)
        # file_path = screenshot_path + filename
        file_path = screenshot_path + '/error_screenshot.png'
        self.driver.save_screenshot(file_path)
        logging.info("错误页面截图成功，图表保存的路径:{}".format(file_path))
        return file_path

    def save_image_to_allure(self):
        """保存失败的截图到allure报告中"""
        file_path = self.save_scree_image()
        with open(file_path, "rb") as f:
            file = f.read()
            allure.attach(file, "失败截图", allure.attachment_type.PNG)

    def close_popup(self):
        """关闭浏览器的alert弹窗"""
        logging.info("关闭弹出框")
        self.driver.switch_to.alert.accept()

    def scroll_to(self, y, x=0):
        js_str = "window.scrollTo({},{})".format(x, y)
        self.driver.execute_script(js_str)

    def select_text(self, loc, text, display=False):
        """
        选择符合文本内容的下拉选项
        param loc: Select元素元素的定位方式，例如：(By.ID, ’id‘)
        param text: 下拉选项的文本
        param display: 是否使用显示等待的方式查找元素，入参为True/False
        """
        try:
            Select(self.locator(loc, display)).select_by_visible_text(text)
        except Exception as e:
            logging.info('下拉选择框出现异常，异常原因为：{}'.format(e))
            raise
