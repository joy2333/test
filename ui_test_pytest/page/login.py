from selenium.webdriver.common.by import By
from base.base_page import BasePage


class LoginPage(BasePage):
    username = (By.NAME, 'accounts')
    password = (By.NAME, 'pwd')
    verify_code = (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/div/input')
    login_button = (By.XPATH, '//*[@method="post"]/div/*[@type="submit"]')
    brand = (By.XPATH, '//p[@class="prompt-msg"]')

    def login(self, url, username, password, verify_code, expect):
        self.open(url)
        self.input(self.username, username)
        self.input(self.password, password)
        self.input(self.verify_code, verify_code)
        self.click(self.login_button)
        self.wait(1)
        self.assert_element(self.brand, expect)
