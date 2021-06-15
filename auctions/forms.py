from django import forms
from .models import Listing, Bid, Comments


class listing_form(forms.ModelForm):

    class Meta:
        model = Listing
        fields = ['title', 'category',  'description', 'price' ]
       
    

class bid_form(forms.ModelForm):

    class Meta: 
        model = Bid 
        fields = ['bid']



class comment_form(forms.ModelForm):

    class Meta:
        model = Comments 
        fields = ['comment']