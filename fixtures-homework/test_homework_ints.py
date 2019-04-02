import pytest


@pytest.fixture()
def string_data():
    data = (1, 2, 3, 4, 5)
    return data


def test_foo(string_data):
    """Checking for an identity of the addition of two integers."""
    print("\n{}".format(string_data))
    print("Integers 1")
    assert string_data[0] + string_data[1] == 3

def test_bar(string_data):
    """Checking for an identity of the subtraction of two integers."""
    print("\n{}".format(string_data))
    print("Integers 2")
    assert string_data[1] - string_data[0] == 1

def test_baz(string_data):
    """Checking for an identity of the summing of all integers in the tuple."""
    print("\n{}".format(string_data))
    print("Integers 3")
    assert sum(string_data) == 15
