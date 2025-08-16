from locust import HttpUser, between
from ..configs.endpoints import Hosts

class BaseUser(HttpUser):
    abstract = True
    wait_time = between(1, 3)

    def on_start(self):
        """Hook called when a user starts"""
        pass

    def on_stop(self):
        """Hook called when a user stops"""
        pass
