from time import sleep

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class FiltersPage1(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self): #открыть страницу
        self.browser.get('https://eda.ru')

    def cat(self): #выбрать категорию
        self.find((By.XPATH, "//div[@class='emotion-1jy0sh8']")).click()

        self.find((By.XPATH, "//button[contains(text(), 'Основные блюда')]")).click()

    def blu(self): #выбрать блюдо
        self.find((By.XPATH, "//div[@class='emotion-1pba6yl']")).click()

        self.find((By.XPATH, "//button[contains(text(), 'Котлеты')]")).click()

    def kitchen(self): #выбрать кухню
        self.find((By.XPATH, "//div[@class='emotion-1nwm3v3']")).click()

        self.find((By.XPATH, "//button[contains(text(), 'Русская кухня')]")).click()

    def menu(self):#выбрать меню
        self.find((By.XPATH, "//div[@class='emotion-1yrtqfb']")).click()

        self.find((By.XPATH, "//button[contains(text(), 'Детское меню')]")).click()

    def search(self):#нажать кнопку поиска
        self.find((By.XPATH, "//button[@class='emotion-1842bel']")).click()

    def scroll(self):  # Прокручиваем страницу
        self.browser.execute_script("window.scrollTo(0, 500)")

    def back(self):  # Возвращаемся на предыдущую страницу
        self.browser.back()
        sleep(0.5)