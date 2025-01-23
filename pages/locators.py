""" locators """

from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class ButtonLocators():
    BUTTON_LINK = (By.CSS_SELECTOR, "button.btn-add-to-basket")