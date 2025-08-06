from pageobjectmodel.login_page import Logpage
from pageobjectmodel.dashboard_page import Dashboard
from config import config
from utils.screenshot import take_screenshot

def test_ui_elements_visible(driver):
    login = Logpage(driver)
    driver.get(config.BASE_URL)
    assert login.is_logo_visible(),"Logo is not visible on login page"
    take_screenshot(driver,"ui_elements")

def test_dynamic_welcome_text(driver):
    login = Logpage(driver)
    dashboard = Dashboard(driver)
    driver.get(config.BASE_URL)
    login.login(config.USERNAME,config.PASSWORD)
    welcome_text = dashboard.get_welcome_text()
    assert "Dashboard" in welcome_text 
    take_screenshot(driver,"dynamic_element")
