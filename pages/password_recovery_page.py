from pages.basic_page import BasePage
import data.urls
import allure
import locators.password_recovery_locators
import data.variables


class PasswordRecoveryPage(BasePage):
    recovery = locators.password_recovery_locators.PasswordRecoveryLocators

    @allure.step('Переход сайт бургеров')
    def go_to_site(self):
        self.get_site(data.urls.site)

    @allure.step('Нажатие на Войти в аккаунт')
    def click_login(self):
        self.click_on_section(self.recovery.login_button)

    @allure.step('Нажатие на Восстановить пароль')
    def click_restore_password(self):
        self.wait_element_clickable(self.recovery.restore_password)
        self.click_on_section(self.recovery.restore_password)

    @allure.step('Нажатие на Восстановить')
    def click_restore_button(self):
        self.wait_element_clickable(self.recovery.restore_button)
        self.click_on_section(self.recovery.restore_button)

    @allure.step('Нажатие на Сохранить')
    def click_save_button(self):
        self.wait_element_clickable(self.recovery.save_button)
        self.click_on_section(self.recovery.save_button)

    @allure.step('Нажатие на глазок')
    def click_eya_password(self):
        self.click_on_section(self.recovery.eya_password)

    @allure.step('Получить текст Восстановление пароля')
    def get_text_restore_password(self):
        text = self.get_text_of_element(self.recovery.text_restore_password)
        return text

    @allure.step('Получить текст Сохранить')
    def get_text_save_button(self):
        text = self.get_text_of_element(self.recovery.save_button)
        return text

    @allure.step('Получить текст подсвеченной области')
    def get_text_area_light_password(self):
        text = self.get_text_of_element(self.recovery.area_light_password)
        return text

    @allure.step('Ожидание кликабельной кнопки Сохранить')
    def wait_save_button(self):
        self.wait_element_clickable(self.recovery.save_button)

    @allure.step('Ожидание кликабельной кнопки Восстановить пароль')
    def wait_clickable_restore_password(self):
        self.wait_element_clickable(self.recovery.restore_password)

    @allure.step('Ввод пароля')
    def input_password_text(self):
        self.input_text(self.recovery.string_input_email, data.variables.password_for_recovery)
