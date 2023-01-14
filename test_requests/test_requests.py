import json
from urllib.parse import urlencode

import urllib3

URL = 'http://127.0.0.1:5000/get_form?'
http = urllib3.PoolManager()

def main(test_data):
    for item in test_data:
        encoded_args = urlencode(item)
        response = http.request('POST', URL + encoded_args)
        response_form = json.loads(response.data.decode('utf-8'))
        print(f'REQUEST\n{item}\nRESPONSE\n{response_form}')
        print('-------------------------')


if __name__ == '__main__':
    with open('test_requests/test_data.json', 'r') as f:
        test_data = json.load(f)
    main(test_data)