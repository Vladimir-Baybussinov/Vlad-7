from time import sleep
from pages.filter_2 import FiltersPage2
import allure


def test_filter_2(browser):
    with allure.step('Test filter_2'):
        filters_page_2 = FiltersPage2(browser)

    with allure.step("open_filters_2"):
        filters_page_2.open()
        sleep(3)

    with allure.step("open_search"):
        filters_page_2.open_search()
################################################
    with allure.step("find_plus"):
        filters_page_2.find_plus()
        sleep(2)

    with allure.step("find_plus2"):
        filters_page_2.add_ingredients_click()
        sleep(2)

    with allure.step("find_plus3"):
        filters_page_2.add_ingredients_send_text()
        sleep(2)

    with allure.step("find_plus3"):
        filters_page_2.choose_ingredient()
        sleep(2)


################################################
    with allure.step("plus"):
        filters_page_2.plus()

    with allure.step("type"):
        filters_page_2.type()

    with allure.step("type2"):
        filters_page_2.type()

    with allure.step("search"):
        filters_page_2.search()
        sleep(2)



