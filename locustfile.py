from locust import HttpLocust, TaskSet, task
from faucet import faucet
from random import randint


addresses = faucet.get_some_account_addresses(10)


class UserBehavior(TaskSet):
    def on_start(self):
        self.blocks()
        self.recent_transactions()
        self.get_random_account_info()

    def blocks(self):
        self.client.get('/api/witness/v1/blocks/')

    def recent_transactions(self):
        self.client.get('/api/witness/v1/transactions/')

    def get_random_account_info(self):
        self.client.get('/api/witness/v1/accounts/' + addresses[randint(0, 9)])


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000