from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.profile_dropdown = (By.XPATH,"//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")
        self.logout_button = (By.XPATH,"//a[text()='Logout']")

    def logout(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.profile_dropdown)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.logout_button)).click()

class Dashboard:
    def __init__(self, driver):
        self.driver = driver
        self.welcome_text = (By.XPATH,"//h6")
    def get_welcome_text(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.welcome_text)).text
