import requests


def test_ping():
    idurl_ = 'http://is:8084/identity_node2.xml'
    id = 'identity_node2@is_8084'
    print('test_ping')
    response = requests.get('http://supplier_1:8180/user/ping/v1?id=%s' % id)

    assert response.status_code == 200
    print(response.content)
    # assert 1 == 1
