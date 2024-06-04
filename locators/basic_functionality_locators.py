from selenium.webdriver.common.by import By
from locators.main_locators import MainLocators


class BasicFunctionalityLocators(MainLocators):
    # ингредиент булка
    ingredient_button = [By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']"]
    # детали ингредиента
    ingredient_text = [By.XPATH, "//h2[text()='Детали ингредиента']"]

    # кнопка закрыть окно ингредиента
    exit_button = [By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']/*[1]/*[2]"]
    # место куда перетягивать ингредиента
    place_for_ingredient = [By.XPATH, "//section[@class='BurgerConstructor_basket__29Cd7 mt-25 ']"]

    # счетчик ингредиента
    counter_ingredient = [By.XPATH, "//ul[1]/a[1]//p[@class='counter_counter__num__3nue1']"]

    # текст начала готовки заказа
    cook_start_text = [By.XPATH, "//p[text()='Ваш заказ начали готовить']"]
