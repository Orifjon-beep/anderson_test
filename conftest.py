from selenium import webdriver
from selenium.wbdriver.chrome.options import Options
import pytest



    

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    browser.close()
