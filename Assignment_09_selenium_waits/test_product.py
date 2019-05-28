import time
import pytest
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from Assignment_09_selenium_waits.locators import AdminLocators, DashboardLocators


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
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((DashboardLocators.A_PARENT_COLLAPSED)))

        els = self.driver.find_elements(*DashboardLocators.A_PARENT_COLLAPSED)
        for element in els:
            if element.text == element_name:
                element.click()
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
        try:
            pagination = self.driver.find_element(*DashboardLocators.PAGINATION)
            lis = pagination.find_elements_by_tag_name("li")
        except NoSuchElementException:
            print("\nNo paginations found")
            return self.iterate_trs(product_name)
        else:
            for _ in range(len(lis) - 2):
                trs = self.driver.find_elements(*DashboardLocators.TR_TAG)
                for tag_tr in trs:
                    tds = tag_tr.find_elements(*DashboardLocators.TD_TAG)
                    if tds[2].text == product_name:
                        return tag_tr

                pagination = self.driver.find_element(*DashboardLocators.PAGINATION)
                lis = pagination.find_elements_by_tag_name("li")
                lis[-2].find_element(*DashboardLocators.A_TAG).click()

    def iterate_trs(self, product_name):
        """Docstring"""
        trs = self.driver.find_elements(*DashboardLocators.TR_TAG)
        for tag_tr in trs:
            tds = tag_tr.find_elements(*DashboardLocators.TD_TAG)
            if tds[2].text == product_name:
                return tag_tr

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
    login_page.set_password("12345")
    time.sleep(1)  # To prevent multiple data inputing in the fields

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
    tag_tr = dashboard_page.search_product("Test Product")
    tag_tr.find_element(*DashboardLocators.PENCIL).click()
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
    tag_tr = dashboard_page.search_product("Test Product Edited")
    tag_tr.find_element(*DashboardLocators.SELECTED).click()
    driver.find_element(*DashboardLocators.TRASH).click()
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(1)
    assert driver.find_element(*DashboardLocators.SUCCESS)
    dashboard_page.logout()
