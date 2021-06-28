import requests
from utils.handle_config import get_config
from utils.handle_log import logger


def send(case):
    name = case['name']
    logger.info('[{}]->正在处理数据，请稍等...'.format(name))
    method = case['method'].upper()
    url = get_config('environment')['base_url'] + case['path']
    headers = eval(case['headers'])
    if method == 'GET':
        params = eval(case['param'])
        logger.info('[{}]->数据处理完毕！'.format(name))
        logger.info('[{}]->正在发送请求，请稍等...'.format(name))
        return requests.get(url=url, params=params, headers=headers).json()
    elif method == 'POST':
        if headers['Content-Type'] == 'application/x-www-form-urlencoded':
            data = case['data']
            logger.info('[{}]->数据处理完毕！'.format(name))
            logger.info('[{}]->正在发送请求，请稍等...'.format(name))
            return requests.post(url=url, data=data, headers=headers).json()
        if headers['Content-Type'] == 'application/json':
            json = eval(case['json'])
            logger.info('[{}]->数据处理完毕！'.format(name))
            logger.info('[{}]->正在发送请求，请稍等...'.format(name))
            return requests.post(url=url, json=json, headers=headers).json()
    elif method == 'PUT':
        if headers['Content-Type'] == 'application/x-www-form-urlencoded':
            data = case['data']
            logger.info('[{}]->数据处理完毕！'.format(name))
            logger.info('[{}]->正在发送请求，请稍等...'.format(name))
            return requests.put(url=url, data=data, headers=headers).json()
        if headers['Content-Type'] == 'application/json':
            json = eval(case['json'])
            logger.info('[{}]->数据处理完毕！'.format(name))
            logger.info('[{}]->正在发送请求，请稍等...'.format(name))
            return requests.put(url=url, json=json, headers=headers).json()
    elif method == 'DELETE':
        logger.info('[{}]->数据处理完毕！'.format(name))
        logger.info('[{}]->正在发送请求，请稍等...'.format(name))
        return requests.delete(url=url, headers=headers).json()