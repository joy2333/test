import yaml
import logging
from selenium import webdriver
from base.project_path import root_path


def load_yaml(filename):
    """读取yaml文件，返回json数据"""
    # 打开文件：文件路径，可读，编码
    files = open(filename, 'r', encoding='utf-8')
    # 读取文件：加第二个参数更加安全
    data = yaml.load(files, Loader=yaml.FullLoader)
    return data


def get_driver():
    """获取浏览器驱动对象"""
    logging.info('启动Chrome浏览器')
    driver = webdriver.Chrome()
    logging.info('窗口最大化')
    driver.maximize_window()
    logging.info('设置隐性等待15秒')
    driver.implicitly_wait(15)
    return driver


def close_driver(driver):
    """关闭浏览器驱动对象"""
    logging.info('关闭Chrome浏览器')
    driver.quit()


if __name__ == '__main__':
    print(load_yaml(root_path + '/data/login_success.yaml')[0])
