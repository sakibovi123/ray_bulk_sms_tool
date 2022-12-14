from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # api path
    path("api/", include("api.urls")),

    # custom admin url
    path("custom-admin/", include("customadmin.urls"))
]
