
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from authen.serializers import UserSerializer
from rest_framework import status


register_new_user = swagger_auto_schema(
    operation_summary="Creer un nouveau utilisateur",
    request_body=UserSerializer,
    responses={
        status.HTTP_200_OK: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'token': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    title='le token key'
                )
            }
        )
    }
)


get_token = swagger_auto_schema(
    operation_summary="Récuperer le token key à partir du username et du password",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['username', 'password'],
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, title="le nom d'utilisateur"),
            'password': openapi.Schema(type=openapi.TYPE_STRING, title="le mot de passe"),
        }
    ),
    responses={
        status.HTTP_200_OK: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'token': openapi.Schema(type=openapi.TYPE_STRING, title='le token key')
            }
        )
    }
)


create_account = swagger_auto_schema(
    operation_summary="Créer un nouveau account",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['user', 'code'],
        properties={
            'user': openapi.Schema(
                type=openapi.TYPE_OBJECT,
                required=["username", "password"],
                properties={
                    'username': openapi.Schema(type=openapi.TYPE_STRING, title="le nom d'utilisateur"),
                    'password': openapi.Schema(type=openapi.TYPE_STRING, title="le mot de passe"),
                }
            ),
            'code': openapi.Schema(type=openapi.TYPE_STRING, title="le code"),
        }
    ),
    responses={
        status.HTTP_200_OK: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'token': openapi.Schema(type=openapi.TYPE_STRING, title='le token key')
            }
        )
    }
)