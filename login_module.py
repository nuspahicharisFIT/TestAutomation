from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from cookie_module import accept_cookies

def login(driver, wait):
    accept_cookies(driver, wait)
    btn_prijava=wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@aria-label='prijava']")))
    btn_prijava.click()
    username = wait.until(ec.element_to_be_clickable((By.NAME,'username')))
    username.clear()
    username.send_keys("HARABELMOREDZO")
    password = wait.until(ec.element_to_be_clickable((By.NAME,'password')))
    password.clear()
    password.send_keys("hbrnkt123")
    btn_prijava = wait.until(ec.element_to_be_clickable((By.CLASS_NAME,'my-lg')))
    btn_prijava.click()