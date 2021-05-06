from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome("/home/user/chromedriver_linux64/chromedriver")
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    label1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    label1.click()
    label2 = browser.find_element_by_css_selector("[for='robotsRule']")
    label2.click()
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
