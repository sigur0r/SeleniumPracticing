from . import base_page
from .base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.adding_item_to_checkout()
        self.right_item_added()
        self.according_price()

    def adding_item_to_checkout(self):
        link = self.browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        link.click()


    def right_item_added(self):
        # проверка что в корзину добавлен правильный товар
        assert True

    def according_price(self):
        # проверка что цена в корзине соответствующая
        assert True
