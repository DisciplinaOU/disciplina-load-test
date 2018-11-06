from scenarios.api import faucet
from scenarios.api import explorer
from scenarios.api import educator


def courses_cycle():
    # ---- creating new course
    test_course = {"desc": "TestCourse", "subjects": [0]}
    # TODO figure out the way of modifying the architecture
    # so it can handle scenarios like 'faulty input -> expected error code'
    int_course_id = educator.post_create_course(test_course)

    # ---- ensuring that new course is actually in the list
    list_courses = educator.get_courses_list()
    filtered = list(filter(lambda course: course['id'] == int_course_id, list_courses))
    if len(filtered) != 1 or filtered[0]['desc'] != "TestCourse":
        raise Warning('Fail - course create/check cycle')

    # ---- pulling exact course by course_id
    dict_course = educator.get_courses_list(int_course_id)
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
    educator.post_add_student(test_student)

    # ---- ensuring that new student is actually in the list
    students = educator.get_students_list()
    filtered = list(filter(lambda student: student['addr'] == address, students))
    if len(filtered) != 1 or filtered[0]['addr'] != address:
        raise Warning('Fail - student create/check/delete cycle')

    # FIXME: deleting isn't implemented in endpoints. Documents are describing the future
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
    test_course = {"desc": "TestCourse", "subjects": [0]}
    int_course_id = educator.post_create_course(test_course)

    account = faucet.create_account()
    faucet.fill_account(account)

    educator.post_add_student({"addr": account.get_address()})

    educator.post_enroll_student_in_course(account.get_address(), int_course_id)

    # FIXME talked with @martoon about isFinal. It will be fixed with the next merge
    test_assignment = {
        "courseId": int_course_id,
        "contentsHash": "7b6d0c6de38639cc6063e9c36f9dcdb71fff60fe551ccc757246a3bf2fa00f37",
        "isFinal": {
            "isFinal": False
        },
        "desc": "Test assignment"
    }
    educator.post_create_assignment(test_assignment)
    assignments = educator.get_assignments_list(course=int_course_id)
    if len(assignments) > 0:
        print('OK - assignments cycle')


def main():
    student_cycle()
    courses_cycle()
    assignments_cycle()
