import time
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task()
    def add(self):
        for a in range(10):
            self.client.get(f"/math/add?a={a}00&b=999", name = "/math/add")
            time.sleep(1)

