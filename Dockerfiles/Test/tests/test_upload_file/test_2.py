import time

import requests

import os

# os.path.dirname(__file__)
file_path = os.path.join('volume' 'file.txt')
# print(file_path)


def test_customer_1_upload_file():
    # response = requests.post('http://customer_1:8180/share/create/v1')

    # assert response.status_code == 200
    # assert response.json()['status'] == 'OK', response.json()

    # key_id = response.json()['result'][0]['key_id']
    key_id = 'master$customer1@is_8084'

    remote_path = '%s:%s' % (key_id, 'virtual_file.txt')

    response = requests.post('http://customer_1:8180/file/create/v1', json={'remote_path': remote_path})
    assert response.status_code == 200
    assert response.json()['status'] == 'OK', response.json()

    response = requests.post(
        'http://customer_1:8180/file/upload/start/v1',
        json={'remote_path': remote_path, 'local_path': '/volume/file.txt', 'wait_result': 'true'}
    )
    assert response.status_code == 200
    assert response.json()['status'] == 'OK', response.json()

    for i in range(100):
        response = requests.post(
            'http://customer_1:8180/file/download/start/v1',
            json={'remote_path': remote_path, 'destination_path': '/download_volume', 'wait_result': 'true'}
        )
        assert response.status_code == 200

        if response.json()['status'] == 'OK':
            break

        if response.json()['errors'][0].startswith('download not possible, uploading'):
            print('file is not ready for download: retry again in 1 sec')
            time.sleep(1)
        else:
            print(response.json())
            assert False, response.json()
    else:
        assert False, response.json()

        # assert response.json()['status'] == 'OK', response.json()
    print(response.json())
