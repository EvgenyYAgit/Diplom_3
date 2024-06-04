import data.urls
import allure
import locators.basic_functionality_locators
from pages.basic_page import BasePage


class BasicFunctionalityPage(BasePage):
    basic = locators.basic_functionality_locators

    @allure.step('Переход сайт бургеров')
    def go_to_site(self):
        self.get_site(data.urls.site)

    @allure.step('Переход в Ленту заказов')
    def click_on_order_feed(self):
        self.wait_element_clickable(self.basic.order_feed_button)
        self.click_on_section(self.basic.order_feed_button)

    @allure.step('Переход в Конструктор')
    def click_on_constructor(self):
        self.wait_element_clickable(self.basic.constructor_button)
        self.click_on_section(self.basic.constructor_button)

    @allure.step('Нажатие на ингридиент')
    def click_on_ingredient(self):
        self.wait_element_clickable(self.basic.ingredient_button)
        self.click_on_section(self.basic.ingredient_button)

    @allure.step('Нажатие на кнопку закрытия')
    def click_exit_button(self):
        self.wait_element_clickable(self.basic.exit_button)
        self.click_on_section(self.basic.exit_button)

    @allure.step('Нажатие на кнопку Оформить заказ')
    def click_order_button(self):
        self.wait_element_clickable(self.basic.order_button)
        self.click_on_section(self.basic.order_button)

    @allure.step('Ожидание текста Соберите бургер')
    def wait_text_assemble_burger(self):
        self.wait_element_located(self.basic.assemble_the_burger_text)

    @allure.step('Ожидание текста Лента заказов')
    def wait_text_order_feed(self):
        self.wait_element_located(self.basic.order_feed_text)

    @allure.step('Ожидание текста Детали ингредиента')
    def wait_text_detail_ingredient(self):
        self.wait_element_located(self.basic.ingredient_text)

    @allure.step('Ожидание текста счетчика ингредиента')
    def wait_text_counter_ingredient(self):
        self.wait_element_located(self.basic.counter_ingredient)

    @allure.step('Ожидание текста Ваш заказ начали готовить')
    def wait_text_cooking_order(self):
        self.wait_element_located(self.basic.cook_start_text)

    @allure.step('Получить текст Соберите бургер')
    def get_text_assemble_burger(self):
        text = self.get_text_of_element(self.basic.assemble_the_burger_text)
        return text

    @allure.step('Получить текст Лента заказов')
    def get_text_order_feed(self):
        text = self.get_text_of_element(self.basic.order_feed_text)
        return text

    @allure.step('Получить текст Детали ингредиента')
    def get_text_detail_ingredient(self):
        text = self.get_text_of_element(self.basic.ingredient_text)
        return text

    @allure.step('Получить текст счетчика ингредиента')
    def get_text_counter_ingredient(self):
        text = self.get_text_of_element(self.basic.counter_ingredient)
        return text

    @allure.step('Получить текст Ваш заказ начали готовить')
    def get_text_cooking_order(self):
        text = self.get_text_of_element(self.basic.cook_start_text)
        return text

    @allure.step('Перенос элемента ингредиента')
    def drag_and_drop_ingredient(self):
        self.drag_and_drop_element(self.basic.ingredient_button,
                                   self.basic.place_for_ingredient)
