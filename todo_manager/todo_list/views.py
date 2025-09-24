from django.http import (
    HttpRequest,
    HttpResponse,
)
from django.shortcuts import render
from django.urls import reverse

from .models import ToDoItem
from .forms import ToDoItemCreateForm

from django.views.generic import TemplateView, ListView, DetailView, CreateView


def index_view(request: HttpRequest) -> HttpResponse:
    todo_items = ToDoItem.objects.all()[:3]
    return render(
        request,
        template_name="todo_list/index.html",
        context={"todo_items": todo_items},
    )


class ToDoListIndexView(ListView):
    template_name = "todo_list/index.html"
    queryset = ToDoItem.objects.all()


class ToDoListView(ListView):
    model = ToDoItem


class ToDoListDoneView(ListView):
    queryset = ToDoItem.objects.filter(done=True).all()


class ToDoDetailView(DetailView):
    model = ToDoItem


class ToDoItemCreateView(CreateView):
    model = ToDoItem
    form_class = ToDoItemCreateForm
    #fields = ("title", "description")

