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
    ch_close_button = ch_wait.until(EC.element_to_be_clickable(
        By.CSS_SELECTOR, ".modal-footer"))
    ff_close_button = ff_wait.until(EC.element_to_be_clickable(
        By.CSS_SELECTOR, ".modal-footer"))
    time.sleep(5)

    ch_close_button.click()
    ff_close_button.click()
    time.sleep(3)

except Exception as ex:
    print(ex)
finally:
    chrome.quit()
    firefox.quit()