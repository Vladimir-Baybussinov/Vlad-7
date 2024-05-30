from time import sleep

import allure

from pages.autorization_page import AutorizationPage


def test_authorized_browser(browser):
    with allure.step("Open browser autorization page"):
        autorization_page = AutorizationPage(browser)

    with allure.step("Go to web-side"):
        autorization_page.open()
        sleep(1)

    with allure.step("Sing in find"):
        autorization_page.sing_in_find()

    with allure.step("Sing in click"):
        autorization_page.sing_in_click()

    with allure.step("Switch to new window"):
        new_window = browser.window_handles[1]
        browser.switch_to.window(new_window)

    with allure.step("Post Find"):
        autorization_page.post_find()

    with allure.step("Post Click"):
        autorization_page.post_click()

    with allure.step("Post Write"):
        autorization_page.post_write()

    with allure.step("pas Find"):
        autorization_page.pas_find()

    with allure.step("pas Click"):
        autorization_page.pas_click()

    with allure.step("pas Write"):
        autorization_page.pas_write()

    with allure.step("log find"):
        autorization_page.log_find()

    with allure.step("log click"):
        autorization_page.log_click()

    ################################
    with allure.step("Switch to original window"):
        original_window = browser.window_handles[0]
        browser.switch_to.window(original_window)

    return browser
    #################################
