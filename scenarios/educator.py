from scenarios.api import faucet
from scenarios.api import explorer
from scenarios.api import educator


def courses_cycle():
    # ---- creating new course
    test_course = {"desc": "TestCourse", "subjects": [0]}
    # TODO figure out the way of modifying the architecture
    # so it can handle scenarios like 'faulty input -> expected error code'
    int_course_id = educator.post_course(test_course)

    # ---- ensuring that new course is actually in the list
    list_courses = educator.get_courses()
    filtered = list(filter(lambda course: course['id'] == int_course_id, list_courses))
    if len(filtered) != 1 or filtered[0]['desc'] != "TestCourse":
        raise Warning('Fail - course create/check cycle')

    # ---- pulling exact course by course_id
    dict_course = educator.get_courses(int_course_id)
    if dict_course['desc'] != 'TestCourse':
        raise Warning('Fail - course create/check cycle - unexpected course description')

    # ---- deleting the created course
    # TODO: for now there is no endpoint for course deletion. Discuss it with devs.

    print('OK - course create/check cycle')


def student_cycle():
    # ---- creating&filling new wallet
    account = faucet.create_account()
    address = account.get_address()
    faucet.fill_account(account)

    # ---- add new student address
    test_student = {"addr": address}
    educator.post_student(test_student)

    # ---- ensuring that new student is actually in the list
    students = educator.get_students_list()
    filtered = list(filter(lambda student: student['addr'] == address, students))
    if len(filtered) != 1 or filtered[0]['addr'] != address:
        raise Warning('Fail - student create/check/delete cycle')

    # FIXME: deleting isn't implemented in endpoints. Documents are way in the future
    # ---- deleting the address
    educator.delete_student(address)

    # ---- ensuring its deleted
    # students = educator.get_students_list()
    # filtered = list(filter(lambda student: student['addr'] == address, students))
    # if len(filtered) != 0:
    #     raise Warning('Fail - student create/check/delete cycle')
    print('OK - student create/check/delete cycle')


# TODO rename me
def assignments_cycle():
    assignments = educator.get_assignments_list()


def main():
    courses_cycle()
    student_cycle()
