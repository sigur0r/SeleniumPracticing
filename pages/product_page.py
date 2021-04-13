from . import base_page
from .base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.adding_item_to_checkout()
        #self.right_item_added()
        #self.according_price()

    def adding_item_to_checkout(self):
        link = self.browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        link.click()


    def right_item_added(self):
        #item_name = self.browser.find_element(By.CLASS_NAME, "product_main").text  нужно разобраться как реализовать этот способ нормально
        page_item_name = "The shellcoder's handbook был добавлен в вашу корзину."
        checkout_item_name = self.browser.find_element(By.CLASS_NAME, "alertinner ").text # проверка что в корзину добавлен правильный товар
        assert page_item_name == checkout_item_name

    def according_price(self):
        #item_price = self.browser.find_element(By.CLASS_NAME, "col-sm-2") # проверка что в корзину добавлен правильный товар
        product_price = "Стоимость корзины теперь составляет 9,99 £"
        checkout_price = self.browser.find_element(By.CSS_SELECTOR, "div.alert p")
        assert checkout_price == product_price
