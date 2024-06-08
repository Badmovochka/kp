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
            (page.btn_headers_1_my_feed, 'Моя лента', 'https://habr.com/ru/feed/'),
            (page.btn_headers_2_all_streams, 'Все потоки', 'https://habr.com/ru/articles/'),
            (page.btn_headers_3_development, 'Разработка', 'https://habr.com/ru/flows/develop/'),
            (page.btn_headers_4_admin, 'Администрирование', 'https://habr.com/ru/flows/admin/'),
            (page.btn_headers_5_design, 'Дизайн', 'https://habr.com/ru/flows/design/'),
            (page.btn_headers_6_management, 'Менеджмент', 'https://habr.com/ru/flows/management/'),
            (page.btn_headers_7_marketing, 'Маркетинг', 'https://habr.com/ru/flows/marketing/'),
            (page.btn_headers_8_popsci, 'Научпоп', 'https://habr.com/ru/flows/popsci/')
        ]

    for button, button_text , button_link in header_buttons:
        with allure.step(f'Проверка видимости элемента "{button_text}"'):
            check.is_true(button.is_visible())

        with allure.step(f'Проверка кликабельности элемента "{button_text}"'):
            check.is_true(button.is_clickable())

        with allure.step(f'Проверка текста элемента "{button_text}"'):
            btn_text = button.get_text()
            check.equal(btn_text, button_text, f'Тест локатора "{button_text}" не равен ожидаемому результату')

        with allure.step(f'Проверка ссылки элемента {button_text}'):
            btn_link = button.get_attribute('href')
            check.equal(btn_link, button_link, f'Ссылка локатора {button_text} не равна ожидаемой')


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
@allure.feature('Проверка поиска')
def test_search(web_browser):
    """Этот тест проверяет строку поиска"""

    page = MainPage(web_browser)

    page.btn_search.click()
    time.sleep(1)

    searched_value = 'Тестирование'

    page.field_search.send_keys(searched_value)

    page.btn_submit_search.click()
    time.sleep(1)

    with allure.step(f'Проверка, что поиск выдал ленту результатов'):
        check.is_true(page.articles_feed.is_visible())

    with allure.step(f'Проверка, что результатов поиска больше одного'):
        check.greater_equal(page.articles.count(), 1)

    count = 1
    for article in page.articles:
        with allure.step(f'Проверка, что статья № {count} содержит искомое слово "{searched_value}"'):
            check.is_true(article.text.find(searched_value))
        count += 1

@allure.story('Проверка главной страницы')
@allure.feature('Проверка меню "Настройки языка" (радио-баттоны)')
def test_settings_radios(web_browser):
    """Этот тест проверяет радио-баттоны в настройках"""

    page = MainPage(web_browser)

    page.scroll_down()
    time.sleep(1)

    page.btn_settings.click()
    time.sleep(1)

    radio_buttons = [
        (page.radio_russian, page.radio_russian_label, "Русский"),
        (page.radio_english, page.radio_english_label, "English"),
        (page.radio_classic, page.radio_classic_label, "Classic"),
        (page.radio_compact, page.radio_compact_label, "Compact"),
        (page.radio_dark, page.radio_dark_label, "Dark"),
        (page.radio_light, page.radio_light_label, "Light"),
        (page.radio_system, page.radio_system_label, "System")
    ]

    for radio, radio_label, required_radio_text in radio_buttons:
        radio.scroll_to_element()

        with allure.step(f'Проверка элемента "{required_radio_text}" на наличие'):
            check.is_true(radio_label.is_presented(), f'Radio button {required_radio_text} is not presented')

        with allure.step(f'Проверка текста элемента "{required_radio_text}" на отображение'):
            check.is_true(radio_label.is_visible(), f'Radio button text {required_radio_text} is not displayed')

        with allure.step(f'Проверка элемента "{required_radio_text}" на кликабельность'):
            check.is_true(radio_label.is_clickable(), f'Radio button {required_radio_text} is not clickable')

        with allure.step(f'Проверка, что элемент "{required_radio_text}" выбран'):
            radio_label.click()
            time.sleep(2)
            check.is_true(radio.is_selected(), f'Radio button {required_radio_text} is not selected')

@allure.story('Проверка главной страницы')
@allure.feature('Проверка меню "Настройки языка" (чекбоксы)')
def test_settings_checkboxes(web_browser):
    """Этот тест проверяет чекбоксы в настройках"""

    page = MainPage(web_browser)

    page.scroll_down()
    time.sleep(1)

    page.btn_settings.click()
    time.sleep(1)

    checkboxes = [
        (page.checkbox_russian, page.checkbox_russian_label, "Русский"),
        (page.checkbox_english, page.checkbox_english_label, "Английский")
    ]

    for checkbox, checkbox_label, required_checkbox_text in checkboxes:
        checkbox.scroll_to_element()

        with allure.step(f'Проверка элемента "{required_checkbox_text}" на наличие'):
            check.is_true(checkbox_label.is_presented(), f'Checkbox {required_checkbox_text} is not presented')

        with allure.step(f'Проверка текста элемента "{required_checkbox_text}" на отображение'):
            check.is_true(checkbox_label.is_visible(), f'Checkbox text {required_checkbox_text} is not displayed')

        with allure.step(f'Проверка элемента "{required_checkbox_text}" на кликабельность'):
            check.is_true(checkbox_label.is_clickable(), f'Checkbox {required_checkbox_text} is not clickable')

        with allure.step(f'Проверка, что элемент "{required_checkbox_text}" выбран'):
            if checkbox.is_selected() is False:
                checkbox_label.click()
                time.sleep(1)
            check.is_true(checkbox.is_selected(), f'Checkbox {required_checkbox_text} is not selected')

    for checkbox, checkbox_label, required_checkbox_text in checkboxes:
        checkbox.scroll_to_element()
        if checkbox.is_selected():
            checkbox_label.click()

    with allure.step(f'Проверка появления предупреждающего текста'):
        check.is_true(page.checkbox_warning.is_visible(), f'Checkbox warning is not displayed')
        warning_text = page.checkbox_warning.get_text()
        check.equal(warning_text, 'Должен быть выбран хотя бы один язык', f'Текст предупреждающего уведомления не равен ожидаемому')
