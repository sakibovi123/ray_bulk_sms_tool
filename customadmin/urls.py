from django.urls import path
from .views import *

urlpatterns = [
    path("", AdminIndex.as_view(), name="AdminIndex"),
]