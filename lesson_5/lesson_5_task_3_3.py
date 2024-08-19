from selenium import webdriver
from time import sleep

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:
    chrome.get("http://uitestingplayground.com/classattr")
    firefox.get("http://uitestingplayground.com/classattr")

    for C in range(3):
        blue_button = chrome.find_element(
            "xpath", "//button[contains(concat(' ' , normalize-space(@class), ' '), ' btn-primary ')]")
        blue_button.click()
        blue_button = firefox.find_element(
            "xpath", "//button[contains(concat(' ' , normalize-space(@class), ' '), ' btn-primary ')]")
        blue_button.click()
        sleep(3)
        chrome.switch_to.alert.accept()
        firefox.switch_to.alert.accept()
except Exception as ex:
    print(ex)
finally:
    chrome.quit()
    firefox.quit()