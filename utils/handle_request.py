import requests


def send(case):
    name = case['name']
    method = case['method'].upper()
    url = case['path']
    headers = eval(case['headers'])
    if method == 'GET':
        params = eval(case['param'])
        return requests.get(url=url, params=params, headers=headers).json()
    elif method == 'POST':
        if headers['Content-Type'] == 'application/x-www-form-urlencoded':
            data = case['data']
            return requests.post(url=url, data=data, headers=headers).json()
        if headers['Content-Type'] == 'application/json':
            json = eval(case['json'])
            return requests.post(url=url, json=json, headers=headers).json()
    elif method == 'PUT':
        if headers['Content-Type'] == 'application/x-www-form-urlencoded':
            data = case['data']
            return requests.put(url=url, data=data, headers=headers).json()
        if headers['Content-Type'] == 'application/json':
            json = eval(case['json'])
            return requests.put(url=url, json=json, headers=headers).json()
    elif method == 'DELETE':
        return requests.delete(url=url, headers=headers).json()