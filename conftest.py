import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    yield driver
    driver.quit()

# navigation
@pytest.fixture
def navigation():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.selenium.dev/")
    yield driver
    driver.quit()



import pytest
import os
from utils.screenshot import take_screen
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' and report.failed:
        driver = item.funcargs.get("driver",None)
        if driver:
            screenshot_path = take_screen(driver,item.name)
            if os.path.exists(screenshot_path):
                extra.append(pytest_html.extras.image(screenshot_path))
        report.extra = extra
def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin('html')
