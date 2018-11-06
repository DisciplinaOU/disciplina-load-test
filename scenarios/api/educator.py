import requests
import json
import settings
from random import randint


def get_students_list():
    r = requests.get(settings.EDUCATOR_BASE_URL + settings.EDUCATOR_STUDENTS_LIST)
    if r.status_code == 200:
        data = json.loads(r.text)
        return data
    else:
        raise Warning('GET ' + settings.EDUCATOR_STUDENTS_LIST + ' returned non 200 code')


def post_add_student(student_obj):
    r = requests.post(settings.EDUCATOR_BASE_URL + settings.EDUCATOR_STUDENTS_LIST, json=student_obj)
    if r.status_code == 201:
        # properly created course
        data = json.loads(r.text)
        return data
    elif r.status_code == 400:
        print(r)
    else:
        raise Warning('POST /students unhandled error code')


def post_enroll_student_in_course(student_addr, course_id):
    payload = {"courseId": course_id}
    url = settings.EDUCATOR_BASE_URL + settings.EDUCATOR_STUDENTS_LIST
    url += '/' + student_addr + '/courses'
    r = requests.post(url, json=payload)
    if r.status_code == 201:
        # properly enrolled student into given course
        return 0
    else:
        raise Warning(str('POST ' + settings.EDUCATOR_STUDENTS_LIST + '/' + student_addr + '/courses unhandled error code'))


def delete_student(studentAddr):
    r = requests.delete(settings.EDUCATOR_BASE_URL + settings.EDUCATOR_STUDENTS_LIST + '/' + studentAddr)
    if r.status_code == 200:
        return True
    elif r.status_code == 500:
        print('DELETE /students/{student} returned 500. Probably not implemented yet')


# Assigns a new assignment to a student
def assign_assignment_to_student(student):
    url = settings.EDUCATOR_BASE_URL


def get_courses_list(course_id=None):
    url = settings.EDUCATOR_BASE_URL + settings.EDUCATOR_COURSES_LIST
    if course_id is not None:
        url += '/' + str(course_id)
    r = requests.get(url)
    if r.status_code == 200:
        data = json.loads(r.text)
        return data
    else:
        raise Warning('GET ' + settings.EDUCATOR_COURSES_LIST + ' returned non 200 code')


def post_create_course(courseObj):
    r = requests.post(settings.EDUCATOR_BASE_URL + settings.EDUCATOR_COURSES_LIST, json=courseObj)
    if r.status_code == 201:
        # properly created course
        data = json.loads(r.text)
        return data
    elif r.status_code == 400:
        print(r)
    else:
        raise Warning('POST ' + settings.EDUCATOR_COURSES_LIST + ' unhandled error code')


def get_submissions_list():
    r = requests.get(settings.EDUCATOR_BASE_URL + settings.EDUCATOR_SUBMISSIONS_LIST)
    if r.status_code == 200:
        print('list successful')
        # TODO: format data.
    else:
        raise Warning('While getting submissions we got non 200 code')


def get_grades_list():
    r = requests.get(settings.EDUCATOR_BASE_URL + settings.EDUCATOR_GRADES_LIST)
    if r.status_code == 200:
        data = json.loads(r.text)
        return data
    else:
        raise Warning('GET ' + settings.EDUCATOR_GRADES_LIST + ' returned non 200 code')


def get_assignments_list(**kwargs):
    url = settings.EDUCATOR_BASE_URL + settings.EDUCATOR_ASSIGNMENTS
    if len(kwargs) > 0:
        url += '?'
        for key, value in kwargs.items():
            url += str(key) + '=' + str(value) + '&'
        url = url[:-1]
    r = requests.get(url)
    if r.status_code == 200:
        data = json.loads(r.text)
        return data
    else:
        raise Warning('GET ' + settings.EDUCATOR_ASSIGNMENTS + ' returned non 200')


def post_create_assignment(assignment_obj):
    url = settings.EDUCATOR_BASE_URL + settings.EDUCATOR_ASSIGNMENTS
    url += '?autoAssign=false'
    r = requests.post(url, json=assignment_obj)
    if r.status_code == 201:
        return True
    else:
        raise Warning('POST ' + settings.EDUCATOR_ASSIGNMENTS + ' returned unhandled code (non 201)')


def get_proofs_list():
    r = requests.get(settings.EDUCATOR_BASE_URL + settings.EDUCATOR_PROOFS_LIST)
    if r.status_code == 200:
        print('list successful')
        # TODO: format data.
    else:
        raise Warning('While getting proofs we got non 200 code')
