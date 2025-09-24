from pages.basic_page import BasePage
import data.urls
import allure
import locators.section_order_feed_locators
import locators.basic_functionality_locators
import locators.personal_area_locators
import data.variables


class SectionOrderFeed(BasePage):
    section = locators.section_order_feed_locators.SectionOrderFeedLocators
    basic = locators.basic_functionality_locators.BasicFunctionalityLocators
    area = locators.personal_area_locators.PersonalAreaLocators

    @allure.step('Переход сайт бургеров')
    def go_to_site(self):
        self.get_site(data.urls.site)

    @allure.step('Нажатие на Ленту заказов')
    def click_order_feed_button(self):
        self.wait_element_clickable(self.section.order_feed_button)
        self.click_on_section(self.section.order_feed_button)

    @allure.step('Нажатие на первый заказ в ленте')
    def click_first_order(self):
        self.wait_element_clickable(self.section.first_order)
        self.click_on_section(self.section.first_order)

    @allure.step('Нажатие на Оформить заказ')
    def click_order_button(self):
        self.wait_element_clickable(self.section.order_button)
        self.click_on_section(self.section.order_button)

    @allure.step('Нажатие на закрыть окно')
    def click_close_window_order(self):
        self.wait_element_clickable(self.section.close_window_order)
        self.click_on_section(self.section.close_window_order)

    @allure.step('Нажатие на Историю заказов')
    def click_history_order_button(self):
        self.wait_element_clickable(self.section.history_order_button)
        self.click_on_section(self.section.history_order_button)

    @allure.step('Нажатие на Личный кабинет')
    def click_personal_area(self):
        self.wait_element_clickable(self.area.personal_area)
        self.click_on_section(self.area.personal_area)

    @allure.step('Нажатие на Конструктор')
    def click_constructor_button(self):
        self.wait_element_clickable(self.section.constructor_button)
        self.click_on_section(self.section.constructor_button)

    @allure.step('Ожидание текста Лента заказов')
    def wait_text_order_feed_text(self):
        self.wait_element_located(self.section.order_feed_text)

    @allure.step('Ожидание текста Соберите бургер')
    def wait_text_assemble_the_burger_text(self):
        self.wait_element_located(self.section.assemble_the_burger_text)

    @allure.step('Ожидание текста Состав')
    def wait_text_contents_order(self):
        self.wait_element_located(self.section.contents_order)

    @allure.step('Ожидание кликабельного текста заказа')
    def wait_clickable_order_text(self):
        self.wait_element_clickable(self.section.order_text)

    @allure.step('Получить текст Состав')
    def get_text_contents_order(self):
        text = self.get_text_of_element(self.section.contents_order)
        return text

    @allure.step('Получить текст заказа')
    def get_order_text(self):
        text = self.get_text_of_element(self.section.order_text)
        return text

    @allure.step('Получить текст Выполнено за все время')
    def get_text_counter_order_all_time(self):
        text = self.get_text_of_element(self.section.counter_order_all_time)
        return text

    @allure.step('Получить текст Выполнено за сегодня')
    def get_text_counter_order_today(self):
        text = self.get_text_of_element(self.section.counter_order_today)
        return text

    @allure.step('Получить текст элемента заказа в работе')
    def get_text_in_work_order(self):
        text = self.get_text_of_element(self.section.in_work_order)
        return text

    @allure.step('Перенос элемента ингредиента')
    def drag_and_drop_ingredient(self):
        self.drag_and_drop_element(self.basic.ingredient_button,
                                   self.basic.place_for_ingredient)

    @allure.step('Ожидание изменения номера заказа')
    def wait_another_number_order(self):
        new_text = self.wait_another_text(self.section.number_order,
                                          data.variables.default_number)
        return new_text

    @allure.step('Получить текст списка готовых заказов')
    def get_text_list_ready_order(self):
        text = self.get_text_list(self.section.list_ready_order)
        return text

    @allure.step('Ожидание видимости элемента')
    def wait_element_visible(self, text):
        self.wait_element_will_be_visible(self.section.in_work_order, text)
