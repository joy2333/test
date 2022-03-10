from selenium.webdriver.common.by import By
from base.base_page import BasePage


class SearchPage(BasePage):
    search_input = (By.NAME, 'wd')
    search_button = (By.ID, 'ai-topsearch')
    shop_button = (By.CSS_SELECTOR, '[class="am-animation-scale-up"]')
    set_meal = (By.CSS_SELECTOR, '[data-value="套餐一"]')
    color = (By.CSS_SELECTOR, '[data-value="金色"]')
    capacity = (By.CSS_SELECTOR, '[data-value="128G"]')
    immediately_buy = (By.CSS_SELECTOR, '[title="点此按钮到下一步确认购买信息"]')
    cash_payment = (By.XPATH, '//*[contains(text(),"现金支付")]')
    submit_order = (By.CSS_SELECTOR, '[title="点击此按钮，提交订单"]')
    brand = (By.XPATH, '/html/body/div[11]/div/p')

    def search(self, name, expect):
        self.wait(1)
        self.input(self.search_input, name)
        self.click(self.search_button)
        self.assert_element(self.brand, expect)

    def shopping(self, name, expect):
        self.wait(1)
        self.input(self.search_input, name)
        self.click(self.search_button)
        self.click(self.shop_button)
        self.switch_handle()
        self.click(self.set_meal)
        self.wait(1)
        self.click_move(self.color, 5, 5)
        self.click_move(self.capacity, 5, 5)
        self.click(self.immediately_buy)
        self.close_popup()
        self.click(self.cash_payment)
        self.close_popup()
        self.click(self.submit_order)
        self.assert_element(self.brand, expect)
