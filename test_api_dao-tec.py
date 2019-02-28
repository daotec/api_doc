# coding=utf-8

import json
import hmac
import hashlib
import requests
import test_api_key_x


def get_api_key():
    api_key = test_api_key_x.API_KEY
    secret_key = test_api_key_x.SECRET_KEY
    return api_key, secret_key


def request(api, method, params, secret_key):
    url = "https://www.dao-tec.com/api/v1/{}".format(api)
    headers = {'contentType': 'application/x-www-form-urlencoded'}
    params['secret_key'] = secret_key
    content = json.dumps(params)
    sig = hmac.new(secret_key.encode("utf8"), msg=content.encode("utf8"),
                   digestmod=hashlib.sha256).hexdigest()
    params['signature'] = sig
    if (method == 'get'):
        payload = ''
        for key in params.keys():
            payload += key + '=' + str(params[key]) + '&'
        url = '{}?{}'.format(url, payload)
        response = requests.get(url, headers=headers)
    elif (method == 'post'):
        response = requests.post(url, headers=headers, data=params)
    elif (method == 'delete'):
        response = requests.delete(url, headers=headers, data=params)
    true = True
    false = False
    resp = response.content
    resp = json.loads(resp)
    return resp


def test_balances():
    method = 'get'
    api_key, secret_key = get_api_key()
    params = {}
    params['api_key'] = api_key
    params['exchange'] = 'okex'
    params['account_type'] = 'api_bind'
    params['symbol'] = 'eos_usdt'
    params['strategy_name'] = 'manual_trading'
    secret_key = secret_key
    rst = request('balances', method, params, secret_key)
    print(rst)


def test_post_orders():
    method = 'post'
    api_key, secret_key = get_api_key()
    params = {}
    params['api_key'] = api_key
    params['exchange'] = 'okex'
    params['account_type'] = 'api_bind'
    params['symbol'] = 'eos_usdt'
    params['strategy_name'] = 'manual_trading'
    params['order_type'] = 'sell_limit'
    params['price'] = '5.1'
    params['amount'] = '0.3'
    params['money_num'] = '0'
    secret_key = secret_key
    rst = request('orders', method, params, secret_key)
    print(rst)


def test_get_orders():
    method = 'get'
    api_key, secret_key = get_api_key()
    params = {}
    params['api_key'] = api_key
    params['exchange'] = 'okex'
    params['account_type'] = 'api_bind'
    params['symbol'] = 'eos_usdt'
    params['strategy_name'] = 'manual_trading'
    params['order_id'] = '2382399339367424'
    secret_key = secret_key
    rst = request('orders', method, params, secret_key)
    print(rst)


def test_delete_orders():
    method = 'delete'
    api_key, secret_key = get_api_key()
    params = {}
    params['api_key'] = api_key
    params['exchange'] = 'okex'
    params['account_type'] = 'api_bind'
    params['symbol'] = 'eos_usdt'
    params['strategy_name'] = 'manual_trading'
    params['order_id'] = '2382399339367424'
    secret_key = secret_key
    rst = request('orders', method, params, secret_key)
    print(rst)


def main():
    test_balances()
    # test_post_orders()
    # test_get_orders()
    # test_delete_orders()
    pass


if __name__ == '__main__':
    main()
