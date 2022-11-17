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
    content = models.TextField(
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
    phone_number = models.CharField(
        max_length=255
    )
    is_sent = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return f"{self.phone_number}"


class Group(models.Model):
    created_at = models.DateField(max_length=255)
    customers = models.ManyToManyField(Customer)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    def __str__(self):
        return str(self.id)
        # for c in self.customers.all():
        #     return str(c.phone_number)


class SendMessageModel(models.Model):
    created_at = models.DateField(default=date.today)
    content = models.ForeignKey(
        ContentTemplate, on_delete=models.CASCADE
    )
    number = models.ForeignKey(
        NumberGroup, on_delete=models.CASCADE, null=True
    )
    # phone_field = models.CharField(max_length=255, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "SendMessage"
        verbose_name_plural = "SendMessages"

    def __str__(self):
        return str(self.created_at)

    # def save(self, *args, **kwargs):
    #     account_sid = "AC2b0cc7c783ccc1e82f3771636dda5e73"
    #     auth_token = "97a616e1b312b9b4ea0e74c27099377e"
    #     client = Client(
    #         account_sid, auth_token
    #     )
    #
    #     # for c in range(0, 10):
    #
    #     for c in Group.objects.all():
    #         for p in Customer.objects.filter(id=c.id):
    #             send_message = client.messages.create(
    #                 body=self.content.content,
    #                 from_=f"+{self.number.number}",
    #                 to=p.phone_number,
    #                 # to="+8801610968643"
    #             )
    #             print(len(str(c.phone_number)))
    #     super(SendMessageModel, self).save(*args, **kwargs)
