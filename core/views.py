from django.shortcuts import render, redirect, get_object_or_404
from .models import Term, User
from django.contrib.auth.forms import UserCreationForm
from .forms import TermForm