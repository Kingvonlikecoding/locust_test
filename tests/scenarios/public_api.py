from locust import task
from .base_user import BaseUser
from ..configs.endpoints import Endpoints, Hosts

class PublicApiUser(BaseUser):
    host = Hosts.JSON_PLACEHOLDER

    @task(5)
    def get_posts(self):
        with self.client.get(Endpoints.POSTS, catch_response=True) as resp:
            if resp.status_code != 200 or len(resp.json()) < 10:
                resp.failure("get_posts failed")
            else:
                resp.success()

    @task(2)
    def create_post(self):
        payload = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
        with self.client.post(Endpoints.POSTS, json=payload, catch_response=True) as resp:
            if resp.status_code != 201 or resp.json().get("id") is None:
                resp.failure("create_post failed")
            else:
                resp.success()

    @task(2)
    def httpbin_get(self):
        with self.client.get(Endpoints.HTTPBIN_GET, catch_response=True) as resp:
            if resp.status_code != 200:
                resp.failure("httpbin_get failed")
            else:
                resp.success()

    @task(1)
    def random_dog(self):
        with self.client.get(Endpoints.DOG_API, catch_response=True) as resp:
            if resp.status_code != 200:
                resp.failure("random_dog failed")
            else:
                resp.success()
