from scenarios import witness
from scenarios import educator

if __name__ == '__main__':
    try:
        witness.main()
        educator.main()
    except Warning:
        raise
