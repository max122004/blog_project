from rest_framework import serializers

from authentication.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validate_data):
        user = super().create(validate_data)
        user.set_password(user.password)
        user.save()
        return user


class UserSerializerList(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'last_login']


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'is_active', 'email']


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']