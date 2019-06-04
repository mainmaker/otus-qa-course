from Assignment_10_selenium_page_object.models.locators import DashboardLocators


class BasePage:
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    def _check_for_success_(self):
        """Docstring"""
        return self.driver.find_element(*DashboardLocators.SUCCESS)
