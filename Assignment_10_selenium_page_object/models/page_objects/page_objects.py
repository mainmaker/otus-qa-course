from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from Assignment_10_selenium_page_object.models.page import BasePage
from Assignment_10_selenium_page_object.models.locators import LoginLocators, DashboardLocators


class LoginPage(BasePage):
    """docstring for LoginPage"""

    def set_username(self, username):
        """Docstring"""
        self.driver.find_element(*LoginLocators.USERNAME).send_keys(username)

    def set_password(self, password):
        """Docstring"""
        self.driver.find_element(*LoginLocators.PASSWORD).send_keys(password + Keys.RETURN)

class DashboardPage(BasePage):
    """docstring for DashboardPage"""

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

    # def check_for_success(self):
    #     """Docstring"""
    #     return self.driver.find_element(*DashboardLocators.SUCCESS)
