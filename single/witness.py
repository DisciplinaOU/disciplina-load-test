from single.api import faucet
from single.api import explorer


# Creating account, filling through faucet and checking its balance with block explorer API
def create_fill_account():
    account = faucet.create_account()
    faucet.fill_account(account)
    account_info = explorer.get_account_info(account.address)
    if account_info['balances']['total'] == 20:
        print('Account creation and filling successful.')
    else:
        print('Failed to pass the account create/fill/check cycle')


def main():
    create_fill_account()
