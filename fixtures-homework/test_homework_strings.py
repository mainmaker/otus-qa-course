import pytest


@pytest.fixture()
def string_data():
    data = "Here goes some string"
    return data


def test_foo(string_data):
    """Slicing for first five items in the string."""
    print("\n{}".format(string_data))
    print("String slicing 1")
    assert string_data[:5] == "Here "

def test_bar(string_data):
    """Slicing for last five items in the string."""
    print("\n{}".format(string_data))
    print("String slicing 2")
    assert string_data[-5:] == "tring"

def test_baz(string_data):
    """Slicing for all items in the string except first and last five items."""
    print("\n{}".format(string_data))
    print("String slicing 3")
    assert string_data[5:-5] == "goes some s"
