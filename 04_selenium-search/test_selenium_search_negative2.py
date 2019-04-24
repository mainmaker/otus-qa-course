import time
from selenium.webdriver.common.keys import Keys


def test_negative_login2(driver):
    """Docstring"""
    usarname_field = driver.find_element_by_xpath("//input[@id='input-username']")
    usarname_field.send_keys("admin")
    time.sleep(1)
    password_field = driver.find_element_by_xpath("//input[@id='input-password']")
    password_field.send_keys("123451")
    password_field.send_keys(Keys.RETURN)
    time.sleep(1)
    assert driver.find_element_by_xpath("//*[contains(text(), 'No match for Username and/or Password.')]")
