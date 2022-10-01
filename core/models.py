from unicodedata import category
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import DateTimeField


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Tag(models.Model):
    tag = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tag


class Term(models.Model):
    original_term = models.CharField(max_length=150)
    preferred_term = models.CharField(max_length=150)
    provenance = models.CharField(max_length=500)
    category = models.CharField(max_length=150, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(to=Tag, related_name="terms", blank=True)
