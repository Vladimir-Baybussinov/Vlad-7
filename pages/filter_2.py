import webbrowser
from time import sleep

from pages.base import BasePage
from selenium.webdriver.common.by import By

plus_ingredients = (By.XPATH, "//div[@class='emotion-182j3cv'][1]")
minus_ingredients = (By.XPATH, "//div[@class='emotion-182j3cv'][2]")


class FiltersPage2(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.minus_ingredients = None
        self.plus_ingredients = None

    def open(self):
        self.browser.get('https://eda.ru')
        self.browser.refresh()

    def open_search(self):
        self.find((By.XPATH, "//span[text()='Ингредиенты, детали']")).click()
        sleep(2)

    def find_plus(self):
        self.plus_ingredients = self.find(plus_ingredients)

    def plus(self):
        self.plus_ingredients.click()

    def send1(self):
        self.plus_ingredients.send_keys('Куриное филе')

    def find_minus(self):
        self.minus_ingredients = self.find(minus_ingredients)

    def minus(self):
        self.minus_ingredients.click()

    def send2(self):
        self.plus_ingredients.send_keys('Огурец')
