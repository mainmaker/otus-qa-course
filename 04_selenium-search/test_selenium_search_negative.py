import time
from selenium.webdriver.common.keys import Keys


def test_negative_login1(driver):
    """Docstring"""
    usarname_field = driver.find_element_by_xpath("//input[@name='username']")
    usarname_field.send_keys("admin2")
    time.sleep(2)
    usarname_field = driver.find_element_by_xpath("//input[@name='username']")
    usarname_field.send_keys(Keys.CONTROL + "a")
    usarname_field.send_keys(Keys.DELETE)
    time.sleep(2)
    password_field = driver.find_element_by_xpath("//input[@name='password']")
    password_field.send_keys("12345")
    password_field.send_keys(Keys.RETURN)
    time.sleep(1)
    assert driver.find_element_by_xpath("//*[contains(text(), 'No match for Username and/or Password.')]")
