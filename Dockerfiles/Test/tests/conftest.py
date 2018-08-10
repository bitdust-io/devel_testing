import pytest
import requests
import time


@pytest.yield_fixture(scope='session', autouse=True)
def timeout_before_tests_to_activate_bitdust():
    # Code that will run before your test, for example:
    time.sleep(20)
    # A test function will be run at this point
    yield
    # Code that will run after your test, for example:
    # files_after = # ... do something to check the existing files
    # assert files_before == files_after


@pytest.fixture(scope='session', autouse=True)
def identity_create():
    # time.sleep(20)
    response = requests.post('http://supplier_1:8180/identity/create/v1', json={'username': 'identity_node1'})

    assert response.status_code == 200
    print("supplier_1", response.content)
    #
    # response = requests.post('http://supplier_2:8180/identity/create/v1', json={'username': 'identity_node2'})
    #
    # assert response.status_code == 200
    # print("supplier_2", response.content)


@pytest.fixture(scope='session', autouse=True)
def identity_create_2():
    response = requests.post('http://supplier_2:8180/identity/create/v1', json={'username': 'identity_node2'})

    assert response.status_code == 200
    print("supplier_2", response.content)
