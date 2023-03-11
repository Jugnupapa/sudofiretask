from rest_framework import serializers
from .models import Customer, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name', 'email', 'mobile_no']

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Customer
        fields = ['user','profile_number']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        customer, created = Customer.objects.update_or_create(user=user, profile_number=validated_data.pop('profile_number'))
        return customer
