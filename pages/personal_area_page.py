from pages.basic_page import BasePage
import data.urls
import allure
import locators.personal_area_locators


class PersonalArea(BasePage):
    area = locators.personal_area_locators

    @allure.step('Переход сайт бургеров')
    def go_to_site(self):
        self.get_site(data.urls.site)

    @allure.step('Нажатие на Личный кабинет')
    def click_personal_area(self):
        self.wait_element_clickable(self.area.personal_area)
        self.click_on_section(self.area.personal_area)

    @allure.step('Нажатие на История заказов')
    def click_history_order_button(self):
        self.wait_element_clickable(self.area.history_order_button)
        self.click_on_section(self.area.history_order_button)

    @allure.step('Нажатие на Выход')
    def click_exit_button(self):
        self.wait_element_clickable(self.area.exit_button)
        self.click_on_section(self.area.exit_button)

    @allure.step('Ожидание текста Вход')
    def wait_text_entrance(self):
        self.wait_element_located(self.area.entrance_text)

    @allure.step('Получить текст Вход')
    def get_text_entrance(self):
        text = self.get_text_of_element(self.area.entrance_text)
        return text

    @allure.step('Получить текст История заказов')
    def get_text_history_order_button(self):
        text = self.get_text_of_element(self.area.history_order_button)
        return text
