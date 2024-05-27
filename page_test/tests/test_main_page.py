import allure
import pytest
import pytest_check as check
from page_test.page.locators import MainPage
from selenium.webdriver.common.action_chains import ActionChains
import time

@allure.story('Проверка главной страницы')
@allure.feature('Проверка хедера')
def test_headers(web_browser):
    """Этот тест проверяет хедер главной страницы"""

    page = MainPage(web_browser)

    header_buttons = [
            (page.btn_headers_1_my_feed, 'Моя лента'),
            (page.btn_headers_2_all_streams, 'Все потоки'),
            (page.btn_headers_3_development, 'Разработка'),
            (page.btn_headers_4_admin, 'Администрирование'),
            (page.btn_headers_5_design, 'Дизайн'),
            (page.btn_headers_6_management, 'Менеджмент'),
            (page.btn_headers_7_marketing, 'Маркетинг'),
            (page.btn_headers_8_popsci, 'Научпоп')
        ]

    for button, button_text in header_buttons:
        with allure.step(f'Проверка видимости элемента "{button_text}"'):
            check.is_true(button.is_visible())

        with allure.step(f'Проверка кликабельности элемента "{button_text}"'):
            check.is_true(button.is_clickable())

        with allure.step(f'Проверка текста элемента "{button_text}"'):
            btn_text = button.get_text()
            check.equal(btn_text, button_text, f'Тест локатора "{button_text}" не равен ожидаемому результату')

#Тесты футера разбиты на разделы, т.к. проверка футера целиком выполняется очень долго
@allure.story('Проверка главной страницы')
@allure.feature('Проверка футера - раздел "Ваш аккаунт')
def test_footer_account(web_browser):
    """Этот тест проверяет раздел футера Ваш аккаунт"""

    page = MainPage(web_browser)

    footer_buttons = [
            (page.btn_footer_1, 'Ваш аккаунт'),
            (page.btn_footer_1_1, 'Войти'),
            (page.btn_footer_1_2, 'Регистрация')
        ]

    page.scroll_down()
    time.sleep(1)

    for button, button_text in footer_buttons:
        with allure.step(f'Проверка видимости элемента "{button_text}"'):
            check.is_true(button.is_visible())

        with allure.step(f'Проверка кликабельности элемента "{button_text}"'):
            check.is_true(button.is_clickable())

        with allure.step(f'Проверка текста элемента "{button_text}"'):
            btn_text = button.get_text()
            check.equal(btn_text, button_text, f'Тест локатора "{button_text}" не равен ожидаемому результату')

@allure.story('Проверка главной страницы')
@allure.feature('Проверка футера - раздел "Разделы')
def test_footer_sections(web_browser):
    """Этот тест проверяет раздел футера Разделы"""

    page = MainPage(web_browser)

    footer_buttons = [
            (page.btn_footer_2, 'Разделы'),
            (page.btn_footer_2_1, 'Статьи'),
            (page.btn_footer_2_2, 'Новости'),
            (page.btn_footer_2_3, 'Хабы'),
            (page.btn_footer_2_4, 'Компании'),
            (page.btn_footer_2_5, 'Авторы'),
            (page.btn_footer_2_6, 'Песочница')
        ]

    page.scroll_down()
    time.sleep(1)

    for button, button_text in footer_buttons:
        with allure.step(f'Проверка видимости элемента "{button_text}"'):
            check.is_true(button.is_visible())

        with allure.step(f'Проверка кликабельности элемента "{button_text}"'):
            check.is_true(button.is_clickable())

        with allure.step(f'Проверка текста элемента "{button_text}"'):
            btn_text = button.get_text()
            check.equal(btn_text, button_text, f'Тест локатора "{button_text}" не равен ожидаемому результату')

