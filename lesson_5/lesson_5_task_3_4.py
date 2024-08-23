import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:
    chrome.get("http://the-internet.herokuapp.com/entry_ad")
    firefox.get("http://the-internet.herokuapp.com/entry_ad")

    ch_wait = WebDriverWait(chrome, 10)
    ff_wait = WebDriverWait(firefox, 10)
    ch_wait.until(EC.element_to_be_clickable(
        chrome.find_element(By.CSS_SELECTOR, '.modal-footer'))).click()
    ff_wait.until(EC.element_to_be_clickable(
        firefox.find_element(By.CSS_SELECTOR, '.modal-footer'))).click()

except Exception as ex:
    print(ex)
finally:
    chrome.quit()
    firefox.quit()