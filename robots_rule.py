from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.TAG_NAME, "img")
    elem = x_element.get_attribute("valuex")
    y = calc(elem)

    input0 = browser.find_element(By.ID, "answer")
    input0.send_keys(y)

    check = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
    check.click()

    radioo = browser.find_element(By.ID, "robotsRule")
    radioo.click()

    butt = browser.find_element(By.TAG_NAME, "button")
    butt.click()

finally:
    time.sleep(10)
    browser.quit()


    
    

    
