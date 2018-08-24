import requests
import json
import settings


def get_account_info(address):
    r = requests.get(settings.EXPLORER_ACCOUNT_INFO + address, verify=False)  # SSLError occurs, so verify=False
    if r.status_code == 200:
        data = json.loads(r.text)
        return data
    else:
        raise Warning('While checking the account info we got non 200 code')


def check_accounts_balance(accounts):
    print('----------------------')
    for account in accounts:
        account_info = get_account_info(account.address)
        if account.theoretical_balance != account_info['balances']['total']:
            print('! Got wrong balance')
    print('----------------------')
    print('Balance checks done. If there were no "wrong balance" messages - everything is ok')


def get_blocks():
    r = requests.get(settings.EXPLORER_BLOCKS, verify=False)  # SSLError occurs, so verify=False
    if r.status_code == 200:
        print('Successfully retrieved blocks')
    else:
        raise Warning('GET api/witness/v1/blocks returned non 200')


def get_recent_transactions():
    r = requests.get(settings.EXPLORER_TRANSACTIONS, verify=False)  # SSLError occurs, so verify=False
    if r.status_code == 200:
        print('Successfully retrieved recent transactions')
    else:
        raise Warning('GET api/witness/v1/transactions returned non 200')


def api_test():
    get_blocks()
    get_recent_transactions()