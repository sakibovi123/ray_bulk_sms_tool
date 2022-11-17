from django.contrib import admin
from .models import *
from .resource import *
from import_export.admin import ImportExportModelAdmin


class CustomerImport(ImportExportModelAdmin):
    resource_class = CustomerResource


admin.site.register(Customer, CustomerImport)

admin.site.register(
    [
        ContentTemplate,
        NumberGroup,
        SendMessageModel,
        Group
    ]
)
