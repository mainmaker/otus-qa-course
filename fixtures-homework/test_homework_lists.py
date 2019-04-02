import pytest


@pytest.fixture()
def list_data():
    data = [1, 2, 3, 4, 5]
    return data


def test_foo(list_data):
    """Checking for an identity of the last item in the list."""
    print("\n{}".format(list_data))
    print("List slicing 1")
    assert list_data[-1] == 5

def test_bar(list_data):
    """Slicing for every even item in the list between 2nd and 5th items."""
    print("\n{}".format(list_data))
    print("List slicing 2")
    assert list_data[1:4:2] == [2, 4]

def test_baz(list_data):
    """Reversing of the list."""
    print("\n{}".format(list_data))
    print("List slicing 3")
    assert list_data[::-1] == [5, 4, 3, 2, 1]
