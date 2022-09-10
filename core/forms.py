from django import forms
from .models import Term, User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    name = forms.CharField(max_length=100, help_text="Name")
    email = forms.EmailField(max_length=100, help_text="Email Address")

    class Meta:
        model = User
        fields = ["username", "password", "email"]

class TermForm(forms.ModelForm):
    class Meta:
        model = Term
        fields = [
            "original_term",
            "preferred_term",
            "provenance",
        ]
        exclude = ['created_at']