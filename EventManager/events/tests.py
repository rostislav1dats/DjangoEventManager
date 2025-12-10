from django.test import TestCase
from rest_framework.test import APIClient

class EventTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_event(self):
        reg = self.client.post('/apiuser/register/', {
            'email': 'alex10@gmail.com',
            'password': '-5'
        })

        access = reg.data['access']
        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {access}')

        event = {
            'title': 'Conference',
            'description': 'Tech talk',
            'date': '2025-10-10',
            'location': 'Berlin'
        }

        response = self.client.post('/apievents/events/', event)
        self.assertEqual(response.status_code, 201)
