from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


chrome = webdriver.Chrome()
wait = WebDriverWait(chrome, 20, 0.1)

try:
    chrome.get("http://uitestingplayground.com/ajax")
    
    chrome.find_element(By.CSS_SELECTOR, "#ajaxButton"). click()
    
    print(wait.until (EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".bg-success"))).text)

except Exception as ex:
    print(ex)
finally:
    chrome.quit()