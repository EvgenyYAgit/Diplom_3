import allure
from pages.basic_functionality_page import BasicFunctionalityPage
import data.variables
import data.helpers
import data.urls


class TestBasicFunctionality:

    @allure.title('Переход по клику на «Конструктор»')
    def test_click_constructor(self, driver):
        page = BasicFunctionalityPage(driver)
        page.go_to_site()
        page.click_on_order_feed()
        page.click_on_constructor()
        page.wait_text_assemble_burger()
        excepted = page.get_text_assemble_burger()
        assert data.variables.text_assemble_burger == excepted

    @allure.title('Переход по клику на «Лента заказов»')
    def test_click_order_feed(self, driver):
        page = BasicFunctionalityPage(driver)
        page.go_to_site()
        page.click_on_order_feed()
        page.wait_text_order_feed()
        excepted = page.get_text_order_feed()
        assert data.variables.text_order_feed == excepted

    @allure.title('Всплывающее окно с деталями')
    def test_popup_window_with_details(self, driver):
        page = BasicFunctionalityPage(driver)
        page.go_to_site()
        page.click_on_ingredient()
        page.wait_text_detail_ingredient()
        excepted = page.get_text_detail_ingredient()
        assert data.variables.text_ingredient_details == excepted

    @allure.title('Всплывающее окно закрыть кликом по крестику')
    def test_close_window_clicking_cross(self, driver):
        page = BasicFunctionalityPage(driver)
        page.go_to_site()
        page.click_on_ingredient()
        page.click_exit_button()
        page.wait_text_assemble_burger()
        excepted = page.get_text_assemble_burger()
        assert data.variables.text_assemble_burger == excepted

    @allure.title('Счётчик ингридиента увеличивается')
    def test_ingredient_counter_increases(self, driver):
        page = BasicFunctionalityPage(driver)
        page.go_to_site()
        page.drag_and_drop_ingredient()
        page.wait_text_counter_ingredient()
        excepted = page.get_text_counter_ingredient()
        assert data.variables.counter == excepted

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_logged_user_can_place_order(self, driver):
        page = BasicFunctionalityPage(driver)
        page.go_to_site()
        data_user = data.helpers.login_unique_user()
        data.helpers.login(page, data_user[1], data_user[2])
        page.click_order_button()
        excepted = page.get_text_cooking_order()
        data.helpers.api_user_delete(data_user[0])
        assert data.variables.text_order_being_prepared == excepted
