from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import pytest
from login_module import login

expectedUrl = "https://olx.ba/poruke"

def test_login(driver):
    wait=WebDriverWait(driver,60)
    driver.get("https://olx.ba")
    login(driver,wait)
    btn_poruke = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'flex') and contains(@class, 'items-center') and contains(@class, 'border-r') and contains(@class, 'border-gray-400') and contains(@class, 'mr-md') and contains(@class, 'pr-md') and contains(@class, 'msg')]/img")))
    btn_poruke.click()
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@placeholder='Pretraži poruke']")))
    currentUrl = driver.current_url
    assert expectedUrl == currentUrl