from django.shortcuts import render, redirect, get_object_or_404
from .models import Tag, Term, User
from django.contrib.auth.forms import UserCreationForm
from .forms import TermForm, TagForm
from django.views.generic import TemplateView, ListView
from django.db.models import query, Q

def home(request):
    user = request.user
    terms = Term.objects.filter()

    return render(
        request,
        "home.html",
        {
            "terms": terms,
        },
    )

def term_detail(request, pk):
    term = get_object_or_404(Term, pk=pk)

    return render(request, "term_detail.html", {"term": term})

def tag_detail(request, pk):
    tag = get_object_or_404(Tag, pk=pk)

    return render(request, "tag_detail.html", {"tag": tag})

def add_tag(request):
    if request.method == "POST":
        form = TagForm(data=request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.save()

            return redirect("tag_detail", pk=tag.pk)
    else:
        form = TagForm()

    return render(request, "add_tag.html", {"form": form})

def add_term(request):
    if request.method == "POST":
        form = TermForm(data=request.POST)
        if form.is_valid():
            term = form.save(commit=True)
            term.save()

            return redirect("term_detail", pk=term.pk)
    else:
        form = TermForm()

    return render(request, "add_term.html", {"form": form})

def term_library(request):
    user = request.user
    terms = Term.objects.filter().order_by('original_term')

    return render(
        request,
        "term_library.html",
        {
            "terms": terms,
        },
    )

def tag_list(request):
    user = request.user
    tags = Tag.objects.filter()

    return render(
        request,
        "tag_list.html",
        {
            "tags": tags,
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

def edit_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == "GET":
        form = TagForm(instance=tag)
    else:
        form = TagForm(data=request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect("tag_detail", pk=tag.pk)

    return render(request, "edit_tag.html", {"form": form, "tag": tag, "pk": pk})

def delete_term(request, pk):
    term = get_object_or_404(Term, pk=pk)
    if request.method == "POST":
        term.delete()
        return redirect(to="term_library")
    return render(request, "delete_term.html", {"term": term})

def delete_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == "POST":
        tag.delete()
        return redirect(to="tag_list")
    return render(request, "delete_tag.html", {"tag": tag})
class search_term(ListView):
    model = Term
    template_name = 'search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Term.objects.filter(

            Q(original_term__icontains=query) | Q(preferred_term__icontains=query)
        )

        return object_list

