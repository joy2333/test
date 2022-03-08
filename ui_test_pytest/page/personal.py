from selenium.webdriver.common.by import By
from base.base_page import BasePage


class AddressPage(BasePage):
    personal_center = (By.XPATH, '//*[contains(text(),"个人中心")]')
    my_address = (By.XPATH, '//*[contains(text(),"我的地址")]/i')
    add_address = (By.CSS_SELECTOR, '[data-popup-title="新增地址"]')
    iframe = (By.XPATH, '/html/body/div[9]/div/div[2]/iframe')
    alias = (By.CSS_SELECTOR, '[name="alias"]')
    name = (By.CSS_SELECTOR, '[name="name"]')
    tel = (By.CSS_SELECTOR, '[name="tel"]')
    province = (By.XPATH, '/html/body/div[1]/form/div[4]/div[1]')
    province_ = (By.XPATH, '/html/body/div[1]/form/div[4]/div[1]/div/ul/li[2]')
    city = (By.XPATH, '//a[@tabindex="-1"]/span[contains(text(),"城市")]')
    city_ = (By.XPATH, '/html/body/div[1]/form/div[4]/div[2]/div/ul/li[2]')
    county = (By.XPATH, '//a[@tabindex="-1"]/span[contains(text(),"区/县")]')
    county_ = (By.XPATH, '/html/body/div[1]/form/div[4]/div[3]/div/ul/li[2]')
    address = (By.CSS_SELECTOR, '[name="address"]')
    save = (By.XPATH, '/html/body/div[1]/form/div[7]/button')
    delete = (By.XPATH, '/html/body/div[4]/div[3]/div/ul/li[1]/div[2]/a[3]')
    determine = (By.XPATH, '/html/body/div[9]/div/div[3]/span[2]')
    brand = (By.XPATH, '//p[@class="prompt-msg"]')

    def test_update_address(self, alias, name, tel, address, expect):
        self.click(self.personal_center)
        self.click(self.my_address)
        self.click(self.add_address)
        self.wait(1)
        self.close_popup()
        self.switch_frame(self.iframe)
        self.input(self.alias, alias)
        self.input(self.name, name)
        self.input(self.tel, tel)
        self.click(self.province)
        self.click(self.province_)
        self.click(self.city)
        self.click(self.city_)
        self.click(self.county)
        self.click(self.county_)
        self.input(self.address, address)
        self.click(self.save)
        self.switch_default()
        self.wait(2)
        self.click_(self.delete)
        self.click(self.determine)
        self.assert_element(self.brand, expect)