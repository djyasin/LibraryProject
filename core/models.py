from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import DateTimeField

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Term(models.Model):
    library_of_congress = models.CharField(max_length=150)
    popular_term = models.CharField(max_length=150)
    provenance = models.CharField(max_length=500)
    created_at = DateTimeField(auto_now_add=True)