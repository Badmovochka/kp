'''Черновики тестов'''

import allure
import pytest
import pytest_check as check
from page_test.page.locators import MainPage
import time


# def test_headers(web_browser):
#     """Этот тест проверяет хедер главной страницы"""
#
#     page = MainPage(web_browser)
#
#     check.equal(page.btn_headers_domain.get_text(), 'Домены', 'Тест локатора не равен ожидаймому результату')
#     check.is_true(page.btn_headers_mail.is_visible())


@allure.story('Проверка главной страницы')
@allure.feature('Проверка строки поиска')
def test_headers(web_browser):
    """Этот тест проверяет строку поиска главной страницы"""

    page = MainPage(web_browser)

    # elements_main_page = [
    #     (page.input_space, 'Введите домены')
    # ]
    #
    # for element, elements_text in elements_main_page:
    #     with allure.step('Проверка видимости строки поиска'):
    #         check.is_true(element.is_visible())
    #
    #     with allure.step('Сверка текста плейсхолдера'):
    #         check.equal(element.get_attribute('placeholder'), elements_text)

    with allure.step('Проверка видимости строки и кнопки поиска'):
        check.is_true(page.input_space.is_visible())
        check.is_true(page.submit_button.is_visible())

    with allure.step('Сверка текста плейсхолдера'):
        check.equal(page.input_space.get_attribute('placeholder'), 'Введите домены')

    with allure.step('Проверка ввода с строку'):
        input_text = 'Тестирование'
        page.input_space.send_keys(input_text)
        time.sleep(1)
        page.submit_button.click()

        check.equal(page.domain_text.get_attribute('value'), input_text.lower())

        page.go_back()

    #дописать локаторы
    with allure.step('Проверка домена и зоны'):
        text_input_main = [
            'hhh'
            '123'
            ]

        text_by_zone = page.text_by_zone.get_text()

        for text_input_main_elements in text_input_main:

            page.input_space.send_keys(text_input_main_elements)
            page.submit_button.click(1)

            time.sleep(5)

            check.equal(page.text_results_search_domain_text.get_text(), text_input_main_elements + text_by_zone)
            page.go_back()


        # page.input_space.send_keys(input_text)
        # time.sleep(1)
        # page.submit_button.click()
        #
        # check.equal(page.domain_text.get_attribute('value'), input_text.lower())


    # check.equal(page.btn_headers_domain.get_text(), 'Домены', 'Тест локатора не равен ожидаймому результату')
    # check.is_true(page.btn_headers_mail.is_visible())

    # def test_headers(web_browser):
    #     """Этот тест проверяет хедер главной страницы"""
    #
    #     page = MainPage(web_browser)
    #
    #     check.equal(page.btn_headers_domain.get_text(), 'Домены', 'Тест локатора не равен ожидаемому результату')
    #     check.is_true(page.btn_headers_mail.is_visible())

    # @allure.story('Проверка главной страницы')
    # @allure.feature('Проверка строки поиска')
    # def test_headers(web_browser):
    #     """Этот тест проверяет строку поиска главной страницы"""
    #
    #     page = MainPage(web_browser)

    # elements_main_page = [
    #     (page.input_space, 'Введите домены')
    # ]
    #
    # for element, elements_text in elements_main_page:
    #     with allure.step('Проверка видимости строки поиска'):
    #         check.is_true(element.is_visible())
    #
    #     with allure.step('Сверка текста плейсхолдера'):
    #         check.equal(element.get_attribute('placeholder'), elements_text)

    # with allure.step('Проверка видимости строки и кнопки поиска'):
    #     check.is_true(page.input_space.is_visible())
    #     check.is_true(page.submit_button.is_visible())
    #
    # with allure.step('Сверка текста плейсхолдера'):
    #     check.equal(page.input_space.get_attribute('placeholder'), 'Введите домены')
    #
    # with allure.step('Проверка ввода с строку'):
    #     input_text = 'Тестирование'
    #     page.input_space.send_keys(input_text)
    #     time.sleep(1)
    #     page.submit_button.click()
    #
    #     check.equal(page.domain_text.get_attribute('value'), input_text.lower())
    #
    #     page.go_back()

    # дописать локаторы
    # with allure.step('Проверка домена и зоны'):
    #     text_input_main = [
    #         'hhh'
    #         '123'
    #         ]
    #
    #     text_by_zone = page.text_by_zone.get_text()
    #
    #     for text_input_main_elements in text_input_main:
    #
    #         page.input_space.send_keys(text_input_main_elements)
    #         page.submit_button.click(1)
    #
    #         time.sleep(5)
    #
    #         check.equal(page.text_results_search_domain_text.get_text(), text_input_main_elements + text_by_zone)
    #         page.go_back()

    # page.input_space.send_keys(input_text)
    # time.sleep(1)
    # page.submit_button.click()
    #
    # check.equal(page.domain_text.get_attribute('value'), input_text.lower())

    # check.equal(page.btn_headers_domain.get_text(), 'Домены', 'Тест локатора не равен ожидаймому результату')
    # check.is_true(page.btn_headers_mail.is_visible())