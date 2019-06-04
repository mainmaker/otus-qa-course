import pytest
from selenium.webdriver.common.keys import Keys
from Assignment_10_selenium_page_object.models.locators import DashboardLocators


@pytest.mark.usefixtures("login")
def test_add_product(dashboard_page):
    """Docstring"""
    dashboard_page.switch_to_element("Catalog")
    dashboard_page.go_to_page("Products")
    dashboard_page.add_product("Test Product", "Test Meta Tag", "Test Model")
    assert dashboard_page._check_for_success_()
    dashboard_page.logout()

@pytest.mark.usefixtures("login")
def test_edit_product(driver, dashboard_page):
    """Docstring"""
    dashboard_page.switch_to_element("Catalog")
    dashboard_page.go_to_page("Products")
    tag_tr = dashboard_page.search_product("Test Product")
    tag_tr.find_element(*DashboardLocators.PENCIL).click()
    product_name = driver.find_element(*DashboardLocators.INPUT_NAME1)
    product_name.send_keys(Keys.CONTROL + "a")
    product_name.send_keys("Test Product Edited")
    driver.find_element(*DashboardLocators.SAVE).click()
    assert dashboard_page._check_for_success_()
    dashboard_page.logout()

@pytest.mark.usefixtures("login")
def test_delete_product(driver, dashboard_page):
    """Docstring"""
    dashboard_page.switch_to_element("Catalog")
    dashboard_page.go_to_page("Products")
    tag_tr = dashboard_page.search_product("Test Product Edited")
    tag_tr.find_element(*DashboardLocators.SELECTED).click()
    driver.find_element(*DashboardLocators.TRASH).click()
    alert = driver.switch_to.alert
    alert.accept()
    assert dashboard_page._check_for_success_()
    dashboard_page.logout()
