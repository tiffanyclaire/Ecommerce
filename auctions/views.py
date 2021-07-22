from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from auctions.models import User, Listing, Watchlist, Categories, Bid

from .forms import *

def index(request):
    return render(request, "auctions/index.html", {
        "Listings" : Listing.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def create_listing(request):
    form = listing_form(request.POST, request.FILES)
    if form.is_valid(): 
        listing = form.save(commit=False)
        listing.seller = request.user
        listing.save()
        return HttpResponseRedirect(reverse("index"))

    else:
        form = listing_form()
        return render(request, "auctions/create_listing.html", {
            "form": form
        })



def listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    form = bid_form()
    return render(request, "auctions/listing.html", {
        "listing": listing, 
        "form" : form
   })


@login_required
def watchlist_add(request, listing_id):
    user = request.user
    listing = Listing.objects.get(id=listing_id)
    watchlist = Watchlist(listing=listing, user=user)
    watchlist.save()
    return HttpResponseRedirect(reverse("listing", args=(listing_id,)))


        
@login_required
def watchlist(request):
    watchlist = Watchlist.objects.filter(user=request.user)
    return render(request, "auctions/watchlist.html", {
        "listings" : watchlist
    })


@login_required
def categories(request):
    listings = None
    category = None
    if request.method == "POST":
        category = request.POST["categories"]
        listings = Listing.objects.filter(category = category)
    return render(request, "auctions/categories.html", {
        "categories" : Categories.objects.all(),
        "category" : Categories.objects.get(id = category) if category is not None else "",
        "listings" : listings
        })

@login_required
def bid(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    starting_bid = listing.price
    new_bid = float(request.POST['bid'])

    if new_bid >= starting_bid:
        bid = Bid(user=request.user, bid=new_bid, listing=listing)
        bid.save()
        #update intitial listing price#
        Listing.objects.filter(id=listing_id).update(price=new_bid)
        return redirect("listing", id=listing_id)

    else:
        listing = Listing.objects.get(id=listing_id)
        form = bid_form()
        return render(request, "auctions/listing.html", {
        "listing": listing, 
        "form" : form,
        "message" : {'error':'Your bid must be higher than the current price'}
   })






        
      #  if listing.price >= newbid:#
          #  listing = Listing.objects.get(id=listing_id)#
          #  return render (request, "auctions/listing.html")#
