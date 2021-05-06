
from selenium import webdriver
import time


import math

def calc(x):
    return math.log1p(math.fabs(12*math.sin(x))-1)


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome("/home/user/chromedriver_linux64/chromedriver")
    browser.get(link)
    time.sleep(5)
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = int(browser.find_element_by_id("input_value").text)
    y = str(calc(x))
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(40)
    # закрываем браузер после всех манипуляций
    browser.quit()
