from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class MainGetRequest(TestCase):
    def test_get_request(self):
        client = Client()
        response = client.get('/boolseye/')
        self.assertEqual(response.status_code, 200)


class MainPostRequest(TestCase):
    def test_get_request(self):
        client = Client()
        response = client.post('/boolseye/')
        self.assertEqual(response.status_code, 302)


class AddUserGetRequest(TestCase):
    def test_get_request(self):
        client = Client()
        response = client.get('/boolseye/register/')
        self.assertEqual(response.status_code, 200)


class AddUserTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')

    def test_add_user(self):
        data = {
            'login': 'testuser',
            'password': 'testpassword',
            'email': 'testuser@example.com',
        }

        response = self.client.post(self.register_url, data)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())


class LoginGetRequest(TestCase):
    def test_get_request(self):
        client = Client()
        response = client.get('/boolseye/login/')
        self.assertEqual(response.status_code, 200)


class LoginPostRequest(TestCase):
    def test_get_request(self):
        client = Client()
        response = client.post('/boolseye/')
        self.assertEqual(response.status_code, 302)


class SupportGetRequest(TestCase):
    def test_get_request(self):
        client = Client()
        response = client.get('/boolseye/support/')
        self.assertEqual(response.status_code, 200)


class AccountGetRequest(TestCase):
    def test_get_request(self):
        client = Client()
        response = client.get('/boolseye/account/')
        self.assertEqual(response.status_code, 302)


class QuizGetRequest(TestCase):
    def test_get_request(self):
        client = Client()
        response = client.get('/boolseye/quiz/')
        self.assertEqual(response.status_code, 200)
