import allure
from pages.password_recovery_page import PasswordRecoveryPage
import data.variables
import data.helpers
import data.urls


class TestPasswordRecovery:

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_recovery_page(self, driver):
        page = PasswordRecoveryPage(driver)
        page.go_to_site()
        page.click_login()
        page.click_restore_password()
        excepted = page.get_text_restore_password()
        assert data.variables.text_password_recovery == excepted

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_click_on_restore_button(self, driver):
        page = PasswordRecoveryPage(driver)
        page.go_to_site()
        page.click_login()
        page.click_restore_password()
        page.input_password_text()
        page.click_restore_button()
        page.wait_save_button()
        excepted = page.get_text_save_button()
        assert data.variables.text_save == excepted

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_password_field_highlighting(self, driver):
        page = PasswordRecoveryPage(driver)
        page.go_to_site()
        page.click_login()
        page.wait_clickable_restore_password()
        page.click_eya_password()
        excepted = page.get_text_area_light_password()
        assert data.variables.text_password == excepted
