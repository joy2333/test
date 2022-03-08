from selenium.webdriver.common.by import By
from base.base_page import BasePage


class SearchPage(BasePage):
    search_input = (By.NAME, 'wd')
    search_button = (By.ID, 'ai-topsearch')
    shop_button = (By.CSS_SELECTOR, '[class="am-animation-scale-up"]')
    set_meal = (By.CSS_SELECTOR, '[data-value="套餐一"]')
    color = (By.XPATH, '//*[@data-value="金色"]/img')
    capacity = (By.CSS_SELECTOR, '[data-value="128G"]')
    immediately_buy = (By.CSS_SELECTOR, '[title="点此按钮到下一步确认购买信息"]')
    cash_payment = (By.XPATH, '//*[contains(text(),"现金支付")]')
    submit_order = (By.CSS_SELECTOR, '[title="点击此按钮，提交订单"]')
    brand = (By.XPATH, '//*[@class="map-more-submit"]/span')

    def search(self, name, expect):
        self.wait(1)
        self.input(self.search_input, name)
        self.click(self.search_button)
        self.assert_element(self.brand, expect)
