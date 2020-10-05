from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class TestRegisterView(APITestCase):

    def test_create_account(self):
        """
        Tests des creations des des utilisateurs -> /auth
        """
        url = reverse('authen')

        user1 = {
            'username': 'helloWorld',
            'password': 'toto'
        }

        user2 = {
            'username': 'helloWorld2',
            'password': 'toto'
        }

        response = self.client.post(url, user1, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(list(response.data.keys()), ['token'])
        self.assertGreaterEqual(len(response.data['token']), 2)
        self.assertEqual(User.objects.count(), 1)

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post(url, user2, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
