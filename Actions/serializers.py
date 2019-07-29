from rest_framework import serializers
from Actions.models import User, Todo, History
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    token = serializers.ReadOnlyField()
    class Meta:
        model=User
        fields=[
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "password",
            "is_superuser",
            "is_active",
            "date_joined",
            "last_login",
            "gender",
            "token"
        ]
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.ReadOnlyField()

    def validate(self, data):
        email=data.get("email")
        password=data.get("password")
        user=authenticate(username=email, password=password)
        if user is None:
            raise serializers.ValidationError("email or Password is incorrect")
        return{
            "email":user.email,
            "username":user.username,
            "token":user.token
    }
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("user", "id", "action", "created_at")

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ("id", "table_name", "item_id", "action", "user", "body", "created_at")



