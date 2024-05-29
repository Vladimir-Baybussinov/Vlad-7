from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

search = (By.XPATH, "//button[@class='emotion-144n0ca']")
product = (By.XPATH, "//div[@class='emotion-1ttdbi2'][2]")
search_line = (By.XPATH, "//input[@type='text']")

class SearchPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://eda.ru')
        self.browser.refresh()

    def search_find(self):
        return self.find(search)

    def search_click(self):
        return self.search_find().click()

    def search_line_find(self):
        return self.find(search_line)

    def search_line_click(self):
        return self.search_line_find().click()

    def search_line_write(self):
        return self.search_line_find().send_keys('картофель')

    def search_dropdown(self):
        return self.find(product)


    def search_choose_product(self):
        return self.search_dropdown().click()

