
from django.urls import path
from authen.views import RegisterView, GetToken


urlpatterns = [
    path('', RegisterView.as_view(), name='authen'),
    path('get_token', GetToken.as_view(), name='get_token'),
]
