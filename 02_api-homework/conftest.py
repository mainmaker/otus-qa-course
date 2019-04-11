import pytest
import requests


def pytest_collection_modifyitems(items, config):
    """Docsting"""
    fixture_name = config.option.address
    if fixture_name is not None:
        selected_items = []
        deselected_items = []

        for item in items:
            if fixture_name in getattr(item, 'fixturenames', ()):
                selected_items.append(item)
            else:
                deselected_items.append(item)
        config.hook.pytest_deselected(items=deselected_items)
        items[:] = selected_items
        if len(selected_items) == 0:
            print("Wrong URL")


def pytest_addoption(parser):
    """Docsting"""
    parser.addoption("--address",
                     action="store",
                     default=None,
                     help="just run tests that use a particular fixture")

@pytest.fixture
def dog():
    """Docsting"""
    return requests.get("https://dog.ceo/api/breeds/image/random")

@pytest.fixture
def brew():
    """Docsting"""
    return requests.get("https://api.openbrewerydb.org/breweries/5494")

@pytest.fixture
def cdn():
    """Docsting"""
    return requests.get("https://api.cdnjs.com/libraries?search=1140")
