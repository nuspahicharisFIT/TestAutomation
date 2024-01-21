from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import pytest
from cookie_module import accept_cookies

def test_pregled_oglasa(driver):
    wait=WebDriverWait(driver,60)
    driver.get("https://olx.ba")
    accept_cookies(driver,wait)
    btn_oglas=wait.until(ec.element_to_be_clickable((By.XPATH,"//div[contains(@class, 'grid-desktop-md') and contains(@class, 'px-md')]/descendant::h1[contains(@class, 'main-heading') and contains(@class, 'normal-heading')][3]")))
    oglas_text=btn_oglas.text
    btn_oglas.click()
    detaljan_element = wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "main-title-listing")))
    detaljan_text = detaljan_element.text

    assert detaljan_text == oglas_text