import sys
import time
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.firefox.options import Options
from Assignment_10_selenium_page_object.models.page_objects.page_objects import LoginPage, DashboardPage


def pytest_addoption(parser):
    """Docstring"""
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--timeout", action="store", default="1000")
    parser.addoption("--address", action="store", default="http://165.22.10.232/")

@pytest.fixture(scope="session", autouse=True)
def driver(request):
    """Docstring"""
    browser = request.config.getoption("--browser")
    path = "opencart/admin/"
    address = "".join([request.config.getoption("--address"), path])

    if browser == 'firefox':
        options = Options()
        options.headless = True
        capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()
        capabilities['timeouts'] = {'implicit': 3000, 'pageLoad': 3000, 'script': 30000}
        capabilities['loggingPrefs'] = {'browser': 'ALL', 'client': 'ALL', 'driver': 'ALL',
                                        'performance': 'ALL', 'server': 'ALL'}
        profile = webdriver.FirefoxProfile()
        profile.set_preference('app.update.auto', False)
        profile.set_preference('app.update.enabled', False)
        profile.accept_untrusted_certs = True
        wd = webdriver.Firefox(firefox_profile=profile, 
            capabilities=capabilities, options=options)
    elif browser == 'chrome':
        options = ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1200x600')
        capabilities = webdriver.DesiredCapabilities.CHROME.copy()
        capabilities['acceptSslCerts'] = True
        capabilities['acceptInsecureCerts'] = True
        wd = webdriver.Chrome(desired_capabilities=capabilities, options=options)
    elif browser == 'chead':
        options = ChromeOptions()
        options.add_argument('--start-maximized')
        capabilities = webdriver.DesiredCapabilities.CHROME.copy()
        capabilities['acceptSslCerts'] = True
        capabilities['acceptInsecureCerts'] = True
        wd = webdriver.Chrome(desired_capabilities=capabilities, options=options)
    elif browser == 'fhead':
        capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()
        capabilities['timeouts'] = {'implicit': 3000, 'pageLoad': 3000, 'script': 30000}
        capabilities['loggingPrefs'] = {'browser': 'ALL', 'client': 'ALL', 'driver': 'ALL',
                                        'performance': 'ALL', 'server': 'ALL'}
        profile = webdriver.FirefoxProfile()
        profile.set_preference('app.update.auto', False)
        profile.set_preference('app.update.enabled', False)
        profile.accept_untrusted_certs = True
        wd = webdriver.Firefox(firefox_profile=profile, capabilities=capabilities)
        wd.maximize_window()
    else:
        print('\n\nBrowser not supported!')
        sys.exit(1)

    wd.get(address)
    wd.implicitly_wait(30000)
    wd.set_page_load_timeout(int(request.config.getoption("--timeout")))
    yield wd

    wd.quit()

@pytest.fixture(scope="module")
def login_page(driver):
    """Docstring"""
    return LoginPage(driver)

@pytest.fixture(scope="function")
def login(login_page):
    """Docstring"""
    login_page.set_username("admin")
    login_page.set_password("12345")
    time.sleep(1)  # To prevent multiple data inputing in the fields in firefox

@pytest.fixture(scope="module")
def dashboard_page(driver):
    """Docstring"""
    return DashboardPage(driver)
