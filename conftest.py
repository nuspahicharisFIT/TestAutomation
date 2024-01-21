import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    chrome_service = Service("chromedriver.exe")
    chrome_options=webdriver.ChromeOptions()
    
    driver=webdriver.Chrome(service=chrome_service, options=chrome_options)
    yield driver
    driver.quit()