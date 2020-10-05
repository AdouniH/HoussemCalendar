
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
