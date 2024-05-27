import webbrowser
from time import sleep

from pages.base import BasePage
from selenium.webdriver.common.by import By

plus_ingredients = (By.XPATH, "//div[@class='emotion-rnz1vw'][1]")
minus_ingredients = (By.XPATH, "//div[@class='emotion-rnz1vw'][2]")


class FiltersPage2(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.minus_ingredients = None
        self.plus_ingredients = None

    def open(self):
        self.browser.get('https://eda.ru')
        sleep(2)
        self.browser.refresh()

    def open_search(self):
        self.find((By.XPATH, "//span[text()='Ингредиенты, детали']")).click()
        sleep(2)

    def plus(self):
        self.plus_ingredients = self.find(plus_ingredients)
        self.plus_ingredients.click()
        return self.plus_ingredients.send_keys('куринное филе')
        sleep(5)

    def minus(self):
        self.minus_ingredients = self.find(minus_ingredients).click()
        self.minus_ingredients.click()
        return self.minus_ingredients.send_keys('огурцы, лимон')
        sleep(5)


