''''''

import os

from page_test.page.base_page import WebPage
from page_test.page.elements import WebElement


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://hoster.by'

        super().__init__(web_driver, url)

    # btn_headers_domain = WebElement(xpath='//div[@id="menu-item"]//span[contains(text(),"Домены")]')
    # btn_headers_hosting = WebElement(xpath='//div[@id="menu-item"]//span[contains(text(),"Хостинг")]')
    # btn_headers_cloud = WebElement(xpath='//div[@id="menu-item"]//span[contains(text(),"Облако")]')
    # btn_headers_mail = WebElement(xpath='//div[@id="menu-item"]//span[contains(text(),"Почта")]')

    input_space = WebElement(xpath='//*[@class = "m-input m-b1"]')
    submit_button = WebElement(xpath='//*[@class = "m-button red"]')

    text_results_search_domain_text = WebElement(xpath='')

    domain_text = WebElement(xpath='//*[@name = "domain_name"]')

    text_by_zone = WebElement(xpath='//*[@name = "choosedzones" and @id = "choosedby"]')



