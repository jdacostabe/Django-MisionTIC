from rest_framework import serializers
from bank_be.models.user import User
from bank_be.models.account import Account
from bank_be.serializers.accountSerializer import AccountSerializer

class UserSerializer(serializers.ModelSerializer):

    account = AccountSerializer(many=False);

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'email', 'account']

    def create(self, validated_data):
        accountData = validated_data.pop('account')
        userInstance = User.objects.create(**validated_data)
        Account.objects.create(user=userInstance, **accountData)
        return userInstance