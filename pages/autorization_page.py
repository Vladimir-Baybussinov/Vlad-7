from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

btn1=(By.XPATH, "//button[@class='emotion-fjxovz']")
btn2=(By.XPATH,"//button[@class='rui-Button-button rui-Button-type-primary rui-Button-size-medium rui-Button-iconPosition-left rui-Button-block']")
login = (By.ID, "login")
password = (By.ID, "password")


class AutorizationPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self): ###test-case-1
        return self.browser.get('http://eda.ru')

    def sing_in_find(self): ###test-case-2
        return self.find(btn1).click()
        sleep(5)

    def sing_in_click(self):
        return self.sing_in_find().click()

    def post_find(self):
        return self.find(login)
    def post_click(self):
        return self.post_find().click()

    def post_write(self):
        self.find(login).click()
        return self.post_find().send_keys('vova_220403@mail.ru')

    def pas_find(self):
        return self.find(password).click()


    def pas_click(self):
        return self.pas_find().click()

    def pas_write(self):
        return self.find(password).send_keys('Vendetta220403')

    def log_find(self):
        return self.find(btn2)

    def log_click(self):
        return self.log_find().click()

