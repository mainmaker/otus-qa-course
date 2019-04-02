import pytest


@pytest.fixture()
def set_data():
    data = {1, "12312", 123.22, (1, 2)}
    return data


def test_foo(set_data):
    """Checking for an identity of two sets."""
    print("\n{}".format(set_data))
    print("Sets 1")
    assert set_data == {(1, 2), 1, 123.22, "12312"}

def test_bar(set_data):
    """Checking for a specific difference between two sets."""
    print("\n{}".format(set_data))
    print("Sets 2")
    assert set_data.difference({(1, 2), 1, 123.22}) == {"12312"}

def test_baz(set_data):
    """Checking for the length of the set."""
    print("\n{}".format(set_data))
    print("Sets 3")
    assert len(set_data) == 4
