from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import CharField, NullBooleanField


class User(AbstractUser):
    pass

class Listing(models.Model):
    seller  = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listing")
    category = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    price = models.IntegerField()
    date_listed = models.DateTimeField(auto_now_add=True)


class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bid")
    title = models.CharField(max_length=64)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bid", default= None)
    bid = models.IntegerField(default= None) 


class Watchlist(models.Model):
    User = models.CharField
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="watchlist", default= None)

class Comments(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    comment = models.CharField(max_length=100)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments", default= None)





