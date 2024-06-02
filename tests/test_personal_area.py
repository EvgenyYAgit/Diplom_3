import locators.personal_area_locators
import allure
import data.helpers
import data.urls
from pages.home_page import HomePage
import data.variables


class TestPersonalArea:
    @allure.title('Переход в «Личный кабинет»')
    def test_go_personal_account(self, driver):
        some_object = HomePage(driver)
        some_object.get_site(data.urls.site)
        some_object.wait_element_clickable(locators.personal_area_locators.personal_area)
        some_object.click_on_section(locators.personal_area_locators.personal_area)
        some_object.wait_element_located(locators.personal_area_locators.entrance_text)
        assert data.variables.text_entrance == some_object.get_text_of_element(
            locators.personal_area_locators.entrance_text)

    @allure.title('Переход в раздел «История заказов»')
    def test_go_order_history_section(self, driver):
        some_object = HomePage(driver)
        some_object.get_site(data.urls.site)
        # создается пользователь по апи и передается токен
        token = data.helpers.login_unique_user(some_object)
        some_object.wait_element_clickable(locators.personal_area_locators.personal_area)
        some_object.click_on_section(locators.personal_area_locators.personal_area)
        some_object.wait_element_clickable(locators.personal_area_locators.history_order_button)
        some_object.click_on_section(locators.personal_area_locators.history_order_button)
        excepted = some_object.get_text_of_element(locators.personal_area_locators.history_order_button)
        # передается токен и удаляется пользователь
        data.helpers.api_user_delete(token)
        assert data.variables.text_history_orders == excepted

    @allure.title('Выход из аккаунта')
    def test_log_out(self, driver):
        some_object = HomePage(driver)
        some_object.get_site(data.urls.site)
        # создается пользователь по апи и передается токен
        token = data.helpers.login_unique_user(some_object)
        some_object.wait_element_clickable(locators.personal_area_locators.personal_area)
        some_object.click_on_section(locators.personal_area_locators.personal_area)
        some_object.wait_element_clickable(locators.personal_area_locators.exit_button)
        some_object.click_on_section(locators.personal_area_locators.exit_button)
        some_object.wait_element_located(locators.personal_area_locators.enter_text)
        excepted = some_object.get_text_of_element(locators.personal_area_locators.enter_text)
        # передается токен и удаляется пользователь
        data.helpers.api_user_delete(token)
        assert data.variables.text_entrance == excepted
