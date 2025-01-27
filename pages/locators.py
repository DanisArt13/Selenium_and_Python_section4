""" locators """

from selenium.webdriver.common.by import By
   
class ButtonLocators():
    BUTTON_LINK = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a.btn-default")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class BasketPageLocators():
    ITEMS_LINK = (By.CSS_SELECTOR, "div.basket-items")
    NONE_PRODUCTS_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")

class HomePageLocators():
    HOME_PAGE_LINK = (By.CSS_SELECTOR ,".col-sm-7 a")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") 
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form") 
    LOGIN_EMAIL = (By.CSS_SELECTOR, 'input[name="login-username"]')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, 'input[name="login-password"]')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, 'input[name="registration-email"]')
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, 'input[name="registration-password1"]')
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, 'input[name="registration-password2"]')
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, 'button[name="registration_submit"]')
    
class ProductPageLocators():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")
    