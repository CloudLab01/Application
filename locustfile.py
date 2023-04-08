from locust import HttpUser, between, task

class HelloWorldUser(HttpUser):
    @task
    def hello(self):
        self.client.get("/")

    @task
    def hello_name(self):
        self.client.post("/hello", data={"name": "Piotr"})
