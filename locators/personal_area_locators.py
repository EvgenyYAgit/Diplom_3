from selenium.webdriver.common.by import By
from locators.main_locators import MainLocators


class PersonalAreaLocators(MainLocators):
    # текст вход
    entrance_text = [By.XPATH, "//h2[text()='Вход']"]

    # строка ввода емайл
    string_input_email = [By.XPATH, "//input[@type='text']"]
    # строка ввода пароль
    string_input_password = [By.XPATH, "//input[@type='password']"]
    # кнопка войти
    entrance_button = [By.XPATH, "//button[text()='Войти']"]

    # кнопка история заказов
    history_order_button = [By.XPATH, "//a[text()='История заказов']"]
    # заказ из истории заказов
    my_order = [By.XPATH, "//h2[text()='Люминесцентный space краторный бургер']"]

    # кнопка выход
    exit_button = [By.XPATH, "//button[text()='Выход']"]
