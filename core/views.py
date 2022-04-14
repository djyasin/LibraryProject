from django.shortcuts import render, redirect, get_object_or_404
from .models import Term, User
from django.contrib.auth.forms import UserCreationForm
from .forms import TermForm


def term_detail(request, pk):
    term = get_object_or_404(Term, pk=pk)

    return render(request, "term_detail.html", {"term": term})

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

def term_library(request):
    user = request.user
    terms = Term.objects.filter()

    return render(
        request,
        "term_library.html",
        {
            "terms": terms,
        },
    )

def edit_term(request, pk):
    term = get_object_or_404(Term, pk=pk)
    if request.method == "GET":
        form = TermForm(instance=term)
    else:
        form = TermForm(data=request.POST, instance=term)
        if form.is_valid():
            form.save()
            return redirect("term_detail", pk=term.pk)

    return render(request, "edit_term.html", {"form": form, "term": term, "pk": pk})