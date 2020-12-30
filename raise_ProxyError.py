import requests

proxy = {'http' : '145.54.234.43:8000', \
		 'https' : '145.54.234.43:8000'}

def custom_server(login, password):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    }
    status = False
    while True:
        # noinspection PyBroadException
        payload = {'email': login, 'pass': password}
        try:
            response = requests.post('https://vk.com/', data=payload, headers=headers, proxies=proxy)
            raise ProxyError
            status_code = str(response.status_code)
            if status_code == '401':
                pass
            elif status_code == '403':
                status = False
                # This query was been forbidden. Retrying
                # Этот запрос был отклонён. Повторяю
                continue
            if status_code.startswith('3'):  # or ('token' in response.text):
                status = True
                break
            elif status_code.startswith('4') and (status_code != ('401' or '403')):
                status = False
                # Server error
                time.sleep(10)
                continue
            elif status_code.startswith('5'):
                status = False
                # Client error
                time.sleep(10)
            else:
                status = False
                break
        except ConnectionError:
            status = False
            time.sleep(2)
        except TimeoutError:
            status = False
            time.sleep(60)
        # посмотреть, как правильно называется ошибка
    return status

custom_server('89170050729', 'henry228337')