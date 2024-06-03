from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
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

    @allure.step('Ожидание элемента и нажатие через скрипт')
    def wait_and_click(self, element):
        wait_element = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(element))
        self.driver.execute_script("arguments[0].click();", wait_element)
