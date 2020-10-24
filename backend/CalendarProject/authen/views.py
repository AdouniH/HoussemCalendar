
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist

from authen.models import Account
from authen.serializers import UserSerializer, AccountSerializer
from authen import doc_auth


class RegisterView(APIView):
    """
    Gestion de l'authentification
    """
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    # def get(self, request, format=None):
    #     users = User.objects.all()
    #     serializer = UserSerializer(users, many=True)
    #     return Response(serializer.data)

    @doc_auth.register_new_user
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            context = {'token': token.key}
            return Response(context, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetToken(APIView):
    @doc_auth.get_token
    def post(self, request, format=None):

        user = authenticate(
            username=request.data.get("username"),
            password=request.data.get("password")
        )

        if user:
            token, created = Token.objects.get_or_create(user=user)
            context = {'token': token.key}
            return Response(context, status.HTTP_200_OK)

        else:
            return Response({}, status.HTTP_400_BAD_REQUEST)


class AccountView(APIView):
    # def get(self, request, format=None):
    #
    #     accounts = Account.objects.all()
    #     serializer = AccountSerializer(accounts, many=True)
    #     accounts = []
    #
    #     for serializer_data in serializer.data:
    #         context = {}
    #         for key, value in serializer_data.items():
    #             if key == 'user':
    #                 context["username"] = value["username"]
    #                 context["password"] = value["password"]
    #                 continue
    #             context[key] = value
    #         accounts.append(context)
    #
    #     return Response(accounts)

    @doc_auth.create_account
    def post(self, request, format=None):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username= serializer.data["user"]["username"])
            context = {}
            if user:
                token, created = Token.objects.get_or_create(user=user)
                context["token"] = token.key
            return Response(context, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetTokenFromAccount(APIView):
    @doc_auth.get_token_from_account
    def post(self, request, format=None):
        code = request.data["code"]
        
        try:
            account = Account.objects.get(code=code)
        except ObjectDoesNotExist:
            account = None

        if account:
            user = account.user
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response({}, status=status.HTTP_400_BAD_REQUEST)


class CheckToken(APIView):
    @doc_auth.check_token_from_account
    def post(self, request, format=None):
        tokenKey = request.data["token"]

        try:
            user = Token.objects.get(key=tokenKey).user
            account = Account.objects.get(user=user)
        except ObjectDoesNotExist:
            account = None

        if account:
            return Response({"code": account.code}, status=status.HTTP_200_OK)
        return Response({}, status=status.HTTP_400_BAD_REQUEST)
