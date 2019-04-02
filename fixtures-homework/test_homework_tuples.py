import pytest


@pytest.fixture()
def tuple_data():
    data = (1, 2, 3, 4, 5)
    return data


def test_foo(tuple_data):
    """Checking for tuple identity."""
    print("\n{}".format(tuple_data))
    print("Tuples 1")
    assert tuple_data == (1, 2, 3, 4, 5)

def test_bar(tuple_data):
    """Checking for an identity of the item in the tuple."""
    print("\n{}".format(tuple_data))
    print("Tuples 2")
    assert tuple_data[3] == 4

def test_baz(tuple_data):
    """Checking for the length of the tuple."""
    print("\n{}".format(tuple_data))
    print("Tuples 3")
    assert len(tuple_data) == 5
