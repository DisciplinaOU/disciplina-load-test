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


def post_student(studentObj):
    r = requests.post(settings.EDUCATOR_BASE_URL + settings.EDUCATOR_STUDENTS_LIST, json=studentObj)
    if r.status_code == 201:
        # properly created course
        data = json.loads(r.text)
        return data
    elif r.status_code == 400:
        print(r)
    else:
        raise Warning('POST /students unhandled error code')


def delete_student(studentAddr):
    r = requests.delete(settings.EDUCATOR_BASE_URL + settings.EDUCATOR_STUDENTS_LIST + '/' + studentAddr)
    if r.status_code == 200:
        return True
    elif r.status_code == 500:
        print('DELETE /students/{student} returned 500. Probably not implemented yet')


# Assigns a new assignment to a student
def assign_assignment_to_student(student):
    url = settings.EDUCATOR_BASE_URL


def get_courses(course_id=None):
    url = settings.EDUCATOR_BASE_URL + settings.EDUCATOR_COURSES_LIST
    if course_id is not None:
        url += '/' + str(course_id)
    r = requests.get(url)
    if r.status_code == 200:
        data = json.loads(r.text)
        return data
    else:
        raise Warning('GET ' + settings.EDUCATOR_COURSES_LIST + ' returned non 200 code')


def post_course(courseObj):
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


def get_assignments_list(student=None):
    url = settings.EDUCATOR_BASE_URL + settings.EDUCATOR_ASSIGNMENTS_LIST
    if student is not None and isinstance(student, str):
        url += '&student=' + student
    r = requests.get(url)
    if r.status_code == 200:
        data = json.loads(r.text)
        return data
    else:
        raise Warning('GET' + settings.EDUCATOR_ASSIGNMENTS_LIST + ' returned non 200')


def get_proofs_list():
    r = requests.get(settings.EDUCATOR_BASE_URL + settings.EDUCATOR_PROOFS_LIST)
    if r.status_code == 200:
        print('list successful')
        # TODO: format data.
    else:
        raise Warning('While getting proofs we got non 200 code')
