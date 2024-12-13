import time

import allure
import pytest_check as check
from locators.locators_main_page import MainPage
from conftest import web_browser


@allure.story('Travel site main page test')
@allure.feature('Block display test')

@allure.feature('Footer test')
def test_footers(web_browser):
    """This test checks main page footer"""

    page = MainPage(web_browser)

    elements_footers = [
        (page.btn_footers_, 'Contact support', 'https://support.onetwotrip.com/hc/en-us?utm_source=mainMenu'),
        (page.btn_footers_, 'FAQ', 'https://support.onetwotrip.com/hc/en-us/'),
        (page.btn_footers_, 'Bonus'),
        (page.btn_footers_, 'MyTravel', 'https://www.onetwotrip.com/en-us/ticket/'),
        (page.btn_footers_, 'PersonalArea', 'https://www.onetwotrip.com/en-us/ticket/')]