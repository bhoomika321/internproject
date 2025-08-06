from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class NavPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def go_to(self, link_text):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, link_text))).click()

    def get_page_heading(self):
        return self.wait.until(EC.visibility_of_element_located((By.TAG_NAME,"h1"))).text



