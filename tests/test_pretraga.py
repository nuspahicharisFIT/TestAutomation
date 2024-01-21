from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import pytest
from cookie_module import accept_cookies

resultValue = "REZULTATA"

def test_login(driver):
    wait=WebDriverWait(driver,60)
    driver.get("https://olx.ba")
    accept_cookies(driver,wait)
    pretraga = wait.until(expected_conditions.element_to_be_clickable((By.NAME, 'notASearchField')))
    pretraga.clear()
    pretraga.send_keys("auto")
    pretraga.send_keys(Keys.RETURN)
    rezultatPretrage = wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'search-title')))
    checkValue = rezultatPretrage.text.split()[-1]
    assert resultValue == checkValue