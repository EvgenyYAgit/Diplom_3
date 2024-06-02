import allure
from pages.home_page import HomePage
import data.variables
import data.helpers
import data.urls
import locators.password_recovery_locators


class TestPasswordRecovery:

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_recovery_page(self, driver):
        some_object = HomePage(driver)
        some_object.get_site(data.urls.site)
        some_object.click_on_section(locators.password_recovery_locators.login_button)
        some_object.wait_element_clickable(locators.password_recovery_locators.restore_password)
        some_object.click_on_section(locators.password_recovery_locators.restore_password)
        assert data.variables.text_password_recovery == some_object.get_text_of_element(
            locators.password_recovery_locators.text_restore_password)

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_click_on_restore_button(self, driver):
        some_object = HomePage(driver)
        some_object.get_site(data.urls.site)
        some_object.click_on_section(locators.password_recovery_locators.login_button)
        some_object.wait_element_clickable(locators.password_recovery_locators.restore_password)
        some_object.click_on_section(locators.password_recovery_locators.restore_password)
        some_object.input_text(locators.password_recovery_locators.string_input_email,
                               data.variables.password_for_recovery)
        some_object.click_on_section(locators.password_recovery_locators.restore_button)
        some_object.wait_element_clickable(locators.password_recovery_locators.save_button)
        assert data.variables.text_save == some_object.get_text_of_element(
            locators.password_recovery_locators.save_button)

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_password_field_highlighting(self, driver):
        some_object = HomePage(driver)
        some_object.get_site(data.urls.site)
        some_object.wait_element_clickable(locators.password_recovery_locators.login_button)
        some_object.click_on_section(locators.password_recovery_locators.login_button)
        some_object.wait_element_clickable(locators.password_recovery_locators.restore_password)
        some_object.click_on_section(locators.password_recovery_locators.eya_password)
        assert data.variables.text_password == some_object.get_text_of_element(
            locators.password_recovery_locators.area_light_password)
