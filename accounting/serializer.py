from rest_framework import serializers

from .models import Position, Employees, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password']

        def create(self, validated_data):
            try:
                user = User(username=validated_data['username'])
                user.set_password(validated_data['password'])
                user.save()
            except:
                return user


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'
        read_only_fields = ['user', ]
