from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    element1 = browser.find_element(By.CSS_SELECTOR, "div.container form span#num1")
    x = element1.text
    element2 = browser.find_element(By.CSS_SELECTOR, "div.container form span#num2")
    y = element2.text
    sum_elements = int(x) + int(y) 

    browser.find_element(By.CSS_SELECTOR, "[value='" + str(sum_elements) + "']").click()    

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()