from abc import ABC
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class UserSerializer(serializers.Serializer, ABC):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password"
        ]

    def create(self, validated_data):
        username = validated_data.get("username")
        email = validated_data.get("email")
        password = validated_data.get("password")

        alr_user = User.objects.filter(email=email)

        if not alr_user:
            if username is not None and email is not None and password is not None:
                user = User(username=username, email=email)
                user.set_password(password)
                user.save()
                return user
            else:
                raise serializers.ValidationError({
                    "error": "Please Fill up the all fields"
                })
        else:
            raise serializers.ValidationError({
                "error": "User Already Exists"
            })


class ContentTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentTemplate
        fields = [
            "created_at", "slug", "title", "content"
        ]
