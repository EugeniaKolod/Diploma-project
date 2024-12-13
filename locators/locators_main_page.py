import os

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.onetwotrip.com/'

        super().__init__(web_driver, url)

    btn_headers_home = WebElement(xpath= '(//a[@href="/en-us/"])[1]')
    btn_headers_bonus = WebElement(xpath='//*[@href="https://www.onetwotrip.com/en-us/loyalty/bonuses/"]')
    btn_headers_customer_support = WebElement(xpath='//*[@data-locator="nav-dropdown"]//div")]')
    btn_drop_down_faq = WebElement(xpath='//*[@href = "https://support.onetwotrip.com/hc/en-us", "faq")]')
    btn_headers_my_travel = WebElement(xpath='//a[@href="https://www.onetwotrip.com/en-us/ticket/"]')
    btn_headers_personal_area = WebElement(xpath='//button[@data-locator="Button profileLogin" and @type="button"]//div')
    btn_headers_language = WebElement(xpath='//*[@fill="#F0F0F0" and @cx="256" and @cy="256" and @r="256"]')


    btn_pip_up_сookie = WebElement(id="accept")
    block_main = WebElement(xpath='//div[@class="m-section main-intro"]')
    txt_main_h1 = WebElement(xpath='//h1[@class="intro-title m-font-hl1"]')
    input_main_wrapper = WebElement(xpath='//input[@class="m-input m-b1"]')
    btn_search_domain = WebElement(xpath='//button[@class="m-button red"]')
    text_results_search_domain = WebElement(xpath='//div[@class="group-valid group-domain"]//div[@class="name tCell middle"]')
    text_by_zone = WebElement(xpath='(//span[@class="domain-name m-font-l2"])[1]')
    group_valid_domain = WebElement(xpath='//div[@class="tabCont"]')
    btn_domain_link = WebElement(xpath='//*[contains(text(), "Подобрать домен")]')
    btn_count_box = ManyWebElements(xpath='//div[contains(@class, "category-item m-font-l2")]')
    count_box = ManyWebElements(xpath='//a[@class="solutions-item"]')
