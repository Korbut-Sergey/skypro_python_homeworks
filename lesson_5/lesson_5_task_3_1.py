from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:
    chrome.get("https://the-internet.herokuapp.com/add_remove_elements/")
    firefox.get("https://the-internet.herokuapp.com/add_remove_elements/")
    
    for C in range(5):
        chrome.find_element(
            By.XPATH, '//button[text()="Add Element]').click()
        firefox.find_element(
            By.XPATH, '//button[text()="Add Element]').click()
    sleep(3)

    chrome_delete_buttons = chrome.find_elements(
        "xpath", '//button[text()="Delete"]')
    firefox_delete_buttons = firefox.find_elements(
        "xpath", '//button[text()="Delete"]')
    print(
        f"Количество кнопок Delete в Chrome: {len(chrome_delete_buttons)}")
    print(
        f"Количество кнопок Delete в Firefox: {len(firefox_delete_buttons)}")

except Exception as ex:
    print(ex)
finally:
    chrome.quit()
    firefox.quit()