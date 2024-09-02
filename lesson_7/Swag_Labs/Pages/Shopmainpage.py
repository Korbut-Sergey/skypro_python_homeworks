from selenium.webdriver.common.by import By
from lesson_7.constants import Shop_URL


class Shopmainpage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get(Shop_URL)

    def registration_fields (self):
        self._user_name = (By.ID, "user-name")
        self._password = (By.ID, "password")
        self._login_button = (By.ID, "login-button")

        self.browser.find_element(*self._user_name).send_keys("standart_user")
        self.browser.find_element(*self._password).send_keys("secret_sauce")
        self.browser.find_element(*self._login_button).click()

    def buy_issue(self):
        self.Sauce_Labs_Backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.Sauce_Labs_Bolt_TShirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.Sauce_Labs_Onesie = (By.ID, "add-to-cart-sauce-labs-onesie")

    def click_issue(self):
        self.browser.find_element(*self.Sauce_Labs_Backpack).click()
        self.browser.find_element(*self.Sauce_Labs_Bolt_TShirt).click()
        self.browser.find_element(*self.Sauce_Labs_Onesie).click()

    def into_container(self):
        self.Container = (By.ID, "shopping_cart_container")
        
        self.browser.find_element(*self.Container).click()