from selenium import webdriver

chrome = webdriver.Chrome()

try:
    chrome.get("http://uitestingplayground.com/textinput")
    chrome.find_element("id", "newButtonName").send_keys("SkyPro")
    chrome.find_element("id", "updatingButton").click()
    print(chrome.find_element("id", "updatingButton").text)

except Exception as ex:
    print(ex)
finally:
    chrome.quit()