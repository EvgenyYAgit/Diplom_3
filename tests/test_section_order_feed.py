import allure
from pages.section_order_feed_page import SectionOrderFeed
import data.variables
import data.helpers
import data.urls


class TestSectionOrderFeed:

    @allure.title('Всплывающее окно с деталями заказа')
    def test_pop_up_window_order_details(self, driver):
        page = SectionOrderFeed(driver)
        page.go_to_site()
        page.click_order_feed_button()
        page.wait_text_order_feed_text()
        page.click_first_order()
        page.wait_text_contents_order()
        excepted = page.get_text_contents_order()
        assert data.variables.text_composition == excepted

    @allure.title('Заказы из «История заказов» отображаются на странице «Лента заказов»')
    def test_same_orders_in_different_places(self, driver):
        page = SectionOrderFeed(driver)
        page.go_to_site()
        data_user = data.helpers.login_unique_user()
        data.helpers.login(page, data_user[1], data_user[2])
        page.wait_text_assemble_the_burger_text()
        page.drag_and_drop_ingredient()
        page.click_order_button()
        page.wait_another_number_order()
        page.click_close_window_order()
        page.click_order_feed_button()
        page.click_personal_area()
        page.click_history_order_button()
        page.wait_clickable_order_text()
        number_order = page.get_order_text()
        page.click_order_feed_button()
        page.wait_text_order_feed_text()
        list_orders = page.get_text_list_ready_order()
        list_number_orders = [list_orders.text for list_orders in list_orders]
        data.helpers.api_user_delete(data_user[0])
        assert number_order[1:] in list_number_orders

    @allure.title('Счётчик "Выполнено за всё время" увеличивается при новом заказе')
    def test_the_counter_increases_new_order_all_time(self, driver):
        page = SectionOrderFeed(driver)
        page.go_to_site()
        data_user = data.helpers.login_unique_user()
        data.helpers.login(page, data_user[1], data_user[2])
        page.click_order_feed_button()
        page.wait_text_order_feed_text()
        all_time = page.get_text_counter_order_all_time()
        page.click_constructor_button()
        page.wait_text_assemble_the_burger_text()
        page.drag_and_drop_ingredient()
        page.click_order_button()
        page.wait_another_number_order()
        page.click_close_window_order()
        page.click_order_feed_button()
        page.wait_text_order_feed_text()
        new_all_time = page.get_text_counter_order_all_time()
        data.helpers.api_user_delete(data_user[0])
        assert int(new_all_time) > int(all_time)

    @allure.title('Счётчик "Выполнено за сегодня" увеличивается при новом заказе')
    def test_counter_increases_new_order_today(self, driver):
        page = SectionOrderFeed(driver)
        page.go_to_site()
        data_user = data.helpers.login_unique_user()
        data.helpers.login(page, data_user[1], data_user[2])
        page.click_order_feed_button()
        page.wait_text_order_feed_text()
        all_time = page.get_text_counter_order_today()
        page.click_constructor_button()
        page.wait_text_assemble_the_burger_text()
        page.drag_and_drop_ingredient()
        page.click_order_button()
        page.wait_another_number_order()
        page.click_close_window_order()
        page.click_order_feed_button()
        page.wait_text_order_feed_text()
        new_all_time = page.get_text_counter_order_today()
        data.helpers.api_user_delete(data_user[0])
        assert int(new_all_time) > int(all_time)

    @allure.title('Новый заказ появляется в разделе "В работе"')
    def test_new_order_appears_in_progress_section(self, driver):
        page = SectionOrderFeed(driver)
        page.go_to_site()
        data_user = data.helpers.login_unique_user()
        data.helpers.login(page, data_user[1], data_user[2])
        page.wait_text_assemble_the_burger_text()
        page.drag_and_drop_ingredient()
        page.click_order_button()
        order_number = page.wait_another_number_order()
        page.click_close_window_order()
        page.click_order_feed_button()
        page.wait_element_visible(order_number)
        in_work_order = page.get_text_in_work_order()
        data.helpers.api_user_delete(data_user[0])
        assert order_number in in_work_order
