""" product_page """
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ButtonLocators, BasketPageLocators, ProductPageLocators

import time
import pytest

class PageObject(BasePage):
    
    def click_add_product(self):
        link = self.browser.find_element(*ButtonLocators.BUTTON_LINK)
        link.click()
        self.solve_quiz_and_get_code()
        
    @pytest.mark.xfail    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"
           
