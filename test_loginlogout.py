from config import config
from pageobjectmodel.login_page2 import LoginP
from pageobjectmodel.dashboard_page import DashboardPage

def test_login_and_logout(driver):
    login_page = LoginP(driver)
    dashboard_page = DashboardPage(driver)
    login_page.loadurl(config.BASE_URL)
    login_page.login(config.USERNAME,config.PASSWORD)
    dashboard_page.logout()
    assert "login" in driver.current_url.lower()





