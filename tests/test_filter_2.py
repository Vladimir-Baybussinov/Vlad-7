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

    with allure.step("find_plus"):
        filters_page_2.find_plus()

    with allure.step("plus"):
        filters_page_2.plus()

    with allure.step("send1"):
        filters_page_2.send1()

    with allure.step("find_minus"):
        filters_page_2.find_minus()

    with allure.step("minus"):
        filters_page_2.minus()

    with allure.step("send2"):
        filters_page_2.send2()
