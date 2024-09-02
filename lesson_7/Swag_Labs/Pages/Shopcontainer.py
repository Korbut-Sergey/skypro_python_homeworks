from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Shopcontainer:
    def __init__(self, browser):
        self.browser = browser

    def checkout(self):
        self.check = (By.ID, "checkout")

        self.browser.find_element(*self.check).click()

    def info(self):
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")

        self.browser.find_element(*self.first_name).send_keys("Evgen")
        self.browser.find_element(*self.last_name).send_keys("Voronov")
        self.browser.find_element(*self.postal_code).send_keys("123321")
        self.browser.find_element(*self.continue_button).click()

    def price(self):
        WebDriverWait(self.browser, 20, 0.1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".summary_total_label"))).text
        total_price = self.browser.find_element(By.CSS_SELECTOR, ".summary_total_label")
        total = total_price.text.strip().replace("Total: $", "")
        return total