import time


def test_positive_forgot(driver):
    """Docstring"""
    link = driver.find_element_by_link_text("Forgotten Password")
    time.sleep(1)
    link.click()
    time.sleep(1)
    assert driver.find_element_by_tag_name("h1").text == "Forgot Your Password?"
