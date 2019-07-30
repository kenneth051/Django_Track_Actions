# Third-Party Imports
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

# App Imports
from Actions.tests import APIBaseTestCase
from Actions.models import User, History, Todo

client = APIClient()


class AppTests(APIBaseTestCase):
    def test_user_model(self):
        """ Test User model"""
        user = User.objects.create_superuser(
            "test9@test.com", "test9", password="123456789"
        )
        self.assertEqual(str(user), "test9@test.com")
        self.assertEqual(str(user.email), "test9@test.com")
        self.assertEqual(str(user.username), "test9")

    def test_user_model_with_password(self):
        """ Test User model"""
        with self.assertRaises(TypeError):
            user = User.objects.create_superuser(
                "test9@test.com", "test9", password=None
            )

    def test_wrong_login(self):
        data = {"email": "wayne@rooney.com", "password": "123"}
        res = client.post("/api/v1/users/login/", data=data, format="json")
        self.assertEqual(res.status_code, 400)

    def test_create_to_do_without_authentication(self):
        # create
        data = {"action": "write code"}
        response = client.post(self.todo, HTTP_AUTHORIZATION=None, data=data)
        self.assertEqual(response.status_code, 403)

    def test_create_to_do_with_bad_authentication(self):
        data = {"action": "write code"}
        response = client.post(self.todo, HTTP_AUTHORIZATION="None", data=data)
        self.assertEqual(response.status_code, 403)

    def test_create_update_delete_to_do_get_history(self):
        # create
        data = {"action": "write code"}
        response = client.post(self.todo, HTTP_AUTHORIZATION=self.token, data=data)
        self.assertEqual(response.status_code, 201)
        # update
        data1 = {"action": "edit code"}
        edit_todo_url = reverse("todo-detail", args={response.data.get("id")})
        response = client.put(edit_todo_url, HTTP_AUTHORIZATION=self.token, data=data1)
        self.assertEqual(response.status_code, 200)
        # delete
        response = client.delete(edit_todo_url, HTTP_AUTHORIZATION=self.token)
        self.assertEqual(response.status_code, 204)

        # get history
        response = client.get(self.history, HTTP_AUTHORIZATION=self.token)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], History.objects.count())
