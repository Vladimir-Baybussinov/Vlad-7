from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

search = (By.XPATH, "//button[@class='emotion-144n0ca']")
product = (By.XPATH, "//span[@class='emotion-1jmyaem' and text()='Картофельное пюре']")
search_line = (By.XPATH, "//input[@type='text']")


class SearchPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self): #Открываем страницу
        self.browser.get('https://eda.ru')
        self.browser.refresh()

    def search_find(self): #Находим кнопку поиска
        return self.find(search)

    def search_click(self): #Нажимаем на кнопку поиска
        return self.search_find().click()

    def search_line_find(self): #Находим строку поиска
        return self.find(search_line)

    def search_line_click(self): #Нажимаем на строку поиска
        return self.search_line_find().click()

    def search_line_write(self): #Вводим в строку поиска название продукта
        return self.search_line_find().send_keys('Картофель')

    def product_find(self): #Находим продукт
        return self.find(product)

    def product_choose(self): #Нажимаем на продукт
        return self.product_find().click()

    def test_url(self): #Проверяем url
        expected_url = "https://eda.ru/recepty/osnovnye-blyuda/kartofelnoe-pjure-29188"
        actual_url = self.browser.current_url
        assert actual_url == expected_url, f"Expected {expected_url}, but got {actual_url}"
