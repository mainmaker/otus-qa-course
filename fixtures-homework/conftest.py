import pytest


@pytest.fixture(scope="session", autouse=True)
def once_per_session():
    print('\n\nGentlemen, start your engines.')

    def once_per_session_at_the_end():
    	print("\n\nIT WAS GREAT! Let's do it again!")

    yield

    once_per_session_at_the_end()


@pytest.fixture(scope="module", autouse=True)
def once_per_module():
    print('\nOnce per module')
