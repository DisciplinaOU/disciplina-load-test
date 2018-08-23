from faucet import faucet


def main():
    faucet.main(1)


if __name__ == '__main__':
    try:
        main()
    except Warning:
        raise