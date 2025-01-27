""" basket page """

from .base_page import BasePage
from .locators import BasketPageLocators

import pytest

class BasketPage(BasePage):
    
    def none_items_message(self):
        actual_message = self.browser.find_element(*BasketPageLocators.NONE_PRODUCTS_MESSAGE).text
        expected_message = "Your basket is empty"
        assert expected_message in actual_message, f'Incorrect message, must be "{expected_message}"'
        
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_LINK), "Products in the basket, but shouldn't be there"