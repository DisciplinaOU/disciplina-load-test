from faucet import faucet
from explorer import explorer


def main():
    accounts = faucet.main(1)
    explorer.check_accounts_balance(accounts)


if __name__ == '__main__':
    try:
        main()
    except Warning:
        raise