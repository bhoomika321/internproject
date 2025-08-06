import pytest
from pageobjectmodel.login_page import LoginPage
from utils.data_reader import get_login_data
invalid_data = get_login_data("test_data/login_data.csv","invalid")
@pytest.mark.invalid
@pytest.mark.parametrize("credentials",invalid_data)
def test_invalidlogin(setup,credentials):
    driver = setup
    login = LoginPage(driver)
    login.load()
    login.enter_username(credentials['username'])
    login.enter_password(credentials['password'])
    login.click_login()
    # assert "Invalid credentials" in driver.page_source.lower()
    assert "auth/login" in driver.current_url.lower() 
