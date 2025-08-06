import os
from datetime import datetime
def take_screenshot(driver, name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder = "screenshots"
    os.makedirs(folder, exist_ok=True)
    driver.save_screenshot(f"{folder}/{name}_{timestamp}.png")

def take_screen(driver,name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder = "screenshots"
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f"{name}_{timestamp}.png")
    driver.save_screenshot(path)
    return path
