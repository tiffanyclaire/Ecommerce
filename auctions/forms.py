from django import forms
from .models import Listing, Bid, Comments
from django.forms import Textarea


class listing_form(forms.ModelForm):

    class Meta:
        model = Listing
        fields = ['title', 'category',  'description', 'image', 'price' ]

        widgets= {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'category' : forms.Select(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),
            'image' : forms.TextInput(attrs={'class': 'form-control'}),
            'price' : forms.NumberInput(attrs={'class': 'form-control'})
        }
        
    

class bid_form(forms.ModelForm):

    class Meta: 
        model = Bid 
        fields = ['bid']
        labels = {
            "bid": ""
        }

        widgets= {
            'bid' : forms.NumberInput(attrs={'class': 'form-control'})
        }
        

class comment_form(forms.ModelForm):

    class Meta:
        model = Comments 
        fields = ['comment']
        labels = {
            "comment": ""
        }


        widgets= {
            'comment' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type your comment here...'}),
        }
        