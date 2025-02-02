""" test_product_page """
from .pages.product_page import PageObject
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

import pytest
import time

links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
          # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
          # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
          # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
          # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
          # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
          # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
          # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
          # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
          # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
          ]

@pytest.mark.need_review          
@pytest.mark.parametrize('link', links) 
def test_guest_can_add_product_to_basket(browser, link):
    page = PageObject(browser, link)
    page.open()
    page.click_add_product()

@pytest.mark.parametrize('link', links)     
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = PageObject(browser, link)
    page.open()
    page.click_add_product()
    page.should_not_be_success_message()

@pytest.mark.parametrize('link', links) 
def test_guest_cant_see_success_message(browser, link): 
    page = PageObject(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.parametrize('link', links)     
def test_message_disappeared_after_adding_product_to_basket(browser, link): 
    page = PageObject(browser, link)
    page.open()
    page.click_add_product()
    page.should_not_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(browser, link)
    page.open()
    page.should_be_login_link()
    
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review    
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products_in_basket()
    basket_page.none_items_message()

@pytest.mark.login
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        self.login_page = LoginPage(browser, link)
        self.login_page.open()  
        self.email = str(time.time()) + "@fakemail.org"
        self.password = "qazwsx098" 
        
        self.login_page.go_to_login_page()
        self.login_page.register_new_user(self.email, self.password)
        self.login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = PageObject(browser, link)
        page.open()
        page.should_not_be_success_message()
        
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = PageObject(browser, link)
        page.open()
        page.click_add_product()