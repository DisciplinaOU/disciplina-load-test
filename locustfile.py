from locust import HttpLocust, TaskSet, task
from faucet import faucet
from random import randint
import settings
import json

addresses = faucet.get_some_account_addresses(10)


class UserBehavior(TaskSet):
    @task(1)
    def blocks(self):
        self.client.get('/api/witness/v1/blocks/')

    @task(1)
    def recent_transactions(self):
        self.client.get('/api/witness/v1/transactions/')

    @task(1)
    def get_random_account_info(self):
        self.client.get('/api/witness/v1/accounts/' + addresses[randint(0, 9)])

    @task(3)  # 3 indicates weight when randomizing the task for spawned user
    def create_account(self):
        r = self.client.post(settings.FAUCET_CREATE_WALLET_URL, json={})
        if r.status_code == 200:
            data = json.loads(r.text)
            self.client.post(settings.FAUCET_TRANSFER_URL, json={"destination": data['address']})


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000