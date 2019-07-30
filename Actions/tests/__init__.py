# Third-Party Imports
from django.apps import apps
from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.reverse import reverse

User = get_user_model()

from rest_framework.test import APIClient
from Actions.models import User, History, Todo

client = APIClient()


class APIBaseTestCase(TestCase):
    @classmethod
    def setUpClass(self):
        super().setUpClass()

        self.data = {
            "username": "wayne_ronney",
            "first_name": "wayne",
            "last_name": "rooney",
            "email": "wayne@rooney.com",
            "password": "waynerooney123",
            "gender": "male",
        }

        res = client.post("/api/v1/users/", data=self.data, format="json")
        self.token = res.data["token"]

        res = client.post("/api/v1/users/login/", data=self.data, format="json")
        # urls
        self.todo = reverse("todo-list")
        self.history = reverse("history-list")
