from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window() #растягиваем окно


driver.get("https://testing-cm2fe.review.chefmarket.ru/")


elem1 = driver.find_element_by_link_text('Войти') #нашли кнопку "Войти"
elem1.click()#нажали

elem2 = driver.find_element_by_id('129')#нашли поле для номера телефона
elem2.send_keys('79999999998')#ввели номер

time.sleep(5)#ждем 5 секунд

elem3 = driver.find_element_by_xpath('//*[@id="modalDescription"]/div/form/div[2]/div[1]/div[2]/div/button')#находим кнопку "Получить код"
elem3.click()

time.sleep(5)

elem4 = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/section/div/form/div[2]/div[1]/input')#во втором окне вводим код из смс
elem4.send_keys('1234')

elem5 = driver.find_element_by_xpath('//*[@id="modalDescription"]/div/form/div[2]/div[1]/div[2]/div/button')
elem5.click()#жмем "Подтвердить"

time.sleep(5)

driver.quit() #закрываем браузер
