from django.test import TestCase
from rest_framework.test import APIClient

class AuthTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register(self):
        response = self.client.post('/apiuser/register/', {
            'email': 'alex10@gmail.com',
            'password': '-5'
        })

        self.assertEqual(response.status_code, 201)

    def test_login(self):
        self.client.post('/apiuser/register/', {
            'email': 'alex10@gmail.com',
            'password': '-5'
        })

        response = self.client.post('/apiuser/token/', {
            'email': 'alex10@gmail.com',
            'password': '-5'
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)