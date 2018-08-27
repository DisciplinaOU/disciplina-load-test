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
    r = requests.post(settings.FAUCET_CREATE_WALLET_URL, json={})
    if r.status_code == 200:
        data = json.loads(r.text)
        return Account(data['secretKey'], data['publicKey'], data['address'])
    else:
        raise Warning('While creating account we got non 200 code')


def spam_account_create(count):
    accounts = []
    for i in range(0, count):
        accounts.append(create_account())
    print('Finished creating accounts.')
    return accounts


def get_some_account_addresses(count):
    addresses = []
    for account in spam_account_create(count):
        addresses.append(account.address)
    return addresses


def fill_accounts(accounts):
    for account in accounts:
        r = requests.post(settings.FAUCET_TRANSFER_URL, json={"destination": account.address})
        if r.status_code == 200:
            account.theoretical_balance = 20
        else:
            raise Warning('While filling account with money we got non 200 code')
    print('Filling done')


def write_accounts_to_file(accounts):
    if not os.path.exists('output'):
        os.makedirs('output')
    accounts_file = open('output/accounts.txt', "w+")
    for account in accounts:
        accounts_file.write(account.to_string())
    accounts_file.close()


def main(count):
    print('Creating ' + str(count) + ' accounts.')
    accounts = spam_account_create(count)
    print('Acquiring money.')
    fill_accounts(accounts)
    print('Writing accounts data to output/accounts.txt')
    write_accounts_to_file(accounts)
    return accounts

