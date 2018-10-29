from single.api import educator


def courses_cycle():
    courses = educator.get_courses_list()
    print(courses)


def main():
    print('placeholder for educator scenarios')
