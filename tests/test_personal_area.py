import allure
import data.helpers
import data.urls
from pages.personal_area_page import PersonalArea
import data.variables


class TestPersonalArea:
    @allure.title('Переход в «Личный кабинет»')
    def test_go_personal_account(self, driver):
        page = PersonalArea(driver)
        page.go_to_site()
        page.click_personal_area()
        page.wait_text_entrance()
        excepted = page.get_text_entrance()
        assert data.variables.text_entrance == excepted

    @allure.title('Переход в раздел «История заказов»')
    def test_go_order_history_section(self, driver):
        page = PersonalArea(driver)
        page.go_to_site()
        data_user = data.helpers.login_unique_user()
        data.helpers.login(page, data_user[1], data_user[2])
        page.click_personal_area()
        page.click_history_order_button()
        excepted = page.get_text_history_order_button()
        data.helpers.api_user_delete(data_user[0])
        assert data.variables.text_history_orders == excepted

    @allure.title('Выход из аккаунта')
    def test_log_out(self, driver):
        page = PersonalArea(driver)
        page.go_to_site()
        data_user = data.helpers.login_unique_user()
        data.helpers.login(page, data_user[1], data_user[2])
        page.click_personal_area()
        page.click_exit_button()
        page.wait_text_entrance()
        excepted = page.get_text_entrance()
        data.helpers.api_user_delete(data_user[0])
        assert data.variables.text_entrance == excepted
