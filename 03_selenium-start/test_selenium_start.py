def test_start(driver):
    """Docstring"""
    assert driver.find_element_by_link_text("OpenCart").text == "OpenCart"
