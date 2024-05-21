import webbrowser
from time import sleep

from pages.base import BasePage
from selenium.webdriver.common.by import By

plus_ingredients = (By.XPATH, "//div[@class=['emotion-14cydt5']")
minus_ingredients = (By.XPATH, "//div[@class=['emotion-14cydt5']")


class FiltersPage2(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        return self.browser.get('http://eda.ru')
        self.refresh()

    def open_search(self):
        self.find((By.XPATH, "//span[text()='Ингредиенты, детали']")).click()
        sleep(2)
    def plus(self):
        self.find(plus_ingredients).click()
        return self.plus_ingredients.send_keys('куринное филе, помидоры, сыр')
        sleep(5)

    def minus(self):
        self.find(minus_ingredients).click()
        return self.minus_ingredients.send_keys('огурцы, лимон')
        sleep(5)

