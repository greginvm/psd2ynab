import datetime
import pprint

import buxfer
import settings
import ynab
import argparse


def get_args():
    parser = argparse.ArgumentParser('Sync buxfer to YNAB')
    parser.add_argument('--datefrom', type=lambda d: datetime.datetime.strptime(d, '%Y%m%d'))
    parser.add_argument('--days', type=int, default=1)
    parser.add_argument('--test', dest='test', action='store_true')
    return parser.parse_args()


def main():
    buxfer_token = buxfer.login()
    args = get_args()

    since = args.datefrom
    if not since:
        days = args.days
        since = datetime.date.today() - datetime.timedelta(days=days)
    print('Syncing transactions from {} until today'.format(since.isoformat()))
    for bx, yn in settings.ACCOUNT_MAPPING.items():
        txs = buxfer.get_transactions(buxfer_token, bx, since, datetime.date.today())
        ytxs = ynab.txs_bux_to_ynab(txs, yn)
        result = ynab.import_transactions(settings.YNAB_BUDGET, ytxs)
        pprint.pprint(result)


if __name__ == "__main__":
    main()
