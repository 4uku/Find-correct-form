import json
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

BASE_DIR = Path(__file__).parent
URL = 'http://127.0.0.1:5000/get_form?'

def main(test_data):
    for item in test_data:
        encoded_args = urlencode(item)
        # response = http.request('POST', URL + encoded_args)
        request = Request(URL + encoded_args, method='POST')
        with urlopen(request) as response:
            response_form = response.read().decode('utf-8')
        print(f'REQUEST\n{item}\nRESPONSE\n{response_form}')
        print('-------------------------')


if __name__ == '__main__':
    with open(BASE_DIR / 'test_data.json', 'r') as f:
        test_data = json.load(f)
    main(test_data)