from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from seletools.actions import drag_and_drop
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переход на страницу')
    def get_site(self, site):
        self.driver.get(site)

    @allure.step('Нажатие на кликабельный элемент')
    def click_on_section(self, section):
        self.driver.find_element(*section).click()

    @allure.step('Ожидание до видимого элемента')
    def wait_element_located(self, element_located):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(element_located))

    @allure.step('Ожидание до кликабельного элемента')
    def wait_element_clickable(self, element_clickable):
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(element_clickable))

    @allure.step('Получение текста элемента')
    def get_text_of_element(self, text_of_element):
        text = self.driver.find_element(*text_of_element).text
        return text

    @allure.step('Перенос элемента')
    def drag_and_drop_element(self, source, target):
        source = self.driver.find_element(*source)
        target = self.driver.find_element(*target)
        drag_and_drop(self.driver, source, target)

    @allure.step('Ввод сообщения в строку input')
    def input_text(self, string, message):
        self.driver.find_element(*string).send_keys(message)

    @allure.step('Ожидание до видимости элемента')
    def wait_element_will_be_visible(self, present_element, text):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.text_to_be_present_in_element(present_element, text))

    @allure.step('Ожидание изменения элемента в тексте')
    def wait_another_text(self, waiting_element, text):
        # ожидание изменения текста
        WebDriverWait(self.driver, 30).until(lambda driver: self.driver.find_element(
            *waiting_element).text != text)
        # возврат нового текста
        new_text = self.driver.find_element(*waiting_element).text
        return new_text

    @allure.step('Получить текст списка')
    def get_text_list(self, list_text):
        text = self.driver.find_elements(*list_text)
        return text
