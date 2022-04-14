from django.shortcuts import render, redirect, get_object_or_404
from .models import Term, User
from django.contrib.auth.forms import UserCreationForm
from .forms import TermForm

def add_term(request):
    if request.method == "POST":
        form = TermForm(data=request.POST)
        if form.is_valid():
            term = form.save(commit=False)
            term.save()

            return redirect("term_detail", pk=term.pk)
    else:
        form = TermForm()

    return render(request, "add_term.html", {"form": form})