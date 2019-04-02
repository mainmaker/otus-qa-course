import pytest


@pytest.fixture()
def dict_data():
    data = {"alfa": 1, "beta": 2, "gamma": 3}
    return data


def test_foo(dict_data):
    """Checking for an identity of the item in the dictionary."""
    print("\n{}".format(dict_data))
    print("Dictionary 1")
    assert dict_data["alfa"] == 1

def test_bar(dict_data):
    """Checking for existance of the item in the dictionary."""
    print("\n{}".format(dict_data))
    print("Dictionary 2")
    assert ("beta" in dict_data) == True

def test_baz(dict_data):
    """Checking for the length of the dictionary"""
    print("\n{}".format(dict_data))
    print("Dictionary 3")
    assert len(dict_data) == 3
