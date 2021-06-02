from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import CharField


class User(AbstractUser):
    pass

class Listing(models.Model):
    seller  = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    starting_bid = models.IntegerField()
    list = models.DateTimeField(auto_now_add=True)


class Bid(models.Model):
    user = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    listing_id = models.IntegerField()
    bid = models.IntegerField


class Watchlist(models.Model):
    User = models.CharField
    listing_id = models.IntegerField

class Comments(models.Model):
    user =  models.CharField(max_length=64)
    comment = models.CharField(max_length=100)
    listing_id = models.IntegerField()





