from django.db import models
from django.contrib.auth.models import User
from datetime import date
import string
import random


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
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.name


class SendMessageModel(models.Model):
    created_at = models.DateField(default=date.today)
    content = models.ForeignKey(ContentTemplate, on_delete=models.CASCADE)
    number = models.ForeignKey(NumberGroup, on_delete=models.CASCADE, null=True)
    customers = models.ManyToManyField(Customer, blank=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "SendMessage"
        verbose_name_plural = "SendMessages"

    def __str__(self):
        return self.created_at
