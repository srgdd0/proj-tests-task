from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(5, 15)  # Set the time between tasks

    @task
    def make_request(self):
        response = self.client.get("https://webrpc.tech/")  # Send a GET request
