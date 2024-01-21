from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

def accept_cookies(dirver,wait):
    btn_cookie=wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'css-1sjubqu')))
    btn_cookie.click()  