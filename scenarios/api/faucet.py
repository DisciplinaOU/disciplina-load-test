import requests
import json
import os
import settings


class Account:

    def __init__(self, private, public, address):
        self.private = private
        self.public = public
        self.address = address

    def get_address(self):
        return self.address

    def to_string(self):
        return '{ public:' + self.public + ', private:' + self.private + ', address:' + self.address + '}, \n'


def create_account():
    r = requests.post(settings.FAUCET_BASE_URL + settings.FAUCET_CREATE_WALLET_URL, json={})
    if r.status_code == 200:
        data = json.loads(r.text)
        return Account(data['secretKey'], data['publicKey'], data['address'])
    else:
        raise Warning('POST ' + settings.FAUCET_CREATE_WALLET_URL + ' returned non 200 code')


def fill_account(account):
    payload = {"destination": account.get_address()}
    r = requests.post(settings.FAUCET_BASE_URL + settings.FAUCET_TRANSFER_URL, json=payload)
    if r.status_code == 200:
        account.theoretical_balance = 20
    else:
        raise Warning('POST ' + settings.FAUCET_TRANSFER_URL + ' with body ' + str(payload) + ' returned non 200 code')


def write_accounts_to_file(accounts):
    if not os.path.exists('output'):
        os.makedirs('output')
    accounts_file = open('output/accounts.txt', "w+")
    for account in accounts:
        accounts_file.write(account.to_string())
    accounts_file.close()
