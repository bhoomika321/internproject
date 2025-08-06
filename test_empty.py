import pytest
from pageobjectmodel.login_page import LoginPage
from utils.data_reader import get_login_data
empty_data = get_login_data("test_data/login_data.csv","empty")
@pytest.mark.empty
@pytest.mark.parametrize("credentials",empty_data)
def test_empty(setup, credentials):
    driver = setup
    login = LoginPage(driver)
    login.load()
    login.enter_username(credentials['username'])
    login.enter_password(credentials['password'])
    login.click_login()
    assert "required" in driver.page_source.lower()
