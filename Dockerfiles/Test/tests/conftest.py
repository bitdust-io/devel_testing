import pytest
import requests
import time


@pytest.yield_fixture(scope='session', autouse=True)
def timeout_before_tests_to_activate_bitdust():
    print('timeout_before_tests_to_activate_bitdust before')
    time.sleep(20)
    yield
    print('timeout_before_tests_to_activate_bitdust after')


@pytest.fixture(scope='session', autouse=True)
def supplier_1_init(timeout_before_tests_to_activate_bitdust):
    response = requests.post('http://supplier_1:8180/identity/create/v1', json={'username': 'supplier_1'})

    assert response.status_code == 200
    assert response.json()['status'] == 'OK'

    response = requests.get('http://supplier_1:8180/network/connected/v1?wait_timeout=5')
    assert response.json()['status'] == 'ERROR'

    for i in range(5):
        response = requests.get('http://supplier_1:8180/network/connected/v1?wait_timeout=5')
        if response.json()['status'] == 'OK':
            print("supplier_1_init: got status OK")
            break

        print("supplier_1_init: sleep 1 sec")
        time.sleep(1)
    else:
        assert False


@pytest.fixture(scope='session', autouse=True)
def supplier_2_init(timeout_before_tests_to_activate_bitdust):
    response = requests.post('http://supplier_2:8180/identity/create/v1', json={'username': 'supplier_2'})

    assert response.status_code == 200
    assert response.json()['status'] == 'OK'

    response = requests.get('http://supplier_2:8180/network/connected/v1?wait_timeout=5')
    assert response.json()['status'] == 'ERROR'

    for i in range(5):
        response = requests.get('http://supplier_2:8180/network/connected/v1?wait_timeout=5')
        if response.json()['status'] == 'OK':
            print("supplier_2_init: got status OK")
            break

        print("supplier_2_init: sleep 1 sec")
        time.sleep(1)
    else:
        assert False


@pytest.fixture(scope='session', autouse=True)
def proxy_server_1_init(timeout_before_tests_to_activate_bitdust):
    response = requests.post('http://proxy_server_1:8180/identity/create/v1', json={'username': 'proxy_server_1'})

    assert response.status_code == 200
    assert response.json()['status'] == 'OK'

    response = requests.get('http://proxy_server_1:8180/network/connected/v1?wait_timeout=5')
    assert response.json()['status'] == 'ERROR'

    for i in range(5):
        response = requests.get('http://proxy_server_1:8180/network/connected/v1?wait_timeout=5')
        if response.json()['status'] == 'OK':
            print("proxy_server_1_init: got status OK")
            break

        print("proxy_server_1_init: sleep 1 sec")
        time.sleep(1)
    else:
        assert False


@pytest.fixture(scope='session', autouse=True)
def proxy_server_2_init(timeout_before_tests_to_activate_bitdust):
    response = requests.post('http://proxy_server_2:8180/identity/create/v1', json={'username': 'proxy_server_2'})

    assert response.status_code == 200
    assert response.json()['status'] == 'OK'

    response = requests.get('http://proxy_server_2:8180/network/connected/v1?wait_timeout=5')
    assert response.json()['status'] == 'ERROR'

    for i in range(5):
        response = requests.get('http://proxy_server_2:8180/network/connected/v1?wait_timeout=5')
        if response.json()['status'] == 'OK':
            print("proxy_server_2_init: got status OK")
            break

        print("proxy_server_2_init: sleep 1 sec")
        time.sleep(1)
    else:
        assert False
