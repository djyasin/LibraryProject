from django import forms
from .models import Tag,Term, User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "email"]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = [
            "tag",
        ]
        exclude = ['created_at']
class TermForm(forms.ModelForm):
    class Meta:
        model = Term
        fields = [
            "original_term",
            "preferred_term",
            "provenance",
            "category",
            "created_at",
            "tags"
        ]
        tags = forms.ModelMultipleChoiceField(
            queryset=Tag.objects.all(),
            widget=forms.CheckboxSelectMultiple
    )
        exclude = ['created_at']

    class ExploreForm(forms.Form):  
        query = forms.CharField(  
        label='',  
        widget=forms.TextInput(attrs={    
        'placeholder': 'Explore tags'
        }) 
 )