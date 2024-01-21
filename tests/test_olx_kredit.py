from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import pytest
from login_module import login

expectedUrl = "https://olx.ba/mojolx/olx-kredit/stanje-naloga"

def test_olx_kredit(driver):
    wait=WebDriverWait(driver,60)
    driver.get("https://olx.ba")
    login(driver,wait)
    btn_kredit = wait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'olx-credit')))
    btn_kredit.click()
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[@data-v-18c9e23a and @href='/o-olxu/olxkredit' and contains(text(), 'Šta je OLX kredit i za šta se koristi?')]")))
    url = driver.current_url
    assert url == expectedUrl
