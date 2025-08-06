import pytest
from pageobjectmodel.login_page import LoginPage
from utils.data_reader import get_login_data
valid_data = get_login_data("test_data/login_data.csv","valid")
@pytest.mark.valid
@pytest.mark.parametrize("credentials", valid_data)
def test_validlogin(setup, credentials):
    driver = setup
    login = LoginPage(driver)
    login.load()
    login.enter_username(credentials['username'])
    login.enter_password(credentials['password'])
    login.click_login()
    assert "dashboard" in driver.current_url.lower()


