# About

This is a rather rudimentary script that syncs transactions from [Buxfer](https://www.buxfer.com/pricing) to [YNAB](https://www.youneedabudget.com). 
I have written these to add the missing EU financial institutions automatic import feature (known also as PSD2 APIs) to YNAB. 
Buxfer integrates with [SaltEdge](https://www.saltedge.com/products/psd2_account_info), who is an aggregator for these APIs and they support a lot of them.

NOTE: I have abandoned the project since I eventually realized that banks that I use are on the [Shitty Bank List](https://toshl.com/blog/shitty-bank-list/). In my case they do not provide transaction descriptions which makes the imported transactions too cryptic.

__WARNING__: You need to pay for Buxfer (see Plus plan that enables "Automatic Bank Sync"), it costs about $4.00/month.

# Usage

## Credentials

```
cp bridge/setting.py.template bridge/settings.py
```

- YNAB: Use [Personal Access Tokens](https://api.youneedabudget.com/#personal-access-tokens) and put it into `settings.py`
- Buxfer: Get the API token and put it into `settings.py`

## Run

```
pipenv install
pipenv shell
python3 bridge/sync.py --days 3 
```

## Use

put it into crontab