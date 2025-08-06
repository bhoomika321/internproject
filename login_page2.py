from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class LoginP:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.NAME,"username")
        self.password_input = (By.NAME,"password")
        self.login_button = (By.XPATH,"//button[@type='submit']")

    def loadurl(self,base_url):
        self.driver.get(base_url)

    def login(self,username,password):
        wait = WebDriverWait(self.driver,20)
        wait.until(EC.presence_of_element_located(self.username_input)).send_keys(username)
        wait.until(EC.presence_of_element_located(self.password_input)).send_keys(password)
        wait.until(EC.element_to_be_clickable(self.login_button)).click()
        
