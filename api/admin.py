from django.contrib import admin
from .models import *


admin.site.register(
    [
        ContentTemplate,
        NumberGroup,
        SendMessageModel,
        Customer
    ]
)
