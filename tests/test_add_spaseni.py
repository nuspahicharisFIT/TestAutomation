import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import pytest
from login_module import login

no_spaseni = "Nemate spašenih oglasa"

def test_login(driver):
    wait=WebDriverWait(driver,60)
    driver.get("https://olx.ba")
    
    login(driver,wait)

    btn_oglas=wait.until(ec.element_to_be_clickable((By.XPATH,"//div[contains(@class, 'grid-desktop-md') and contains(@class, 'px-md')]/descendant::h1[contains(@class, 'main-heading') and contains(@class, 'normal-heading')][3]")))
    oglas_text=btn_oglas.text
    btn_oglas.click()

    wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "main-title-listing")))

    btn_spasi_oglas= wait.until(ec.element_to_be_clickable((By.XPATH,"//div[contains(@class, 'mb-md') and contains(@class, 'flex') and contains(@class, 'items-center') and contains(@class, 'justify-between') and contains(@class, 'w-full')]/div[2]//button[3]")))
    btn_spasi_oglas.click()

    sidemenu_btn =wait.until(ec.element_to_be_clickable((By.XPATH,"//img[contains(@class, 'ml-sm') and contains(@class, 'cursor-pointer')]")))
    sidemenu_btn.click()

    spaseni_oglasi = wait.until(ec.element_to_be_clickable((By.XPATH,"//a[@class='left link' and .//span[text()='Spašeni oglasi']]")))
    spaseni_oglasi.click()

    spaseni = wait.until(ec.element_to_be_clickable((By.XPATH,"//div[contains(@class, 'saved-article')]/a/div/div[2]//h1"))).text

    assert spaseni == oglas_text

    btn_zatvori = wait.until(ec.element_to_be_clickable((By.XPATH,"//img[@alt='close']")))
    btn_zatvori.click()

    zatvoreno_validacija =wait.until(ec.element_to_be_clickable((By.XPATH,"//h1[contains(@class, 'py-lg')]"))).text
    
    assert zatvoreno_validacija==no_spaseni

    

    

    

   


    
            

