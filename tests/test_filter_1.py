from time import sleep
from pages.filter_1 import FiltersPage1
import allure
from test_autorization import authorized_browser

def test_filter_1(browser,authorized_browser):
    with allure.step("Test filter_1"):
        filters_page_1 = FiltersPage1(browser)

    with allure.step("open_filter_1"):
        filters_page_1.open()

    with allure.step("cat"):
        filters_page_1.cat()
        sleep(2)

    with allure.step("blu"):
        filters_page_1.blu()

    with allure.step("kitchen"):
        filters_page_1.kitchen()

    with allure.step("menu"):
        filters_page_1.menu()
        sleep(2)

    with allure.step("search"):
        filters_page_1.search()
        sleep(2)

    with allure.step("back"):
        filters_page_1.back()
        sleep(3)
