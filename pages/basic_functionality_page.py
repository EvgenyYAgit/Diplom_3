import locators.personal_area_locators
import data.urls
import allure
import locators
from seletools.actions import drag_and_drop
from pages.basic_page import BasePage


class BasicFunctionalityPage(BasePage):

    @allure.step('Переход сайт бургеров')
    def go_to_site(self):
        self.get_site(data.urls.site)

    @allure.step('Переход в Ленту заказов')
    def click_on_order_feed(self):
        self.wait_element_clickable(locators.basic_functionality_locators.order_feed_button)
        self.click_on_section(locators.basic_functionality_locators.order_feed_button)

    @allure.step('Переход в Конструктор')
    def click_on_constructor(self):
        self.wait_element_clickable(locators.basic_functionality_locators.constructor_button)
        self.click_on_section(locators.basic_functionality_locators.constructor_button)

    @allure.step('Нажатие на ингридиент')
    def click_on_ingredient(self):
        self.wait_element_clickable(locators.basic_functionality_locators.ingredient_button)
        self.click_on_section(locators.basic_functionality_locators.ingredient_button)

    @allure.step('Нажатие на кнопку закрытия')
    def click_exit_button(self):
        self.wait_element_clickable(locators.basic_functionality_locators.exit_button)
        self.click_on_section(locators.basic_functionality_locators.exit_button)

    @allure.step('Нажатие на кнопку Оформить заказ')
    def click_order_button(self):
        self.wait_element_clickable(locators.basic_functionality_locators.order_button)
        self.click_on_section(locators.basic_functionality_locators.order_button)

    @allure.step('Ожидание текста Соберите бургер')
    def wait_text_assemble_burger(self):
        self.wait_element_located(locators.basic_functionality_locators.assemble_the_burger_text)

    @allure.step('Ожидание текста Лента заказов')
    def wait_text_order_feed(self):
        self.wait_element_located(locators.basic_functionality_locators.order_feed_text)

    @allure.step('Ожидание текста Детали ингредиента')
    def wait_text_detail_ingredient(self):
        self.wait_element_located(locators.basic_functionality_locators.ingredient_text)

    @allure.step('Ожидание текста счетчика ингредиента')
    def wait_text_counter_ingredient(self):
        self.wait_element_located(locators.basic_functionality_locators.counter_ingredient)

    @allure.step('Ожидание текста Ваш заказ начали готовить')
    def wait_text_cooking_order(self):
        self.wait_element_located(locators.basic_functionality_locators.cook_start_text)

    @allure.step('Получить текст Соберите бургер')
    def get_text_assemble_burger(self):
        text = self.get_text_of_element(locators.basic_functionality_locators.assemble_the_burger_text)
        return text

    @allure.step('Получить текст Лента заказов')
    def get_text_order_feed(self):
        text = self.get_text_of_element(locators.basic_functionality_locators.order_feed_text)
        return text

    @allure.step('Получить текст Детали ингредиента')
    def get_text_detail_ingredient(self):
        text = self.get_text_of_element(locators.basic_functionality_locators.ingredient_text)
        return text

    @allure.step('Получить текст счетчика ингредиента')
    def get_text_counter_ingredient(self):
        text = self.get_text_of_element(locators.basic_functionality_locators.counter_ingredient)
        return text

    @allure.step('Получить текст Ваш заказ начали готовить')
    def get_text_cooking_order(self):
        text = self.get_text_of_element(locators.basic_functionality_locators.cook_start_text)
        return text

    @allure.step('Перенос элемента')
    def drag_and_drop_element(self):
        source = self.driver.find_element(*locators.basic_functionality_locators.ingredient_button)
        target = self.driver.find_element(*locators.basic_functionality_locators.place_for_ingredient)
        drag_and_drop(self.driver, source, target)

    @allure.step('Ввод сообщения в строку input')
    def input_text(self, string, message):
        self.driver.find_element(*string).send_keys(message)
