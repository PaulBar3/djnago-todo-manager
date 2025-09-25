from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path("admin/", admin.site.urls),
    path("todos/", include("todo_list.urls")),
]


urlpatterns.extend(debug_toolbar_urls())
