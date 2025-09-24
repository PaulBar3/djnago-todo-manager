from django.http import (
    HttpRequest,
    HttpResponse,
)
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from .models import ToDoItem
from .forms import (
    ToDoItemCreateForm,
    ToDoItemUpdateForm,
)

from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


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
    # fields = ("title", "description")


class ToDoItemUpdateView(UpdateView):
    model = ToDoItem
    template_name_suffix = "_update_form"
    form_class = ToDoItemUpdateForm


class ToDoItemDeleteView(DeleteView):
    model = ToDoItem
    success_url = reverse_lazy("todo_list:list")
    "_confirm_delete"