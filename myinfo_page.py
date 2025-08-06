from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utils.waits import wait_for_loader_disappear

class MyInfoPage:
    def __init__(self, driver):
        self.driver = driver
        self.myinfo_tab = (By.LINK_TEXT,"My Info")
        self.first_name = (By.NAME,"firstName")
        self.middle_name = (By.NAME,"middleName")
        self.last_name = (By.NAME,"lastName")
        self.employee_id = (By.XPATH,"//label[text()='Employee Id']/../following-sibling::div/input")
        self.other_id = (By.XPATH,"//label[text()='Other Id']/../following-sibling::div/input")
        self.license_number = (By.XPATH,"//label[text()=\"Driver's License Number\"]/../following-sibling::div/input")
        self.license_expiry = (By.XPATH,"//label[text()='License Expiry Date']/../following-sibling::div//input")
        self.nationality_dropdown = (By.XPATH,"//label[text()='Nationality']/../following-sibling::div//div[contains(@class,'oxd-select-text')]")
        self.marital_status_dropdown = (By.XPATH,"//label[text()='Marital Status']/../following-sibling::div//div[contains(@class,'oxd-select-text')]")
        self.date_of_birth = (By.XPATH,"//label[text()='Date of Birth']/following::input[1]")
        self.gender_male = (By.XPATH,"//input[@type='radio' and @value='1']")
        self.gender_female = (By.XPATH,"//label[contains(., 'Female')]//input[@type='radio']")
        self.save_button = (By.XPATH,"//button[@type='submit']")
    def navigate_to_myinfo(self):
        WebDriverWait(self.driver,30).until(EC.element_to_be_clickable(self.myinfo_tab)).click()      
    def wait_for_loader_to_disappear(self):
        WebDriverWait(self.driver,25).until(EC.invisibility_of_element_located((By.CLASS_NAME,"oxd-form-loader")))
        
    def clear_and_type(self, field, value):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", field)
        self.driver.execute_script("arguments[0].click();", field)
        field.clear()
        field.send_keys(value)

    def clear_and_type(self, field_locator, value):
        WebDriverWait(self.driver,20).until(
            EC.invisibility_of_element_located((By.CLASS_NAME,"oxd-form-loader"))
        )
        field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(field_locator)
        )
        field.click()
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(value)
    

    def fill_personal_info(self, fname, mname, lname, emp_id, other_id, license_no, license_exp, nationality, marital_status,date_of_birth,gender):
        wait_for_loader_disappear(self.driver)
        self.clear_and_type(self.first_name, fname)
        self.clear_and_type(self.middle_name, mname)
        self.clear_and_type(self.last_name, lname)
        self.clear_and_type(self.employee_id, emp_id)
        self.clear_and_type(self.other_id, other_id)
        self.clear_and_type(self.license_number, license_no)
        self.clear_and_type(self.license_expiry, license_exp)
        self.select_dropdown(self.nationality_dropdown, nationality)
        self.select_dropdown(self.marital_status_dropdown, marital_status)
        self.clear_and_type(self.date_of_birth,date_of_birth)
        dob_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.date_of_birth))
        dob_input.send_keys(Keys.TAB)
        wait_for_loader_disappear(self.driver)
        if gender.lower() == "female":
            gender_locator = self.gender_female
        else:
            gender_locator = self.gender_male
        gender_input = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(gender_locator))
        self.driver.execute_script("arguments[0].click();", gender_input)
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.save_button)).click()
        save_btn = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(self.save_button))
        save_btn.click()
        time.sleep(5)
    def select_dropdown(self, dropdown_locator, value_to_select):
        dropdown = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(dropdown_locator))
        dropdown.click()
        option = (By.XPATH, f"//div[@role='listbox']//span[text()='{value_to_select}']")
        WebDriverWait(self.driver,30).until(EC.element_to_be_clickable(option)).click()
    def get_value(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator)).get_attribute("value")




