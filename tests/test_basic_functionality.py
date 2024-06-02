import allure
from pages.home_page import HomePage
import data.variables
import data.data
import data.urls
import locators.basic_functionality_locators
import locators.personal_area_locators


class TestBasicFunctionality:

    @allure.title('Переход по клику на «Конструктор»')
    def test_click_constructor(self, driver):
        some_object = HomePage(driver)
        some_object.get_site(data.urls.site)
        some_object.wait_element_clickable(locators.basic_functionality_locators.order_feed_button)
        some_object.click_on_section(locators.basic_functionality_locators.order_feed_button)
        some_object.click_on_section(locators.basic_functionality_locators.constructor_button)
        some_object.wait_element_located(locators.basic_functionality_locators.assemble_the_burger_text)
        assert data.variables.text_assemble_burger == some_object.get_text_of_element(
            locators.basic_functionality_locators.assemble_the_burger_text)

    @allure.title('Переход по клику на «Лента заказов»')
    def test_click_order_feed(self, driver):
        some_object = HomePage(driver)
        some_object.get_site(data.urls.site)
        some_object.wait_element_clickable(locators.basic_functionality_locators.order_feed_button)
        some_object.click_on_section(locators.basic_functionality_locators.order_feed_button)
        some_object.wait_element_located(locators.basic_functionality_locators.order_feed_text)
        assert data.variables.text_order_feed == some_object.get_text_of_element(
            locators.basic_functionality_locators.order_feed_text)

    @allure.title('Всплывающее окно с деталями')
    def test_popup_window_with_details(self, driver):
        some_object = HomePage(driver)
        some_object.get_site(data.urls.site)
        some_object.wait_element_clickable(locators.basic_functionality_locators.ingredient_button)
        some_object.click_on_section(locators.basic_functionality_locators.ingredient_button)
        some_object.wait_element_located(locators.basic_functionality_locators.ingredient_text)
        assert data.variables.text_ingredient_details == some_object.get_text_of_element(
            locators.basic_functionality_locators.ingredient_text)

    @allure.title('Всплывающее окно закрыть кликом по крестику')
    def test_close_window_clicking_cross(self, driver):
        some_object = HomePage(driver)
        some_object.get_site(data.urls.site)
        some_object.wait_element_clickable(locators.basic_functionality_locators.ingredient_button)
        some_object.click_on_section(locators.basic_functionality_locators.ingredient_button)
        some_object.wait_element_located(locators.basic_functionality_locators.ingredient_text)
        some_object.click_on_section(locators.basic_functionality_locators.exit_button)
        some_object.wait_element_located(locators.basic_functionality_locators.assemble_the_burger_text)
        assert data.variables.text_assemble_burger == some_object.get_text_of_element(
            locators.basic_functionality_locators.assemble_the_burger_text)

    @allure.title('Счётчик ингридиента увеличивается')
    def test_ingredient_counter_increases(self, driver):
        some_object = HomePage(driver)
        some_object.get_site(data.urls.site)
        some_object.drag_and_drop_element(locators.basic_functionality_locators.ingredient_button,
                                          locators.basic_functionality_locators.place_for_ingredient)
        some_object.wait_element_located(locators.basic_functionality_locators.ingredient_elements)
        assert data.variables.counter == some_object.get_text_of_element(
            locators.basic_functionality_locators.ingredient_elements)

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_logged_user_can_place_order(self, driver):
        some_object = HomePage(driver)
        some_object.get_site(data.urls.site)
        # создается пользователь по апи и передается токен
        token = data.data.login_unique_user(driver)
        some_object.wait_element_clickable(locators.basic_functionality_locators.order_button)
        some_object.click_on_section(locators.basic_functionality_locators.order_button)
        some_object.wait_element_located(locators.basic_functionality_locators.cook_start_text)
        excepted = some_object.get_text_of_element(locators.basic_functionality_locators.cook_start_text)
        # передается токен и удаляется пользователь
        data.data.api_user_delete(token)
        assert data.variables.text_order_being_prepared == excepted
