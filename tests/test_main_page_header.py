import time

import allure
import pytest_check as check
from locators.locators_main_page import MainPage
from conftest import web_browser


@allure.story('Travel site main page test')
@allure.feature('Block display test')


@allure.feature('Header test')
def test_headers(web_browser):
    """This test checks main page header"""

    page = MainPage(web_browser)

    elements_headers = [
        (page.btn_headers_home, 'Home', 'https://www.onetwotrip.com/en-us/'),
        (page.btn_headers_bonus, 'Bonus','https://www.onetwotrip.com/en-us/loyalty/bonuses/'),
        (page.btn_headers_customer_support, 'CustomerSupport','https://www.onetwotrip.com/en-us/'),
        (page.btn_headers_my_travel, 'MyTravel', 'https://www.onetwotrip.com/en-us/ticket/'),
        (page.btn_headers_personal_area, 'PersonalArea', 'https://www.onetwotrip.com/en-us/ticket/'),
        (page.btn_headers_language, 'Language', 'https://www.onetwotrip.com/en-us/')
    ]

    for elements, elements_text, url_elements in elements_headers:
        with allure.step(f'Test "{elements_text}" display'):
            check.is_true(elements.is_visible())

        with allure.step(f'Test "{elements_text}" clickability'):
            check.is_true(elements.is_clickable())

        with allure.step(f'Test "{elements_text}" text check'):
            check.equal(elements.get_text(), elements_text)


        with allure.step('Test_home'):
            check.is_true(page.btn_headers_home.is_visible())
            check.is_true(page.btn_headers_home.is_clickable())
            check.equal(page.btn_headers_home.get_attribute('href'),'/ en-us/')

        with allure.step('Test_bonus'):
            check.is_true(page.btn_headers_bonus.is_visible())
            check.is_true(page.btn_headers_bonus.is_clickable())
            check.equal(page.btn_headers_bonus.get_text(), 'Bonus')
            check.equal(page.btn_headers_bonus.get_attribute('href'), 'https:// www. onetwotrip. com/ en-us/ loyalty/ bonuses/')

        with allure.step('Test_customer_support'):
            check.is_true(page.btn_headers_customer_support.is_visible())
            check.is_true(page.btn_headers_customer_support.is_clickable())
            check.equal(page.btn_headers_customer_support.get_text(), 'CustomerSupport')
            check.equal(page.btn_headers_customer_support.get_attribute('data-locator'), 'nav-dropdown"// div')


        with allure.step('Test_faq'):
            page.btn_headers_customer_support.click()
            check.is_true(page.btn_drop_down_faq.is_visible())
            check.is_true(page.btn_drop_down_faq.is_clickable())
            check.equal(page.btn_drop_down_faq.get_text(), 'FAQ')
            check.equal(page.btn_drop_down_faq.get_attribute('href'), 'https://support.onetwotrip.com/hc/en-us')
        #
        # with allure.step('My_travel'):
        #     check.is_true(page.btn_headers_my_travel.is_visible())
        #     check.is_true(page.btn_headers_my_travel.is_clickable())
        #     check.equal(page.btn_headers_my_travel.get_text(), 'My_travel')
        #     check.equal(page.btn_headers_my_travel.get_attribute('href'), 'https:// www. onetwotrip. com/ en-us/ ticket/')
        #
        # with allure.step('Personal_area'):
        #     check.is_true(page.btn_headers_personal_area.is_visible())
        #     check.is_true(page.btn_headers_personal_area.is_clickable())
        #     check.equal(page.btn_headers_personal_area.get_text(), 'Personal_area')
        #     check.equal(page.btn_headers_personal_area.get_attribute('button[@data-locator'), 'Button profileLogin" and @type="button"]// div')
        #
        # with allure.step('Language'):
        #     check.is_true(page.btn_headers_language.is_visible())
        #     check.is_true(page.btn_headers_language.is_clickable())
        #     check.equal(page.btn_headers_language.get_text(), 'Language')
        #     check.equal(page.btn_headers_language.get_attribute('@fill="#F0F0F0"'), 'and @cx="256" and @cy="256" and @r="256"]')
        #
        #
        #






