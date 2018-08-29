from faucet import faucet
from explorer import explorer


def main():
    accounts = faucet.main(3)
    explorer.check_accounts_balance(accounts)
    explorer.api_test()
    

if __name__ == '__main__':
    try:
        main()
    except Warning:
        raise