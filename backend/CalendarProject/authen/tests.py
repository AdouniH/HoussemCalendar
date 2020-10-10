from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from authen.models import Account
from django.contrib.auth import authenticate


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

        user = User.objects.create(username="hello")
        user.set_password("world")
        user.save()

        token, created = Token.objects.get_or_create(user=user)
        user_from_token = Token.objects.get(key=token.key).user

        response = self.client.post(url, user1, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(user_from_token.username, user.username)


class TestAccountView(APITestCase):
    def setUp(self):
        pass

    @staticmethod
    def create_hello_user():
        user = User.objects.create(username="hello")
        user.set_password("world")
        user.save()
        account = Account.objects.create(user=user, code="code_100")
        account.save()

    def test_get(self):
        """
        -> /auth/account
        """
        self.create_hello_user()

        url = reverse('account')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['username'], "hello")
        self.assertEqual(response.data[0]['code'], "code_100")
        self.assertIsNotNone(
            authenticate(
                username=response.data[0]['username'],
                password='world'
            )
        )

    def test_post(self):
        """
        -> /auth/account
        """

        url = reverse('account')
        context = {
            "code": "mycode",
            "user": {"username": "new_user",
                     "password": "new_password"}
        }

        response = self.client.post(url, context, format='json')

        self.assertEqual(Account.objects.count(), 1)
        self.assertEqual(Account.objects.all()[0].code, "mycode")
        self.assertGreaterEqual(len(response.data["token"]), 5)


class TestAccountGetTokenView(APITestCase):
    def setUp(self):
        user = User.objects.create(username="hello")
        user.set_password("world")
        user.save()
        account = Account.objects.create(user=user, code="code_100")
        account.save()

        self.tokenKey = Token.objects.get_or_create(user=account.user)[0].key

    def test_post(self):
        """
        -> /auth/get_token_from_account
        """
        url = reverse('get_token_from_account')
        context = {"code": "code_100"}

        response = self.client.post(url, context, format='json')

        self.assertEqual(response.data["token"], self.tokenKey)
