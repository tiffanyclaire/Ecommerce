from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import CharField, NullBooleanField
from django.core.validators import MinValueValidator


class User(AbstractUser):
    pass


class Categories(models.Model):
    category = models.CharField(max_length=30)
    def __str__(self):
         return self.category

    


class Listing(models.Model):
    active = models.BooleanField(default=True)
    seller  = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listing")
    category = models.ForeignKey(Categories, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=64, default= None)
    description = models.CharField(max_length=255)
    image = models.URLField(blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(0.01)])
    date_listed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} created by {self.seller}"
        

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bid")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bid", default= None)
    bid = models.DecimalField(max_digits= 7, decimal_places= 2, default= None)

    def __str__(self):
        return f"{self.listing} : {self.user} : {self.bid}"


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist", default= None)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="watchlist", default= None)

    def __str__(self):
        return f"{self.user}'s watchlist"



class Comments(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField(max_length=255)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments", default= None)

    def __str__(self):
        return f"{self.user} commented {self.comment} on {self.listing}"







