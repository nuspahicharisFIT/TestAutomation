from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import pytest
from login_module import login  

usernameValue = "HARABELMOREDZO"

def test_login(driver):
    wait=WebDriverWait(driver,60)
    driver.get("https://olx.ba")
    login(driver, wait)
    usernameValidacija = wait.until(ec.presence_of_element_located
                                    ((By.XPATH,"//a[contains(@class, 'flex') and contains(@class, 'flex-col') and contains(@class, 'items-start') and contains(@class, 'px-sm') and contains(@class, 'rounded-sm') and contains(@class, 'profile-wrap')]//child::*[contains(@class, 'font-semibold') and contains(@class, 'cursor-pointer')]"))).text

    sidemenu_btn =wait.until(ec.element_to_be_clickable((By.XPATH,"//img[contains(@class, 'ml-sm') and contains(@class, 'cursor-pointer')]")))
    sidemenu_btn.click()

    assert usernameValidacija==usernameValue


    
            

