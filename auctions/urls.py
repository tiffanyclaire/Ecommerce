from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("listing/<int:listing_id>", views.listing, name="listing"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("watchlist_add/<int:listing_id>", views.watchlist_add, name="watchlist_add"),
    path("categories", views.categories, name="categories" ),
    path("bid/<int:listing_id>", views.bid, name="bid"),
    path("close_auction/<int:listing_id>", views.close_auction, name="close_auction")


   
]
