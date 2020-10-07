from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class TestRegisterView(APITestCase):
    def setUp(self):
        user_authentication = User.objects.create_user(username="no", password="way")
        token, created = Token.objects.get_or_create(user=user_authentication)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

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
        self.assertEqual(User.objects.count(), 2)

        response = self.client.post(url, user1, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post(url, user2, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 3)


class TestGetTokenView(APITestCase):
    def test_getToken(self):
        """
        -> /auth/get_token
        """

        url = reverse('get_token')

        user1 = {
            "username": "hello",
            "password": "world"
        }

        user = User.objects.create(username="hello", password="world")
        token, created = Token.objects.get_or_create(user=user)
        user_from_token = Token.objects.get(key=token.key).user

        response = self.client.post(url, user1, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(user_from_token.username, user.username)
