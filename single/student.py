import requests
import json
import settings
from random import randint


def get_student_courses():
    r = requests.get(settings.STUDENT_COURSES)
    if r.status_code == 200:
        courses = json.loads(r.text)
        length = len(courses)
        if length > 0:
            course_id = courses[randint(0, length - 1)]['id']
            course = requests.get(settings.STUDENT_COURSES + str(course_id))
            if course.status_code != 200:
                raise Warning('Failed to get course with id:' + course_id)

    else:
        raise Warning('While getting student courses we got non 200 code')


def get_student_assignments():
    r = requests.get(settings.STUDENT_COURSES)
    if r.status_code == 200:
        assignments = json.loads(r.text)
        length = len(assignments)
        if length > 0:
            assignment_hash = assignments[randint(0, length - 1)]['hash']
            assignment = requests.get('/api/student/v1/assignments/' + str(assignment_hash))
            if assignment.status_code != 200:
                raise Warning('Failed to get assignment with hash:' + assignment_hash)
    else:
        raise Warning('While getting student assignments we got non 200 code')
    

def get_proofs():
    r = requests.get(settings.STUDENT_PROOFS)
    if r.status_code == 200:
        proofs = json.loads(r.text)
        # Placeholder for future testing.
    else:
        raise Warning('Failed to acquire proofs')


def get_submissions():
    r = requests.get(settings.STUDENT_SUBMISSIONS)
    if r.status_code == 200:
        submissions = json.loads(r.text)
        # Placeholder for future testing.
    else:
        raise Warning('Failed to acquire submissions')


def main():
    get_student_courses()
    get_student_assignments()

