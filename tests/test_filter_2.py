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

    with allure.step("plus"):
        filters_page_2.plus()

    with allure.step("minus"):
        filters_page_2.minus()
