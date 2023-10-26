from locust import HttpUser, task, between
import random

class MyUser(HttpUser):
    wait_time = between(5, 15)  # Set the time between tasks

    @task
    def simulate_slow_internet(self):
        # Simulate a slow internet connection (e.g., 3G)
        self.client.get("https://webrpc.tech/", name="Slow Internet")

    @task
    def simulate_fast_internet(self):
        # Simulate a fast internet connection
        self.client.get("https://webrpc.tech/", name="Fast Internet")

    @task
    def simulate_different_connection(self):
        # Simulate different types of connections (you can customize this)
        connection_types = ["4G", "DSL", "Fiber"]
        connection_type = random.choice(connection_types)
        self.client.get("https://webrpc.tech/", name=f"{connection_type} Connection")
