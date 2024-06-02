import allure
from pages.home_page import HomePage
import data.variables
import data.data
import data.urls
import locators.section_order_feed_locators
import locators.personal_area_locators
import locators.basic_functionality_locators


class TestSectionOrderFeed:

    @allure.title('Всплывающее окно с деталями заказа')
    def test_pop_up_window_order_details(self, driver):
        some_object = HomePage(driver)
        some_object.get_site(data.urls.site)
        some_object.click_on_section(locators.section_order_feed_locators.order_feed_button)
        some_object.wait_element_located(locators.section_order_feed_locators.order_feed_text)
        some_object.click_on_section(locators.section_order_feed_locators.first_order)
        some_object.wait_element_located(locators.section_order_feed_locators.contents_order)
        assert data.variables.text_composition == some_object.get_text_of_element(
            locators.section_order_feed_locators.contents_order)

    @allure.title('Заказы из «История заказов» отображаются на странице «Лента заказов»')
    def test_same_orders_in_different_places(self, driver):
        some_object = HomePage(driver)
        some_object.get_site(data.urls.site)
        # создание уникального пользователя, логин и возвращение токена
        token = data.data.login_unique_user(some_object)
        some_object.wait_element_located(locators.section_order_feed_locators.assemble_the_burger_text)
        some_object.drag_and_drop_element(locators.basic_functionality_locators.ingredient_button,
                                          locators.basic_functionality_locators.place_for_ingredient)
        some_object.click_on_section(locators.basic_functionality_locators.order_button)
        some_object.wait_element_clickable(locators.section_order_feed_locators.close_window_order)
        some_object.wait_another_text(locators.section_order_feed_locators.number_order, data.variables.default_number)
        some_object.click_on_section(locators.section_order_feed_locators.close_window_order)
        some_object.wait_element_clickable(locators.section_order_feed_locators.order_feed_button)
        some_object.click_on_section(locators.section_order_feed_locators.order_feed_button)
        some_object.wait_element_located(locators.section_order_feed_locators.order_feed_text)
        some_object.wait_element_clickable(locators.personal_area_locators.personal_area)
        some_object.click_on_section(locators.personal_area_locators.personal_area)
        some_object.wait_element_clickable(locators.section_order_feed_locators.history_order_button)
        some_object.click_on_section(locators.section_order_feed_locators.history_order_button)
        some_object.wait_element_clickable(locators.section_order_feed_locators.order_text)
        number_order = some_object.get_text_of_element(locators.section_order_feed_locators.order_text)
        some_object.click_on_section(locators.basic_functionality_locators.order_feed_button)
        some_object.wait_element_located(locators.basic_functionality_locators.order_feed_text)
        list_orders = some_object.get_text_of_elements(locators.section_order_feed_locators.list_ready_order)
        list_number_orders = [list_orders.text for list_orders in list_orders]
        data.data.api_user_delete(token)
        assert number_order[1:] in list_number_orders

    @allure.title('Счётчик "Выполнено за всё время" увеличивается при новом заказе')
    def test_the_counter_increases_new_order_all_time(self, driver):
        some_object = HomePage(driver)
        some_object.get_site(data.urls.site)
        some_object.click_on_section(locators.section_order_feed_locators.order_feed_button)
        some_object.wait_element_located(locators.section_order_feed_locators.order_feed_text)
        all_time = some_object.get_text_of_element(locators.section_order_feed_locators.counter_order_all_time)
        # создание уникального пользователя, логин и возвращение токена
        token = data.data.login_unique_user(some_object)
        some_object.wait_element_located(locators.section_order_feed_locators.assemble_the_burger_text)
        some_object.drag_and_drop_element(locators.basic_functionality_locators.ingredient_button,
                                          locators.basic_functionality_locators.place_for_ingredient)
        some_object.click_on_section(locators.basic_functionality_locators.order_button)
        some_object.wait_element_clickable(locators.section_order_feed_locators.close_window_order)
        some_object.wait_another_text(locators.section_order_feed_locators.number_order, data.variables.default_number)
        some_object.click_on_section(locators.section_order_feed_locators.close_window_order)
        some_object.wait_element_clickable(locators.section_order_feed_locators.order_feed_button)
        some_object.click_on_section(locators.section_order_feed_locators.order_feed_button)
        some_object.wait_element_located(locators.section_order_feed_locators.order_feed_text)
        new_all_time = some_object.get_text_of_element(locators.section_order_feed_locators.counter_order_all_time)
        # передается токен и удаляется пользователь
        data.data.api_user_delete(token)
        assert int(new_all_time) > int(all_time)

    @allure.title('Счётчик "Выполнено за сегодня" увеличивается при новом заказе')
    def test_counter_increases_new_order_today(self, driver):
        some_object = HomePage(driver)
        some_object.get_site(data.urls.site)
        some_object.wait_element_clickable(locators.section_order_feed_locators.order_feed_button)
        some_object.click_on_section(locators.section_order_feed_locators.order_feed_button)
        some_object.wait_element_located(locators.section_order_feed_locators.order_feed_text)
        today = some_object.get_text_of_element(locators.section_order_feed_locators.counter_order_today)
        # создание уникального пользователя, логин и возвращение токена
        token = data.data.login_unique_user(some_object)
        some_object.wait_element_located(locators.section_order_feed_locators.assemble_the_burger_text)
        some_object.drag_and_drop_element(locators.basic_functionality_locators.ingredient_button,
                                          locators.basic_functionality_locators.place_for_ingredient)
        some_object.click_on_section(locators.basic_functionality_locators.order_button)
        some_object.wait_element_clickable(locators.section_order_feed_locators.close_window_order)
        some_object.wait_another_text(locators.section_order_feed_locators.number_order, data.variables.default_number)
        some_object.click_on_section(locators.section_order_feed_locators.close_window_order)
        some_object.wait_element_clickable(locators.section_order_feed_locators.order_feed_button)
        some_object.click_on_section(locators.section_order_feed_locators.order_feed_button)
        some_object.wait_element_located(locators.section_order_feed_locators.order_feed_text)
        today_new = some_object.get_text_of_element(locators.section_order_feed_locators.counter_order_today)
        # передается токен и удаляется пользователь
        data.data.api_user_delete(token)
        assert int(today_new) > int(today)

    @allure.title('Новый заказ появляется в разделе "В работе"')
    def test_new_order_appears_in_progress_section(self, driver):
        some_object = HomePage(driver)
        some_object.get_site(data.urls.site)
        # создание уникального пользователя, логин и возвращение токена
        token = data.data.login_unique_user(some_object)
        some_object.wait_element_located(locators.section_order_feed_locators.assemble_the_burger_text)
        some_object.drag_and_drop_element(locators.basic_functionality_locators.ingredient_button,
                                          locators.basic_functionality_locators.place_for_ingredient)
        some_object.click_on_section(locators.basic_functionality_locators.order_button)
        some_object.wait_element_clickable(locators.section_order_feed_locators.close_window_order)
        order_number = some_object.wait_another_text(locators.section_order_feed_locators.number_order,
                                                     data.variables.default_number)
        some_object.click_on_section(locators.section_order_feed_locators.close_window_order)
        some_object.wait_element_clickable(locators.section_order_feed_locators.order_feed_button)
        some_object.click_on_section(locators.section_order_feed_locators.order_feed_button)
        some_object.wait_element_will_be_visible(locators.section_order_feed_locators.in_work_order, order_number)
        in_work_order = some_object.get_text_of_element(locators.section_order_feed_locators.in_work_order)
        # передается токен и удаляется пользователь
        data.data.api_user_delete(token)
        assert order_number in in_work_order
