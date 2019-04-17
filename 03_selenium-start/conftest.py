import sys
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.firefox.options import Options


def pytest_addoption(parser):
    """Docstring"""
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--address", action="store", default="http://165.22.10.232/opencart/")

@pytest.fixture(scope="session", autouse=True)
def driver(request):
    """Docstring"""
    browser = request.config.getoption("--browser")
    if browser == 'firefox':
        options = Options()
        options.headless = True
        wd = webdriver.Firefox(options=options)
        wd.get(request.config.getoption("--address"))
    elif browser == 'chrome':
        options = ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1200x600')
        wd = webdriver.Chrome(options=options)
        wd.get(request.config.getoption("--address"))
    else:
        print('\n\nBrowser not supported!')
        sys.exit(1)

    yield wd

    wd.quit()
