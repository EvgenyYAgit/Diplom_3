from selenium.webdriver.common.by import By
from locators.main_locators import MainLocators


class SectionOrderFeedLocators(MainLocators):
    # первый заказ в ленте
    first_order = [By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6'][position()=1]"]
    # тест состав заказа
    contents_order = [By.XPATH, "//p[text()='Cостав']"]

    # текст ваш заказ начали готовить
    order_is_cooking = [By.XPATH, "//p[text()='Ваш заказ начали готовить']"]
    # кнопка закрыть оформление заказа
    close_window_order = [By.XPATH, "//button[@type='button']"]
    # кнопка история заказов
    history_order_button = [By.XPATH, "//a[text()='История заказов']"]

    # получить текст с заказа
    order_text = [By.XPATH, "//p[@class='text text_type_digits-default']"]
    # список готовых заказов
    list_ready_order = [By.XPATH, "//li[@class='text text_type_digits-default mb-2']"]

    # счетчик выполнено за все время
    counter_order_all_time = [By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p"]

    # счетчик выполнено за сегодня
    counter_order_today = [By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p"]

    # вложенный элемент номера заказа в работе
    in_work_order = [By.XPATH,
                     "//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/descendant::li"]
    # номер оформленного заказа
    number_order = [By.XPATH, "//p[text()='идентификатор заказа']/preceding-sibling::h2"]
    # текст идентификатор заказа
    text_identifier_order = [By.XPATH, "//p[text()='идентификатор заказа']"]
