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

    with allure.step("find_plus1_tomatos"):
        filters_page_2.add_ingredients_click()
        sleep(2)

    with allure.step("find_plus2_tomatos"):
        filters_page_2.add_ingredients_send_text()
        sleep(2)

    with allure.step("find_plus3_tomatos"):
        filters_page_2.choose_ingredient()
        sleep(2)


#




    ################################

    with allure.step("find_plus1_cheese"):
        filters_page_2.add_ingredients_click()
        sleep(2)

    with allure.step("find_plus2_cheese"):
        filters_page_2.add_ingredients_send_text_2()
        sleep(2)

    with allure.step("find_plus3_cheese"):
        filters_page_2.choose_ingredient()
        sleep(2)

    ################################################


    with allure.step("del_ingredients_find"):
        filters_page_2.del_ingredients_find()

    with allure.step("del_ingredients_click"):
        filters_page_2.del_ingredients_click()


    with allure.step("del_ingredients_send_text"):
        filters_page_2.del_ingredients_send_text()


    with allure.step("del_ingredients_choose_ingredient"):
        filters_page_2.del_choose_ingredient()


        #################################################
    with allure.step("del_ingredients_find_limon"):
        filters_page_2.del_ingredients_find()

    with allure.step("del_ingredients_click_limon"):
        filters_page_2.del_ingredients_click()


    with allure.step("del_ingredients_send_text_2"):
        filters_page_2.del_ingredients_send_text_2()


    with allure.step("del_ingredients_choose_ingredient_limon"):
        filters_page_2.del_choose_ingredient()

    #######################

    with allure.step("popular_ingredients_find"):
        filters_page_2.popular_ingredients_find()

    with allure.step("popular_ingredients_click"):
        filters_page_2.popular_ingredients_click()

    with allure.step("type_find"):
        sleep(1)
        filters_page_2.type_find()

    with allure.step("type_click"):
        sleep(1)
        filters_page_2.type_click()

    with allure.step("type2_find"):
        sleep(1)
        filters_page_2.type_find()

    with allure.step("type2_click"):
        sleep(1)
        filters_page_2.type_click()

    with allure.step("search"):
        filters_page_2.search()
        sleep(2)
