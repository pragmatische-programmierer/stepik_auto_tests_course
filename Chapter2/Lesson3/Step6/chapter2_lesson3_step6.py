from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.XPATH, "//button[text()='I want to go on a magical journey!']")
    button.click()
    first_window = browser.window_handles[0]
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

    x_element = browser.find_element(By.CSS_SELECTOR, "form div label #input_value")
    x = x_element.text
    y = calc(x)
    input_answer = browser.find_element(By.CSS_SELECTOR, "form div.form-group input#answer")   
    input_answer.send_keys(y)
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()