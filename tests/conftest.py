import pytest
import requests
import random
import string
import time

from selenium import webdriver
from data import CommonData

from pages.main_page import MainPage
from pages.login_page import LoginPage

from locators.locators import MainPageLocators as Mpl
from locators.locators import LoginPageLocators as Lpl


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {request.param}")

    driver.get(CommonData.main_url)
    yield driver
    driver.quit()


@pytest.fixture()
def get_forgot_pass_page(driver):
    main_page = MainPage(driver)
    main_page.click_element(Mpl.account_button_header)
    login_page = LoginPage(driver)
    login_page.scroll_and_click(Lpl.forgot_password_button_login)


@pytest.fixture()
def create_user_and_sign_in(driver):
    letters = string.ascii_lowercase
    login = ''.join(random.choice(letters) for _ in range(10)) + '@ya.ru'
    payload = {"email": f'{login}',
               "password": CommonData.test_user_password,
               "name": CommonData.test_user_name
               }
    response = requests.post(CommonData.register_url, data=payload)
    access_token = ''
    if response.status_code == 200:
        access_token = response.json().get("accessToken")

    main_page = MainPage(driver)
    main_page.click_element(Mpl.account_button_header)
    login_page = LoginPage(driver)
    login_page.send_user_data(Lpl.email_input_field, login)
    login_page.send_user_data(Lpl.password_input_field, CommonData.test_user_password)
    login_page.click_element(Lpl.sign_in_button)
    yield
    headers = {'Authorization': f'{access_token}'}
    requests.delete(CommonData.delete_user_url, headers=headers)


@pytest.fixture()
def create_new_order_and_get_its_number(driver):
    main_page = MainPage(driver)
    main_page.click_element(Mpl.constructor_button_header)
    main_page.drag_and_drop_element(Mpl.ingredient_name, Mpl.constructor_upper_bun_placeholder)
    main_page.drag_and_drop_element(Mpl.fluoric_bun_name, Mpl.constructor_upper_bun_placeholder)
    main_page.click_element(Mpl.place_order_button)
    time.sleep(1)  # Здесь добавлено ожидание загрузки ответа сервера с номером оформленного заказа
    order_number = main_page.get_text_element(Mpl.order_number)
    main_page.click_element(Mpl.order_number_window_close_button)
    return order_number
