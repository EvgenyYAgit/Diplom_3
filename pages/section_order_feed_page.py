from pages.basic_page import BasePage
import data.urls
import allure
import locators.section_order_feed_locators
import locators.basic_functionality_locators
import locators.personal_area_locators
import data.variables


class SectionOrderFeed(BasePage):
    @allure.step('Переход сайт бургеров')
    def go_to_site(self):
        self.get_site(data.urls.site)

    @allure.step('Нажатие на Ленту заказов')
    def click_order_feed_button(self):
        self.wait_element_clickable(locators.section_order_feed_locators.order_feed_button)
        self.click_on_section(locators.section_order_feed_locators.order_feed_button)

    @allure.step('Нажатие на первый заказ в ленте')
    def click_first_order(self):
        self.wait_element_clickable(locators.section_order_feed_locators.first_order)
        self.click_on_section(locators.section_order_feed_locators.first_order)

    @allure.step('Нажатие на Оформить заказ')
    def click_order_button(self):
        self.wait_element_clickable(locators.section_order_feed_locators.order_button)
        self.click_on_section(locators.section_order_feed_locators.order_button)

    @allure.step('Нажатие на закрыть окно')
    def click_close_window_order(self):
        self.wait_element_clickable(locators.section_order_feed_locators.close_window_order)
        self.click_on_section(locators.section_order_feed_locators.close_window_order)

    @allure.step('Нажатие на Историю заказов')
    def click_history_order_button(self):
        self.wait_element_clickable(locators.section_order_feed_locators.history_order_button)
        self.click_on_section(locators.section_order_feed_locators.history_order_button)

    @allure.step('Ожидание и нажатие на Личный кабинет')
    def wait_and_click_personal_area(self):
        self.wait_and_click(locators.personal_area_locators.personal_area)

    @allure.step('Нажатие на Личный кабинет')
    def click_personal_area(self):
        self.wait_element_clickable(locators.personal_area_locators.personal_area)
        self.click_on_section(locators.personal_area_locators.personal_area)

    @allure.step('Нажатие на Конструктор')
    def click_constructor_button(self):
        self.wait_element_clickable(locators.section_order_feed_locators.constructor_button)
        self.click_on_section(locators.section_order_feed_locators.constructor_button)

    @allure.step('Ожидание текста Лента заказов')
    def wait_text_order_feed_text(self):
        self.wait_element_located(locators.section_order_feed_locators.order_feed_text)

    @allure.step('Ожидание текста Соберите бургер')
    def wait_text_assemble_the_burger_text(self):
        self.wait_element_located(locators.section_order_feed_locators.assemble_the_burger_text)

    @allure.step('Ожидание текста Состав')
    def wait_text_contents_order(self):
        self.wait_element_located(locators.section_order_feed_locators.contents_order)

    @allure.step('Ожидание кликабельного текста заказа')
    def wait_clickable_order_text(self):
        self.wait_element_clickable(locators.section_order_feed_locators.order_text)

    @allure.step('Получить текст Состав')
    def get_text_contents_order(self):
        text = self.get_text_of_element(locators.section_order_feed_locators.contents_order)
        return text

    @allure.step('Получить текст заказа')
    def get_order_text(self):
        text = self.get_text_of_element(locators.section_order_feed_locators.order_text)
        return text

    @allure.step('Получить текст Выполнено за все время')
    def get_text_counter_order_all_time(self):
        text = self.get_text_of_element(locators.section_order_feed_locators.counter_order_all_time)
        return text

    @allure.step('Получить текст Выполнено за сегодня')
    def get_text_counter_order_today(self):
        text = self.get_text_of_element(locators.section_order_feed_locators.counter_order_today)
        return text

    @allure.step('Получить текст элемента заказа в работе')
    def get_text_in_work_order(self):
        text = self.get_text_of_element(locators.section_order_feed_locators.in_work_order)
        return text

    @allure.step('Перенос элемента ингредиента')
    def drag_and_drop_ingredient(self):
        self.drag_and_drop_element(locators.basic_functionality_locators.ingredient_button,
                                   locators.basic_functionality_locators.place_for_ingredient)

    @allure.step('Ожидание изменения номера заказа')
    def wait_another_number_order(self):
        new_text = self.wait_another_text(locators.section_order_feed_locators.number_order,
                                          data.variables.default_number)
        return new_text

    @allure.step('Получить текст списка готовых заказов')
    def get_text_list_ready_order(self):
        text = self.get_text_list(locators.section_order_feed_locators.list_ready_order)
        return text

    @allure.step('Ожидание видимости элемента')
    def wait_element_visible(self, text):
        self.wait_element_will_be_visible(locators.section_order_feed_locators.in_work_order, text)
