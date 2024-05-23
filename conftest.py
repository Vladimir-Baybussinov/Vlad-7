from time import sleep

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from pages.autorization import AutorizationPage


@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    chrome_browser.maximize_window()
    return chrome_browser



