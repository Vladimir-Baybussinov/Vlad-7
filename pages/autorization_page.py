from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

login = (By.ID, "login")
password = (By.ID, "password")


class AutorizationPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self): #Открыть страницу
        return self.browser.get('http://eda.ru')

    def sing_in(self): #Нажать на кнопку войти
        self.find((By.XPATH, "//button[@class='emotion-fjxovz']")).click()
        sleep(5)

    def post(self): #Ввести логин
        self.find(login).click()
        return self.find(login).send_keys('vova_220403@mail.ru')

    def pas(self): #Ввести пароль
        self.find(password).click()
        return self.find(password).send_keys('Vendetta220403')

    def log(self): #Нажать  на кнопку логин
        self.find((By.XPATH,
                   "//button[@class='rui-Button-button rui-Button-type-primary rui-Button-size-medium "
                   "rui-Button-iconPosition-left rui-Button-block']")).click()
        self.browser.implicitly_wait(10)
