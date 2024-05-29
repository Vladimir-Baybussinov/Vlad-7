from pages.search_page import SearchPage
from time import sleep
import allure


def test_search(browser):
    with allure.step("Test search"):
        search_page = SearchPage(browser)

    with allure.step("open"):
        search_page.open()

    with allure.step("search_find"):
        search_page.search_find()

    with allure.step("search_click"):
        search_page.search_click()

    with allure.step("search_line_find"):
        search_page.search_line_find()

    with allure.step("search_line_click"):
        search_page.search_line_click()

    with allure.step("search_line_write"):
        search_page.search_line_write()

    with allure.step("search_dropdown"):
        search_page.search_dropdown()
        sleep(5)

    with allure.step("search_choose_product"):
        search_page.search_choose_product()
        sleep(5)
