import pytest
from config import config
from pageobjectmodel.login_page2 import LoginP
from pageobjectmodel.myinfo_page import MyInfoPage
from utils.read_csv import get_form_data

@pytest.mark.parametrize(
    "fname, mname, lname, emp_id, other_id, license_no,license_exp, nationality, marital_status,date_of_birth,gender",
    get_form_data()
)
def test_fill_form(driver, fname, mname, lname, emp_id, other_id, license_no, license_exp, nationality, marital_status,date_of_birth,gender):
    login_page = LoginP(driver)
    login_page.loadurl(config.BASE_URL)
    login_page.login(config.USERNAME,config.PASSWORD)
    myinfo = MyInfoPage(driver)
    myinfo.navigate_to_myinfo()
    myinfo.fill_personal_info(
        fname, mname, lname,
        emp_id, other_id,
        license_no, license_exp,
        nationality, marital_status,
        date_of_birth,gender
    )
