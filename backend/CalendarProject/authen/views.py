
from django.contrib.auth.models import User
from authen.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from authen import doc_auth
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


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

        user = User.objects.get(
            username=request.data.get("username"),
            password=request.data.get("password")
        )

        if user:
            token, created = Token.objects.get_or_create(user=user)
            context = {'token': token.key}
            return Response(context, status.HTTP_200_OK)
        else:
            return Response({}, status.HTTP_400_BAD_REQUEST)
