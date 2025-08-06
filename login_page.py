import time   
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input =(By.NAME,"username")
        self.password_input = (By.NAME,"password")
        self.login_button = (By.XPATH,"//button[@type='submit']")
        self.wait = WebDriverWait(self.driver,10)

    def load(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()

    def enter_username(self,username):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(self.username_input)).send_keys(username)

    def enter_password(self,password):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(self.password_input)).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(self.login_button)).click()  
        time.sleep(3)
    def get_error_message(self):
        error_locator = (By.XPATH,"//p[text()='Invalid credentials']")
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(error_locator)).text
    
    def get_required_field_error(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//span[text()='Required']")))
        error_message = self.driver.find_element(By.XPATH,"//span[text()='Required']").text
        assert "required" in error_message.lower()
  
  
#   form filling page

class Logpage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.NAME,"username")
        self.password_input = (By.NAME,"password")
        self.login_button = (By.CSS_SELECTOR,"button[type='submit']")
        self.driver.save_screenshot("login_failure.png")
        self.logo = (By.XPATH,"//div[@class='orangehrm-login-logo']")

    def login(self, username, password):
        print("[INFO] Waiting for login fields to be visible...")
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.NAME,"username"))).send_keys(username)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.NAME,"password"))).send_keys(password)
        WebDriverWait(self.driver,15).until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']"))).click()
    def is_logo_visible(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.logo))
  

        


        

        
        
