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
        raise Warning('While getting students list we got non 200 code')


def get_courses_list():
    r = requests.get(settings.EDUCATOR_BASE_URL + settings.EDUCATOR_COURSES_LIST)
    if r.status_code == 200:
        data = json.loads(r.text)
        return data
    else:
        raise Warning('While getting courses list we got non 200 code')


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
        print('list successful')
        # TODO: format data.
    else:
        raise Warning('While getting grades we got non 200 code')


def get_assignments_list():
    r = requests.get(settings.EDUCATOR_BASE_URL + settings.EDUCATOR_ASSIGNMENTS_LIST)
    if r.status_code == 200:
        print('list successful')
        # TODO: format data.
    else:
        raise Warning('While getting assignments we got non 200 code')


def get_proofs_list():
    r = requests.get(settings.EDUCATOR_BASE_URL + settings.EDUCATOR_PROOFS_LIST)
    if r.status_code == 200:
        print('list successful')
        # TODO: format data.
    else:
        raise Warning('While getting proofs we got non 200 code')