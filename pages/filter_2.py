import webbrowser
from time import sleep

from pages.base import BasePage
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

plus_ingredients = (By.XPATH, "//div[@class='emotion-1wxt7g0']" and "//button[contains(text(), 'Куриное филе')]")


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
        self.browser.implicitly_wait(10)

    def plus(self):
        self.plus_ingredients.click()
        self.browser.implicitly_wait(10)

    #def type(self):
        #self.find((By.XPATH, "//div[@class='emotion-16rmb3']" "//contains[text(), 'Проверено «Едой»']")).click()

    #def type2(self):
       # self.find((By.XPATH, "//div[@class='emotion-16rmb3']" and "//contains[text(), 'Пошаговые рецепты']")).click()

    def search(self):
        self.find((By.XPATH, "//button[@class='emotion-sjbikb']")).click()




