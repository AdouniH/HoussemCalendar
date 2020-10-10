from rest_framework import serializers
from django.contrib.auth.models import User
from authen.models import Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Account
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(username=validated_data["user"]["username"])
        user.set_password(validated_data["user"]["password"])
        user.save()
        account = Account.objects.create(
            user=user,
            code=validated_data["code"]
        )
        return account

