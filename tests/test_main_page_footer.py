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
        (page.btn_footers_, 'Bonus Points', '√=https://www.onetwotrip.com/en-us/loyalty/bonuses/'),
        (page.btn_footers_, 'User Agreement', 'https://support.onetwotrip.com/hc/en-us/sections/201758669#208009765'),
        (page.btn_footers_, 'Privacy Policy', 'https://support.onetwotrip.com/hc/en-us/articles/208009765-OneTwoTrip-Privacy-Policy')
        (page.btn_footers_, 'About us', 'https://www.onetwotrip.com/en-us/landings/about/')
    ]

    for elements, elements_text, url_elements in elements_footers:
        with allure.step(f'Test "{elements_text}" display'):
            check.is_true(elements.is_visible())

        with allure.step(f'Test "{elements_text}" clickability'):
            check.is_true(elements.is_clickable())

        with allure.step(f'Test "{elements_text}" text check'):
            check.equal(elements.get_text(), elements_text)