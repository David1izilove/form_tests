from pytest import fixture
from selenium import webdriver


@fixture(scope='session')
def chrome_browser():
    browser = webdriver.Chrome('/home/david/Downloads/chromedriver')
    browser.implicitly_wait(10)
    browser.maximize_window()
    return browser

