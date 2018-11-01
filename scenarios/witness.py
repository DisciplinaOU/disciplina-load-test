from scenarios.api import faucet
from scenarios.api import explorer


# Creating account, filling through faucet and checking its balance with block explorer API
def create_fill_account():
    account = faucet.create_account()
    faucet.fill_account(account)
    account_info = explorer.get_account_info(account.get_address())
    if account_info['balances']['total'] == 20:
        print('OK - create/fill/check cycle')
    else:
        print('Fail - account create/fill/check cycle')


def main():
    create_fill_account()
