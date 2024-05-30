from time import sleep

import allure

from pages.autorization_page import AutorizationPage


def test_authorized_browser(browser):
    with allure.step("Open browser autorization page"):
        autorization_page = AutorizationPage(browser)

    with allure.step("Go to web-side"):
        autorization_page.open()
        browser.implicitly_wait(10)
        sleep(1)

    with allure.step("Sing in"):
        autorization_page.sing_in()
        browser.implicitly_wait(10)

    with allure.step("Switch to new window"):
        new_window = browser.window_handles[1]
        browser.switch_to.window(new_window)

    with allure.step("Post"):
        autorization_page.post()
        sleep(1)

    with allure.step("pas"):
        autorization_page.pas()
        sleep(1)

    with allure.step("log"):
        autorization_page.log()

    ################################
    with allure.step("Switch to original window"):
        original_window = browser.window_handles[0]
        browser.switch_to.window(original_window)
        sleep(3)

    return browser
    #################################
