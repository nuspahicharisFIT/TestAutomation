from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementClickInterceptedException
import time
from login_module import login

usernameValue = "HARABELMOREDZO"
expectedUrl = "https://olx.ba/mojolx/postavke/korisnicke-informacije"

def test_korisnicke_postavke(driver):
    wait = WebDriverWait(driver, 60)
    driver.get("https://olx.ba")
    login(driver,wait)
    sidemenu_btn = wait.until(ec.element_to_be_clickable((By.XPATH, "//img[contains(@class, 'ml-sm') and contains(@class, 'cursor-pointer')]")))
    sidemenu_btn.click()

    btn_postavke = wait.until(ec.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'left') and span[text()='Postavke']]")))   
    driver.execute_script("arguments[0].scrollIntoView();", btn_postavke)

    driver.execute_script("arguments[0].click();", btn_postavke)

    wait.until(ec.presence_of_element_located((By.XPATH, "//h1[@data-v-67502ee7 and contains(text(),'Korisničke informacije')]"))) 

    url = driver.current_url
    assert url == expectedUrl
