from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "form div label #input_value")
    x = x_element.text
    y = calc(x)
    input_answer = browser.find_element(By.CSS_SELECTOR, "form div.form-group input#answer")   
    input_answer.send_keys(y)
    checkbox1 = browser.find_element(By.CSS_SELECTOR, "form div.form-check input[type='checkbox']:required")
    checkbox1.click()
    radiobutton1 = browser.find_element(By.CSS_SELECTOR, "form div.form-check.form-radio-custom input[type='radio']#robotsRule") 
    radiobutton1.click()
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()