import time
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 

from Assignment_07_selenium_elements.locators import AdminLocators, DashboardLocators


class LoginPage():
    """docstring for AdminPage"""
    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        """Docstring"""
        self.driver.find_element(*AdminLocators.USERNAME).send_keys(username)        

    def set_password(self, password):
        """Docstring"""
        self.driver.find_element(*AdminLocators.PASSWORD).send_keys(password + Keys.RETURN)
            
class DashboardPage():
    """docstring for DashboardPage"""
    def __init__(self, driver):
        self.driver = driver

    def switch_to_element(self, element_name):
        """Docstring"""
        els = self.driver.find_elements(*DashboardLocators.A_PARENT_COLLAPSED)
        for el in els:
            if el.text == element_name:
                el.click()
                break

    def go_to_page(self, page_name):
        """Docstring"""
        links = self.driver.find_elements(*DashboardLocators.A_TAG)
        for link in links:
            if link.text == page_name:
                link.click()
                break

    def add_product(self, product_name, product_tag, product_model):
        """Docstring"""
        self.driver.find_element(*DashboardLocators.PLUS).click()
        self.driver.find_element(*DashboardLocators.INPUT_NAME1).send_keys(product_name)
        self.driver.find_element(*DashboardLocators.INPUT_META_TITLE1).send_keys(product_tag)
        self.switch_tab("Data")
        self.driver.find_element(*DashboardLocators.INPUT_MODEL).send_keys(product_model)
        self.driver.find_element(*DashboardLocators.SAVE).click()

    def search_product(self, product_name):
        """Docstring"""
        trs = self.driver.find_elements(*DashboardLocators.TR_TAG)
        for tr in trs:
            tds = tr.find_elements(*DashboardLocators.TD_TAG)
            if tds[2].text == product_name:
                return tr

    def switch_tab(self, tab_name):
        """Docstring"""
        links = self.driver.find_elements(*DashboardLocators.A_TAG)
        for link in links:
            if link.text == tab_name:
                link.click()
                break

    def logout(self):
        """Docstring"""
        self.driver.find_element(*DashboardLocators.LOGOUT).click()


@pytest.fixture(scope="module")
def login_page(driver):
    """Docstring"""
    return LoginPage(driver)

@pytest.fixture(scope="function")
def login(login_page):
    """Docstring"""
    login_page.set_username("admin")
    time.sleep(1)
    login_page.set_password("12345")
    time.sleep(1)

@pytest.fixture(scope="module")
def dashboard_page(driver):
    """Docstring"""
    return DashboardPage(driver)


@pytest.mark.usefixtures("login")
def test_add_product(driver, dashboard_page):
    """Docstring"""
    dashboard_page.switch_to_element("Catalog")
    dashboard_page.go_to_page("Products")
    dashboard_page.add_product("Test Product", "Test Meta Tag", "Test Model")
    assert driver.find_element(*DashboardLocators.SUCCESS)  
    dashboard_page.logout()

@pytest.mark.usefixtures("login")
def test_edit_product(driver, dashboard_page):
    """Docstring"""
    dashboard_page.switch_to_element("Catalog")
    dashboard_page.go_to_page("Products")
    tr = dashboard_page.search_product("Test Product")
    tr.find_element(*DashboardLocators.PENCIL).click()
    product_name = driver.find_element(*DashboardLocators.INPUT_NAME1)
    product_name.send_keys(Keys.CONTROL + "a")
    product_name.send_keys("Test Product Edited")
    driver.find_element(*DashboardLocators.SAVE).click()
    assert driver.find_element(*DashboardLocators.SUCCESS)
    dashboard_page.logout()

@pytest.mark.usefixtures("login")
def test_delete_product(driver, dashboard_page):
    """Docstring"""
    dashboard_page.switch_to_element("Catalog")
    dashboard_page.go_to_page("Products")
    tr = dashboard_page.search_product("Test Product Edited")
    tr.find_element(*DashboardLocators.SELECTED).click()
    driver.find_element(*DashboardLocators.TRASH).click()
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(1)
    assert driver.find_element(*DashboardLocators.SUCCESS)
    dashboard_page.logout()

