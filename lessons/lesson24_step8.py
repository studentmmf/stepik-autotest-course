from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math





def calc(x):
    return math.log1p(math.fabs(12*math.sin(x))-1)

try:

    browser = webdriver.Chrome("/home/user/chromedriver_linux64/chromedriver")

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    wait = WebDriverWait(browser, 15)
    wait.until(EC.text_to_be_present_in_element((By.ID,'price'), '$100'))
    button = browser.find_element_by_id('book')
    button.click()
    x = int(browser.find_element_by_id("input_value").text)
    y = str(calc(x))
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    button = browser.find_element_by_id("solve")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()





