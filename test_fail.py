# def test_failure(driver):
#     driver.get("https://opensource-demo.orangehrmlive.com/")
#     assert False, "Forcing this test to fail to check screenshot"
def test_invalid_login_should_fail(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element("name", "username").send_keys("wronguser")
    driver.find_element("name", "password").send_keys("wrongpass")
    driver.find_element("tag name", "button").click()
    assert "Invalid credentials" in driver.page_source 
