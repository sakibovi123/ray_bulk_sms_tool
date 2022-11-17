from import_export import resources
from .models import *


class CustomerResource(resources.ModelResource):
    class Meta:
        model = Customer
        fields = [
            "id", "phone_number"
        ]