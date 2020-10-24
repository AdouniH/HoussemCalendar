
from django.urls import path
from authen.views import RegisterView, GetToken, AccountView, GetTokenFromAccount, CheckToken


urlpatterns = [
    path('', RegisterView.as_view(), name='authen'),
    path('get_token_from_user/', GetToken.as_view(), name='get_token'),
    path('account/', AccountView.as_view(), name='account'),
    path('get_token_from_account/', GetTokenFromAccount.as_view(), name='get_token_from_account'),
    path('check_token/', CheckToken.as_view(), name='check_token_from_account'),
]
