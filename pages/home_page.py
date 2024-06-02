from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from seletools.actions import drag_and_drop
import allure


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переход на страницу')
    def get_site(self, site):
        self.driver.get(site)

    @allure.step('Ввод сообщения в строку input')
    def input_text(self, string, message):
        self.driver.find_element(*string).send_keys(message)

    @allure.step('Прокрутка до элемента на странице')
    def scroll_element(self, scroll_element):
        element = self.driver.find_element(*scroll_element)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Нажатие на кликабельный элемент')
    def click_on_section(self, section):
        self.driver.find_element(*section).click()

    @allure.step('Ожидание до видимого элемента')
    def wait_element_located(self, element_located):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(element_located))

    @allure.step('Ожидание до кликабельного элемента')
    def wait_element_clickable(self, element_clickable):
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(element_clickable))

    @allure.step('Ожидание до элемента когда он будет виден')
    def wait_element_will_be_visible(self, element_clickable, text):
        WebDriverWait(self.driver, 30).until(expected_conditions.text_to_be_present_in_element(element_clickable, text))

    @allure.step('Получение текста элемента')
    def get_text_of_element(self, text_of_element):
        text = self.driver.find_element(*text_of_element).text
        return text

    @allure.step('Поиск элементов по локатору')
    def get_text_of_elements(self, text_of_element):
        text = self.driver.find_elements(*text_of_element)
        return text

    @allure.step('Перенос drag_and_drop элемента')
    def drag_and_drop_element(self, source_object, target_object):
        source = self.driver.find_element(*source_object)
        target = self.driver.find_element(*target_object)
        drag_and_drop(self.driver, source, target)

    @allure.step('Ожидание изменения элемента в тексте')
    def wait_another_text(self, element, text):
        # ожидание изменения текста
        WebDriverWait(self.driver, 30).until(lambda driver: driver.find_element(*element).text != text)
        # возврат нового текста
        return self.driver.find_element(*element).text
