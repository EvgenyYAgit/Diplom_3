from selenium.webdriver.common.by import By


class MainLocators:
    # кнопка личный кабинет
    personal_area = [By.XPATH, "//p[text()='Личный Кабинет']"]
    # текст соберите бургер
    assemble_the_burger_text = [By.XPATH, "//h1[text()='Соберите бургер']"]
    # кнопка конструктор
    constructor_button = [By.XPATH, "//p[text()='Конструктор']"]
    # кнопка лента заказов
    order_feed_button = [By.XPATH, "//p[text()='Лента Заказов']"]
    # кнопка оформления заказа
    order_button = [By.XPATH, "//button[text()='Оформить заказ']"]
    # кнопка войти в аккаунт
    login_button = [By.XPATH, "//button[text()='Войти в аккаунт']"]
    # текст лента заказов
    order_feed_text = [By.XPATH, "//h1[text()='Лента заказов']"]
