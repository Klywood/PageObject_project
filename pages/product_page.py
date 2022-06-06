from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.add_to_basket_button)
        add_button.click()

    def product_name_should_match_the_message(self):
        actual_name = self.browser.find_element(*ProductPageLocators.product_name).text
        print(actual_name)
        name_in_message = self.browser.find_element(*ProductPageLocators.name_in_message).text
        print(name_in_message)
        assert actual_name == name_in_message

    def product_price_should_match_the_message(self):
        actual_price = self.browser.find_element(*ProductPageLocators.product_price).text
        price_in_message = self.browser.find_element(*ProductPageLocators.price_in_message).text
        assert actual_price == price_in_message

