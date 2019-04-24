import time
from selenium.webdriver.common.keys import Keys


def test_positive_login(driver):
    """Docstring"""
    usarname_field = driver.find_element_by_id("input-username")
    usarname_field.send_keys("admin")
    time.sleep(1)
    password_field = driver.find_element_by_id("input-password")
    password_field.send_keys("12345")
    password_field.send_keys(Keys.RETURN)
    time.sleep(1)
    assert driver.find_element_by_id("menu-dashboard")
