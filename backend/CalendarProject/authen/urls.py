
from django.urls import path
from authen.views import RegisterView


urlpatterns = [
    path('', RegisterView.as_view(), name='authen'),
]
