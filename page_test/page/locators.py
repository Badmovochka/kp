import os

from page_test.page.base_page import WebPage
from page_test.page.elements import WebElement
from page_test.page.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://habr.com/ru/feed/'

        super().__init__(web_driver, url)

    #header buttons
    btn_headers_1_my_feed = WebElement(xpath='//*[@class = "tm-main-menu__item tm-main-menu__item_active" and text()="Моя лента"]')
    btn_headers_2_all_streams = WebElement(xpath='//*[@class = "tm-main-menu__item" and text()="Все потоки"]')
    btn_headers_3_development = WebElement(xpath='//*[@class = "tm-main-menu__item" and text()="Разработка"]')
    btn_headers_4_admin = WebElement(xpath='//*[@class = "tm-main-menu__item" and text()="Администрирование"]')
    btn_headers_5_design = WebElement(xpath='//*[@class = "tm-main-menu__item" and text()="Дизайн"]')
    btn_headers_6_management = WebElement(xpath='//*[@class = "tm-main-menu__item" and text()="Менеджмент"]')
    btn_headers_7_marketing = WebElement(xpath='//*[@class = "tm-main-menu__item" and text()="Маркетинг"]')
    btn_headers_8_popsci = WebElement(xpath='//*[@class = "tm-main-menu__item" and text()="Научпоп"]')

    #footer buttons
    btn_footer_1 = WebElement(xpath='//*[@class = "tm-footer-menu__block-title" and text()="Ваш аккаунт"]')
    btn_footer_1_1 = WebElement(xpath='//li[@class = "tm-footer-menu__list-item"]/a[text()="Войти"]')
    btn_footer_1_2 = WebElement(xpath='//li[@class = "tm-footer-menu__list-item"]/a[text()="Регистрация"]')

    btn_footer_2 = WebElement(xpath='//*[@class = "tm-footer-menu__block-title" and text()="Разделы"]')
    btn_footer_2_1 = WebElement(xpath='//*[@class = "footer-menu__item-link" and text()="Статьи"]')
    btn_footer_2_2 = WebElement(xpath='//*[@class = "footer-menu__item-link" and text()="Новости"]')
    btn_footer_2_3 = WebElement(xpath='//*[@class = "footer-menu__item-link" and text()="Хабы"]')
    btn_footer_2_4 = WebElement(xpath='//*[@class = "footer-menu__item-link" and text()="Компании"]')
    btn_footer_2_5 = WebElement(xpath='//*[@class = "footer-menu__item-link" and text()="Авторы"]')
    btn_footer_2_6 = WebElement(xpath='//*[@class = "footer-menu__item-link" and text()="Песочница"]')

    btn_footer_3 = WebElement(xpath='//*[@class = "tm-footer-menu__block-title" and text()="Информация"]')
    btn_footer_3_1 = WebElement(xpath='//*[@class = "footer-menu__item-link" and text()="Устройство сайта"]')
    btn_footer_3_2 = WebElement(xpath='//*[@class = "footer-menu__item-link" and text()="Для авторов"]')
    btn_footer_3_3 = WebElement(xpath='//*[@class = "footer-menu__item-link" and text()="Для компаний"]')
    btn_footer_3_4 = WebElement(xpath='//*[@class = "footer-menu__item-link" and text()="Документы"]')
    btn_footer_3_5 = WebElement(xpath='//*[@class = "tm-footer-menu__list-item"]/a[text()="Соглашение"]')
    btn_footer_3_6 = WebElement(xpath='//*[@class = "tm-footer-menu__list-item"]/a[text()="Конфиденциальность"]')

    btn_footer_4 = WebElement(xpath='//*[@class = "tm-footer-menu__block-title" and text()="Услуги"]')
    btn_footer_4_1 = WebElement(xpath='//*[@class = "tm-footer-menu__list-item"]/a[text()="Корпоративный блог"]')
    btn_footer_4_2 = WebElement(xpath='//*[@class = "tm-footer-menu__list-item"]/a[text()="Медийная реклама"]')
    btn_footer_4_3 = WebElement(xpath='//*[@class = "tm-footer-menu__list-item"]/a[text()="Нативные проекты"]')
    btn_footer_4_4 = WebElement(xpath='//*[@class = "tm-footer-menu__list-item"]/a[text()="Образовательные программы"]')
    btn_footer_4_5 = WebElement(xpath='//*[@class = "tm-footer-menu__list-item"]/a[text()="Стартапам"]')

    #settings buttons, radios & checkboxes
    btn_settings = WebElement(xpath='//button[@class = "tm-footer__link"]')
    radio_russian = WebElement(xpath='//*[@id = "uiRussian"]')
    radio_russian_text = WebElement(xpath='//*[@class = "tm-input-radio-labeled__label"][text()="Русский"]')

    # radio_buttons = [
    #     ['uiRussian', '//*[@id="overlays"]/div/div[2]/div/div/form/div[2]/div[2]/p[1]/div/label', "Русский"],
    #     ['uiEnglish', '//*[@id="overlays"]/div/div[2]/div/div/form/div[2]/div[2]/p[2]/div/label', "English"],
    #     ['feed', '//*[@id="overlays"]/div/div[2]/div/div/form/div[4]/div[2]/p[1]/div/label', "Classic"],
    #     ['feed', '//*[@id="overlays"]/div/div[2]/div/div/form/div[4]/div[2]/p[2]/div/label', "Compact"],
    #     ['colorTheme', '//*[@id="overlays"]/div/div[2]/div/div/form/div[5]/div[2]/p[1]/div/label', "Dark"],
    #     ['colorTheme', '//*[@id="overlays"]/div/div[2]/div/div/form/div[5]/div[2]/p[2]/div/label', "Light"],
    #     ['colorTheme', '//*[@id="overlays"]/div/div[2]/div/div/form/div[5]/div[2]/p[3]/div/label', "System"]
    # ]

    #searchbox
    btn_search = WebElement(xpath='//*[@class="tm-svg-img tm-header-user-menu__icon tm-header-user-menu__icon_search tm-header-user-menu__icon_dark"]')
    field_search = WebElement(xpath='//*[@class="tm-search__input tm-input-text-decorated__input"]')
    btn_submit_search = WebElement(xpath='//*[@class="tm-svg-img tm-svg-icon" and @height = "16"]')

    #search results page
    articles_feed = WebElement(xpath='//*[@class="tm-articles-list"]')
    articles = ManyWebElements(xpath='//*[@class="tm-articles-list__item"]')