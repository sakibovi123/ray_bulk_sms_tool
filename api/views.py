from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from .models import *
from django.contrib.auth.models import User
from rest_framework.views import APIView


class GETContentTemplateView(APIView):

    def get(self, request):
        pass


class POSTContentTemplateView(APIView):

    def post(self, request):
        pass


class PUTContentTemplateView(APIView):

    def put(self, request):
        pass


class DELETEContentTemplateView(APIView):

    def delete(self, request):
        pass


class POSTMessage(APIView):

    def post(self, request):
        pass