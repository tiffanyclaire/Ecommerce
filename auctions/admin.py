from django.contrib import admin

# Register your models here

from . models import Listing, Bid, Watchlist, Comments

admin.site.register(Listing)
admin.site.register(Bid)
admin.site.register(Watchlist)
admin.site.register(Comments)