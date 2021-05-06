from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    def authorization(self, url, number, code):

        driver = self.driver
        driver.get(url)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Войти"))).click() #нашли кнопку "Войти"

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"129"))).send_keys(number)#ввели номер

        #нажимаем кнопку "Получить код"
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="modalDescription"]/div/form/div[2]/div[1]/div[2]/div/button'))).click()

        #во втором окне вводим код из смс
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="134"]'))).send_keys(code)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="modalDescription"]/div/form/div[2]/div[1]/div[2]/div/button'))).click()

class OrdersPage(BasePage):

    def checkStringPresence(self, str):

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div/div[1]/div[10]")))

        assert str in self.driver.page_source #проверяем наличие строки на странице

