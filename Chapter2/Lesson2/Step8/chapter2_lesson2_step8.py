from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
import os

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element(By.CSS_SELECTOR, "input.form-control[name='firstname']")
    first_name.send_keys("John")
    last_name = browser.find_element(By.CSS_SELECTOR, "input.form-control[name='lastname']")
    last_name.send_keys("Doe")
    email_address = browser.find_element(By.CSS_SELECTOR, "input.form-control[name='email']")
    email_address.send_keys("john.doe@my.name")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file_to_test_load.txt')

    file_input = browser.find_element(By.CSS_SELECTOR, "input[name='file']")
    file_input.send_keys(file_path)

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()