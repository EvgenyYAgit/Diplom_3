import pytest
import locators.personal_area_locators
from pages.personal_area_page import PersonalArea
from selenium import webdriver


@pytest.fixture() #(params=['firefox', 'chrome'])
def driver(request):
    browser = None
    options = webdriver.FirefoxOptions()
    options.add_argument('--window-size=1920,1080')
    #if request.param == 'firefox':
    #    browser = webdriver.Firefox(options=options)
    #elif request.param == 'chrome':
    browser = webdriver.Chrome()

    yield browser

    browser.quit()
