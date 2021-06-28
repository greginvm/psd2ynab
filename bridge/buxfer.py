import requests

import settings


def checkError(response):
    response = response['response']
    if response['status'] != "OK":
        raise Exception('Buxfer not OK')

    return response


base = "https://www.buxfer.com/api"


def login():
    url = base + "/login"
    r = requests.post(url, json={'username': settings.BUXFER_USER, 'password': settings.BUXFER_PASS})
    r.raise_for_status()
    r = r.json()
    checkError(r)
    return r['response']['token']


def get_transactions(token, account_name, date_from, date_to):
    txs = []
    page = 1
    while True:
        t = _get_transactions_page(token, account_name, date_from, date_to, page)
        if not t:
            break
        txs.extend(t)
        page += 1
    return txs


def _get_transactions_page(token, account_name, date_from, date_to, page=1):
    url = base + "/transactions"
    r = requests.get(url, params={'token': token,
                                  'page': page, 'accountName': account_name, 'startDate': date_from.isoformat(),
                                  'endDate': date_to.isoformat()})
    r.raise_for_status()
    r = r.json()
    checkError(r)
    return r['response']['transactions']
