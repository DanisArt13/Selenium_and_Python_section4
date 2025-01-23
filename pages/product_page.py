""" product_page """
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ButtonLocators
import time

class PageObject(BasePage):
    
    def click_add_product(self):
        link = self.browser.find_element(*ButtonLocators.BUTTON_LINK)
        link.click()
        self.solve_quiz_and_get_code()