import webbrowser
from time import sleep

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

popular_ingredients = (By.XPATH, "//div[@class='emotion-1wxt7g0']" and "//button[contains(text(), 'Куриное филе')]")
add_ingredients = (By.XPATH, "(//input[@type='text'])[1]")
ingreditent = (By.XPATH, "//button[@class='emotion-kuminy']")
type = (By.XPATH, "//div[@class='emotion-16rmb3']")
del_ingredients = (By.XPATH, "(//input[@type='text'])[2]")


class FiltersPage2(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self): # Переходим на страницу с расшыренным поиском
        self.browser.get('https://eda.ru')
        self.browser.refresh()

    ################################################################
    def open_search(self): #Открываем расширенный поиск
        self.find((By.XPATH, "//span[text()='Ингредиенты, детали']")).click()
        sleep(2)

    def add_ingred_find(self): #Находим строку поиска ингредиента
        self.browser.implicitly_wait(10)
        return self.find(add_ingredients)

    def add_ingredients_click(self):#Нажимаем на строку поиска ингредиента
        return self.add_ingred_find().click()

    def add_ingredients_send_text(self): #Добавляем ингредиент в строку поиска
        return self.add_ingred_find().send_keys('Помидоры')

    def add_ingredients_send_text_2(self): #Добавляем ингредиент в строку поиска
        return self.add_ingred_find().send_keys('Сыр')

    def find_ingredient_dropdown(self): #Находим выпадающий список ингредиентов
        return self.find(ingreditent)

    def choose_ingredient(self): #Выбираем ингредиент из выпадающего списка
        return self.find_ingredient_dropdown().click()

    ################################################################
    def popular_ingredients_find(self): #Находим кнопку с названием ингредиента
        return self.find(popular_ingredients)

    def popular_ingredients_click(self): #Нажимаем на кнопку с названием ингредиента
        return self.popular_ingredients_find().click()

    def type_find(self): #Находим кнопку с типом ингредиента
        return self.find(type)

    def type_click(self): #Нажимаем на кнопку с типом ингредиента
        return self.type_find().click()




    def del_ingredients_find(self): #Находим строку поиска ингредиента
        return self.find(del_ingredients)

    def del_ingredients_click(self): #Нажимаем на строку поиска ингредиента
        return self.del_ingredients_find().click()

    def del_ingredients_send_text(self): #Добавляем ингредиент в строку поиска
        return self.del_ingredients_find().send_keys('Огурцы')

    def del_ingredients_send_text_2(self): #Добавляем ингредиент в строку поиска
        return self.del_ingredients_find().send_keys('Лимон')

    def del_find_ingredients_dropdown(self): #Находим выпадающий список ингредиентов
        return self.find(ingreditent)

    def del_choose_ingredient(self): #Выбираем ингредиент из выпадающего списка
        return self.del_find_ingredients_dropdown().click()





    def search(self):
        self.find((By.XPATH, "//button[@class='emotion-sjbikb']")).click()

    def scroll(self):  # Прокручиваем страницу
        self.browser.execute_script("window.scrollTo(0, 500)")
################################################################

    def test_url(self):
        expected_url = "https://eda.ru/recepty/afishaeda/poshagovye-recepty/ingredienty/13439/13426/13544/eingredienty/15137/13427?isEdaChecked=true"
        actual_url = self.browser.current_url
        assert actual_url == expected_url, f"Expected {expected_url}, but got {actual_url}"