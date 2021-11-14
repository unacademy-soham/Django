from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255, null=False)
    date_of_birth = models.DateField(null=True, blank=True)


class Todo(models.Model):
    CHOICES = [
        ("L", "Low"),
        ("M", "Medium"),
        ("H", "High")
    ]
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=300, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.CharField(max_length=1, choices=CHOICES)

