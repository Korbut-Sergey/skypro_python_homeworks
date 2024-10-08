from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:
    chrome.get("http://the-internet.herokuapp.com/inputs")
    firefox.get("http://the-internet.herokuapp.com/inputs")

    chrome_input_field = chrome.find_element(By.TAG_NAME, "input")
    firefox_input_field = firefox.find_element(By.TAG_NAME, "input")
    chrome_input_field.send_keys("1000")
    firefox_input_field.send_keys("1000")
    sleep(1)
    chrome_input_field.clear()
    firefox_input_field.clear()
    sleep(1)
    chrome_input_field.send_keys("999")
    firefox_input_field.send_keys("999")
    sleep(1)

except Exception as ex:
    print(ex)
finally:
    chrome.quit()
    firefox.quit()