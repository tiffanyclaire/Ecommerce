from django.contrib import admin

# Register your models here

from . models import User, Listing, Bid, Watchlist, Comments, Categories

admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Bid)
admin.site.register(Watchlist)
admin.site.register(Comments)
admin.site.register(Categories)