from django import forms
from .models import Tag,Term, User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    name = forms.CharField(max_length=100, help_text="Name")
    email = forms.EmailField(max_length=100, help_text="Email Address")

    class Meta:
        model = User
        fields = ["username", "password", "email"]


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
            "tags"
        ]
        tags = forms.ModelMultipleChoiceField(
            queryset=Tag.objects.all(),
            widget=forms.CheckboxSelectMultiple
    )
        exclude = ['created_at']