import pytest
from pageobjectmodel.nav_page import NavPage

@pytest.mark.parametrize("menu_link,expected_heading", [
    ("About", "Selenium automates browsers. That's it!"),
    ("Downloads", "Downloads"),
    ("Projects", "Projects"),
    ("Support", "Getting Help"),
    ("Blog", "Selenium Blog"),
    ("Documentation", "The Selenium Browser Automation Project")
])
def test_menu_navigation(navigation, menu_link, expected_heading):
    nav = NavPage(navigation)
    nav.go_to(menu_link)
    heading = nav.get_page_heading()
    assert expected_heading.lower() in heading.lower()

