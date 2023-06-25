from rest_framework import serializers

from baseapp.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'created', 'updated']
