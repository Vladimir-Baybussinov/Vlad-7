from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RecopesPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://eda.ru')
        self.browser.refresh()

    def open_recopes(self):
        self.find((By.XPATH, "//a[@class='emotion-1twuq6e' and text()='Рецепты']")).click()

    def scroll(self):
        self.browser.execute_script("window.scrollTo(0, 500)")
    def recipe_ingridients(self):
        sleep(1)
        self.find((By.XPATH, "//i[@class='emotion-1m3iuaz']")).click()

    def portion_plus(self):
        sleep(3)
        self.find((By.XPATH, "//i[@class='emotion-p8s8gx']")).click()
        sleep(1)


