from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:
    chrome.get("http://the-internet.herokuapp.com/login")
    firefox.get("http://the-internet.herokuapp.com/login")

    ch_input_name = chrome.find_element(By.ID, "username"). send_keys("tomsmith")
    ff_input_name = firefox.find_element(By.ID, "username"). send_keys("tomsmith")
    sleep(1)

    ch_input_pass = chrome.find_element(By.ID, "password"). send_keys("SuperSecretPassword!")
    ff_input_pass = firefox.find_element(By.ID, "password"). send_keys("SuperSecretPassword!")
    sleep(1)

    chrome.find_element(By.TAG_NAME, "button").click()
    firefox.find_element(By.TAG_NAME, "button").click()
    sleep(1)

except Exception as ex:
    print(ex)
finally:
    chrome.quit()
    firefox.quit()