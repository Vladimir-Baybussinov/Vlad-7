import webbrowser
from time import sleep

from pages.base import BasePage
from selenium.webdriver.common.by import By



plus_ingredients = (By.XPATH, "//div[@class='emotion-1wxt7g0']" and "//button[contains(text(), 'Куриное филе')]")
add_ingredients = (By.XPATH, "//input[@type='text']")
ingreditent = (By.XPATH, "//button[@class='emotion-kuminy']")

class FiltersPage2(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.minus_ingredients = None
        self.plus_ingredients = None

    def open(self):
        self.browser.get('https://eda.ru')
        self.browser.refresh()
################################################################
    def open_search(self):
        self.find((By.XPATH, "//span[text()='Ингредиенты, детали']")).click()
        sleep(2)

    def add_ingred_find(self):
        self.browser.implicitly_wait(10)
        return self.find(add_ingredients)

    def add_ingredients_click(self):
        return self.add_ingred_find().click()

    def add_ingredients_send_text(self):
        return self.add_ingred_find().send_keys('Помидоры')

    def find_ingredient_dropdown(self):
        return self.find(ingreditent)

    def choose_ingredient(self):
        return self.find_ingredient_dropdown().click()
################################################################
    def minus_ingridients_find(self):
        self.browser.implicitly_wait(10)
        return self.find(minus_ingridients_find)

    def minus(self):
        self.minus_ingredients.click()
        self.browser.implicitly_wait(10)



################################################################
    def find_plus(self):
        self.plus_ingredients = self.find(plus_ingredients)
        self.browser.implicitly_wait(10)

    def plus(self):
        self.plus_ingredients.click()
        self.browser.implicitly_wait(10)

    def type(self):
        sleep(5)
        self.find((By.XPATH, "//div[@class='emotion-16rmb3']")).click()
        sleep(2)

    def search(self):
        self.find((By.XPATH, "//button[@class='emotion-sjbikb']")).click()
################################################################