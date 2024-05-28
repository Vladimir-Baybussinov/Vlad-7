from time import sleep
from pages.recipes import RecopesPage
import allure


def test_recipes(browser):
    with allure.step("Test recipes"):
        recipes_page = RecopesPage(browser)

    with allure.step("open"):
        recipes_page.open()
        sleep(0.5)

    with allure.step("open_recopes"):
        recipes_page.open_recopes()

    with allure.step("recipe_ingridients"):
        recipes_page.recipe_ingridients()

    with allure.step("portion_plus"):
        recipes_page.portion_plus()

