from single import faucet
from single import explorer
from single import student


def main():
    # accounts = faucet.main(3)
    # explorer.check_accounts_balance(accounts)
    # explorer.api_test()
    student.main()


if __name__ == '__main__':
    try:
        main()
    except Warning:
        raise