@allure.story('Проверка главной страницы')
@allure.feature('Проверка футера - раздел "Информация')
def test_footer_information(web_browser):
    """Этот тест проверяет раздел футера Информация"""

    page = MainPage(web_browser)

    footer_buttons = [
            (page.btn_footer_3, 'Информация'),
            (page.btn_footer_3_1, 'Устройство сайта'),
            (page.btn_footer_3_2, 'Для авторов'),
            (page.btn_footer_3_3, 'Для компаний'),
            (page.btn_footer_3_4, 'Документы'),
            (page.btn_footer_3_5, 'Соглашение'),
            (page.btn_footer_3_6, 'Конфиденциальность')
        ]

    page.scroll_down()
    time.sleep(1)

    for button, button_text in footer_buttons:
        with allure.step(f'Проверка видимости элемента "{button_text}"'):
            check.is_true(button.is_visible())

        with allure.step(f'Проверка кликабельности элемента "{button_text}"'):
            check.is_true(button.is_clickable())

        with allure.step(f'Проверка текста элемента "{button_text}"'):
            btn_text = button.get_text()
            check.equal(btn_text, button_text, f'Тест локатора "{button_text}" не равен ожидаемому результату')

@allure.story('Проверка главной страницы')
@allure.feature('Проверка футера - раздел "Услуги')
def test_footer_services(web_browser):
    """Этот тест проверяет раздел футера Услуги"""

    page = MainPage(web_browser)

    footer_buttons = [
            (page.btn_footer_4, 'Услуги'),
            (page.btn_footer_4_1, 'Корпоративный блог'),
            (page.btn_footer_4_2, 'Медийная реклама'),
            (page.btn_footer_4_3, 'Нативные проекты'),
            (page.btn_footer_4_4, 'Образовательные программы'),
            (page.btn_footer_4_5, 'Стартапам')
        ]

    page.scroll_down()
    time.sleep(1)

    for button, button_text in footer_buttons:
        with allure.step(f'Проверка видимости элемента "{button_text}"'):
            check.is_true(button.is_visible())

        with allure.step(f'Проверка кликабельности элемента "{button_text}"'):
            check.is_true(button.is_clickable())

        with allure.step(f'Проверка текста элемента "{button_text}"'):
            btn_text = button.get_text()
            check.equal(btn_text, button_text, f'Тест локатора "{button_text}" не равен ожидаемому результату')

@allure.story('Проверка главной страницы')
@allure.feature('Проверка меню "Настройки языка" (радио-баттоны и чекбоксы')
def test_settings(web_browser):
    """Этот тест проверяет радио-баттоны и чекбоксы в настройках"""

    page = MainPage(web_browser)

    page.scroll_down()
    time.sleep(1)

    page.btn_settings.click()
    time.sleep(1)

    # radio_buttons = [
    #     ['uiRussian', '//*[@id="overlays"]/div/div[2]/div/div/form/div[2]/div[2]/p[1]/div/label', "Русский"],
    #     ['uiEnglish', '//*[@id="overlays"]/div/div[2]/div/div/form/div[2]/div[2]/p[2]/div/label', "English"],
    #     ['feed', '//*[@id="overlays"]/div/div[2]/div/div/form/div[4]/div[2]/p[1]/div/label', "Classic"],
    #     ['feed', '//*[@id="overlays"]/div/div[2]/div/div/form/div[4]/div[2]/p[2]/div/label', "Compact"],
    #     ['colorTheme', '//*[@id="overlays"]/div/div[2]/div/div/form/div[5]/div[2]/p[1]/div/label', "Dark"],
    #     ['colorTheme', '//*[@id="overlays"]/div/div[2]/div/div/form/div[5]/div[2]/p[2]/div/label', "Light"],
    #     ['colorTheme', '//*[@id="overlays"]/div/div[2]/div/div/form/div[5]/div[2]/p[3]/div/label', "System"]
    # ]

    radio_buttons = [
        (page.radio_russian, page.radio_russian_text, "Русский")
    ]

    for radio, radio_text, required_radio_text in radio_buttons:
        with allure.step(f'Проверка элемента {required_radio_text} на отображение'):
            check.is_true(radio.is_visible(), f'Radio button {required_radio_text} is not displayed')
            check.is_true(radio_text.is_visible(), f'Radio button text {required_radio_text} is not displayed')

        with allure.step(f'Проверка элемента {required_radio_text} на кликабельность'):
            check.is_true(radio.is_clickable(), f'Radio button {required_radio_text} is not clickable')

        with allure.step(f'Проверка, что кнопка {required_radio_text} выбрана'):
            radio.click()
            time.sleep(1)
            check.is_true(radio.is_selected(), f'Radio button {required_radio_text} is not selected')