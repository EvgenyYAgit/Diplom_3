from pages.basic_page import BasePage
import data.urls
import allure
import locators.personal_area_locators


class PersonalArea(BasePage):

    @allure.step('Переход сайт бургеров')
    def go_to_site(self):
        self.get_site(data.urls.site)

    @allure.step('Ожидание и нажатие на Личный кабинет')
    def wait_and_click_personal_area(self):
        self.wait_and_click(locators.personal_area_locators.personal_area)

    @allure.step('Нажатие на Личный кабинет')
    def click_personal_area(self):
        self.wait_element_clickable(locators.personal_area_locators.personal_area)
        self.click_on_section(locators.personal_area_locators.personal_area)

    @allure.step('Нажатие на История заказов')
    def click_history_order_button(self):
        self.wait_element_clickable(locators.personal_area_locators.history_order_button)
        self.click_on_section(locators.personal_area_locators.history_order_button)

    @allure.step('Нажатие на Выход')
    def click_exit_button(self):
        self.wait_element_clickable(locators.personal_area_locators.exit_button)
        self.click_on_section(locators.personal_area_locators.exit_button)

    @allure.step('Ожидание текста Вход')
    def wait_text_entrance(self):
        self.wait_element_located(locators.personal_area_locators.entrance_text)

    @allure.step('Получить текст Вход')
    def get_text_entrance(self):
        text = self.get_text_of_element(locators.personal_area_locators.entrance_text)
        return text

    @allure.step('Получить текст История заказов')
    def get_text_history_order_button(self):
        text = self.get_text_of_element(locators.personal_area_locators.history_order_button)
        return text

    @allure.step('Ввод сообщения в строку input')
    def input_text(self, string, message):
        self.driver.find_element(*string).send_keys(message)
