from django.db import models
from django.contrib.auth.models import User
from datetime import date
import string
import random

from twilio.rest import Client


class ContentTemplate(models.Model):
    created_at = models.DateField(
        default=date.today
    )
    slug = models.SlugField()
    title = models.CharField(
        max_length=255, null=True, blank=True
    )
    content = models.CharField(
        max_length=255
    )

    class Meta:
        ordering = ["created_at"]
        verbose_name = "ContentTemplate"
        verbose_name_plural = "ContentTemplates"

    def __str__(self):
        return str(self.title)


class NumberGroup(models.Model):
    created_at = models.DateField(
        default=date.today
    )
    updated_at = models.DateField(
        null=True, blank=True, auto_now_add=True
    )
    slug = models.SlugField(
        null=True, blank=True
    )
    number = models.CharField(
        max_length=255
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "NumberGroup"
        verbose_name_plural = "NumberGroups"

    def __str__(self):
        return self.number

    @staticmethod
    def generate_slug():
        length = 12
        return "".join(random.choices(string.ascii_lowercase, k=length))

    def save(self, *args, **kwargs):
        self.slug = self.generate_slug()
        super(NumberGroup, self).save(*args, **kwargs)


class Customer(models.Model):
    first_name = models.CharField(
        max_length=255
    )
    last_name = models.CharField(
        max_length=255
    )
    country_code = models.CharField(
        max_length=255
    )
    state_code = models.CharField(
        max_length=255
    )
    phone_number = models.CharField(
        max_length=255
    )

    class Meta:
        ordering = ["-id"]
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class SendMessageModel(models.Model):
    created_at = models.DateField(default=date.today)
    content = models.ForeignKey(
        ContentTemplate, on_delete=models.CASCADE
    )
    number = models.ForeignKey(
        NumberGroup, on_delete=models.CASCADE, null=True
    )
    # phone_field = models.CharField(max_length=255, null=True)
    customers = models.ManyToManyField(
        Customer, blank=True
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "SendMessage"
        verbose_name_plural = "SendMessages"

    def __str__(self):
        return str(self.created_at)

    def save(self, *args, **kwargs):
        account_sid = "AC2b0cc7c783ccc1e82f3771636dda5e73"
        auth_token = "16fb97d1bff52212af1dc7734b80f301"
        client = Client(
            account_sid, auth_token
        )

        # for c in range(0, 10):
        for c in Customer.objects.all():
            send_message = client.messages.create(
                body=self.content.content,
                from_=f"+{self.number.number}",
                to=c.phone_number,
                # to="+8801610968643"
            )
            print("SENT")
            super(SendMessageModel, self).save(*args, **kwargs)
