import random
import requests
import string
import locators.basic_functionality_locators
import locators.password_recovery_locators
import locators.personal_area_locators
import locators.section_order_feed_locators
import data.urls
import allure


@allure.step('Удаление пользователя по api')
def api_user_delete(token):
    headers = {
        'Authorization': f'{token}'
    }
    requests.delete(data.urls.url_for_delete, headers=headers)


@allure.step('Генерация данных для пользователя')
def generate_unique_data():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    user_data = []

    # генерируем емайл, пароль и имя
    email = generate_random_string(5) + '@' + generate_random_string(5) + '.ru'
    password = generate_random_string(10)
    name = generate_random_string(10)
    user_data.append(email)
    user_data.append(password)
    user_data.append(name)
    payload = {
        "email": f'{user_data[0]}',
        "password": f'{user_data[1]}',
        "name": f'{user_data[2]}'
    }
    return payload


@allure.step('Создание пользователя по api, логин и возврат токена для удаления')
def login_unique_user(driver):
    payload = generate_unique_data()
    response = requests.post(data.urls.url_for_register, data=payload)
    headers = response.json()['accessToken']
    data_user = payload
    token = headers
    user_email = data_user['email']
    user_password = data_user['password']
    driver.click_on_section(locators.personal_area_locators.personal_area)
    driver.wait_element_located(locators.personal_area_locators.entrance_text)
    driver.input_text(locators.personal_area_locators.string_input_email, user_email)
    driver.input_text(locators.personal_area_locators.string_input_password, user_password)
    driver.click_on_section(locators.personal_area_locators.entrance_button)
    return token
