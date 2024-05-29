from time import sleep

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class FiltersPage1(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://eda.ru')

    def cat(self):
        self.find((By.XPATH, "//div[@class='emotion-1jy0sh8']")).click()

        self.find((By.XPATH, "//button[contains(text(), 'Основные блюда')]")).click()

    def blu(self):
        self.find((By.XPATH, "//div[@class='emotion-1pba6yl']")).click()

        self.find((By.XPATH, "//button[contains(text(), 'Котлеты')]")).click()

    def kitchen(self):
        self.find((By.XPATH, "//div[@class='emotion-1nwm3v3']")).click()

        self.find((By.XPATH, "//button[contains(text(), 'Русская кухня')]")).click()

    def menu(self):
        self.find((By.XPATH, "//div[@class='emotion-1yrtqfb']")).click()

        self.find((By.XPATH, "//button[contains(text(), 'Детское меню')]")).click()

    def search(self):
        self.find((By.XPATH, "//button[@class='emotion-1842bel']")).click()

    def back(self):  # Возвращаемся на предыдущую страницу
        self.browser.back()
        sleep(0.5)