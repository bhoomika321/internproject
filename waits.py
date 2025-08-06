from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_loader_disappear(driver, timeout=20):
    try:
        WebDriverWait(driver, timeout).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR,"div.oxd-form-loader"))
        )
    except:
        print("[WARNING] Loader not disappearing in time.")
