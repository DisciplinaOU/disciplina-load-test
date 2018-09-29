from locust import HttpLocust, TaskSet, task
from random import randint
import json


class UserBehavior(TaskSet):
    @task(1)
    def courses(self):
        headers = {"Authorization": "Bearer %s" % 'eyJhbGciOiJFZERTQSJ9.eyJkYXQiOnsiYWRQYXRoIjoiL2FwaS9zdHVkZW50L3YxL2NvdXJzZXMiLCJhZFRpbWUiOiIyMDI1LTA4LTEwVDEzOjE1OjQwLjQ2MTk5ODEzNloifX0.O8F0wEfFR8GRYiQNJxurGcP5fU_KVra1pPJ6eqPw2Hl9NKQclZuf6b0_qH7oGeSPahPoZ2t9gcQkQQ4dh0pkBg'}
        # self.client.get('/api/student/v1/courses', headers=headers)
        r = self.client.get('/api/student/v1/courses')
        if r.status_code == 200:
            data = json.loads(r.text)
            length = len(data)
            if length > 0:
                random_id = data[randint(0, length - 1)]['id']
                self.client.get('/api/student/v1/courses/' + str(random_id))

    @task(1)
    def assignments(self):
        r = self.client.get('/api/student/v1/assignments')
        if r.status_code == 200:
            data = json.loads(r.text)
            length = len(data)
            if length > 0:
                random_hash = data[randint(0, length - 1)]['hash']
                self.client.get('/api/student/v1/assignments/' + str(random_hash))

    @task(1)
    def submissions(self):
        r = self.client.get('/api/student/v1/submissions')

    @task(1)
    def proofs(self):
        self.client.get('/api/student/v1/proofs')


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 10000
