from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import time
from login_module import login

usernameValue = "HARABELMOREDZO"
expectedUrl = "https://olx.ba/"

def test_odjava(driver):
    wait = WebDriverWait(driver, 60)
    driver.get("https://olx.ba")
    login(driver,wait)
    sidemenu_btn = wait.until(ec.element_to_be_clickable((By.XPATH, "//img[contains(@class, 'ml-sm') and contains(@class, 'cursor-pointer')]")))
    sidemenu_btn.click()

    btn_odjava = wait.until(ec.element_to_be_clickable((By.XPATH, "//a[@data-v-3c6796b9 and @class='left logout']")))

    driver.execute_script("arguments[0].scrollIntoView();", btn_odjava)

    driver.execute_script("arguments[0].click();", btn_odjava)

    wait.until(ec.presence_of_element_located((By.XPATH, "//*[@aria-label='prijava']")))
        
    url = driver.current_url
    assert url == expectedUrl
