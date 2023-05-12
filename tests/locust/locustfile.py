from locust import HttpUser, task


class ProjectPerftest(HttpUser):

    @task
    def clubs(self):
        self.client.get("/clubs")
