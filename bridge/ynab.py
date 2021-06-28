import requests
import settings

base = 'https://api.youneedabudget.com/v1'


def _get_import_id(ytx):
    return 'YNAB:{}:{}:{}'.format(
        ytx['amount'],
        ytx['date'],
        1
    )


def _get_amount(btx):
    number = btx['amount']
    number *= 1000.0
    number = int(number)

    if btx['type'] in ['expense', 'transfer', 'investment_buy', 'sharedBill', 'paidForFriend']:
        return number * -1
    return number


def txs_bux_to_ynab(btxs, account_id):
    ytxs = []
    for btx in btxs:
        yt = {
            'account_id': account_id,
            'date': btx['date'],
            'amount': _get_amount(btx),
            'payee_name': ' '.join(btx['description'].split(' ')[:-1]),
            'approved': False,
            'flag_color': 'yellow',
            'cleared': 'uncleared',
        }
        yt['import_id'] = _get_import_id(yt)
        ytxs.append(yt)
    return ytxs


def import_transactions(budget_id, ytxs):
    r = requests.post(base + '/budgets/{}/transactions'.format(budget_id), json={'transactions': ytxs},
                      headers={'Authorization': 'Bearer {}'.format(settings.YNAB_TOKEN)})
    print(r.json())
    r.raise_for_status()
    return r.json()['data']['transactions']
