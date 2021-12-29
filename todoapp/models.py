from django.db import models
from django.contrib.auth.models import User


class Users(User):
    address = models.CharField(max_length=255, blank=True, null=True)
    contact_number = models.CharField(max_length=13, blank=True, null=True)
    is_admin = models.BooleanField(default=False)


class Shops(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=255, blank=True, null=True)
    is_open = models.BooleanField(default=False)
    average_ratings = models.FloatField(default=0.0)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)


class Items(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=1000, null=True, blank=True)
    shop = models.ForeignKey(Shops, on_delete=models.CASCADE)
    price = models.FloatField(default=0.0)
    is_available = models.BooleanField(default=True)


class ItemImage(models.Model):
    uri = models.CharField(max_length=200, null=False)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)


class Orders(models.Model):
    invoice_number = models.CharField(max_length=30, null=False)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    shop = models.ForeignKey(Shops, on_delete=models.CASCADE)


class OrderItems(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, null=True, on_delete=models.SET_NULL)


class CartItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)


class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shops, on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0)
    comments = models.CharField(max_length=1000, null=True, blank=True)


class ReviewImages(models.Model):
    uri = models.CharField(max_length=200, null=False)
    review = models.ForeignKey(Reviews, on_delete=models.CASCADE)