from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("encyclopedia/<str:title>", views.md_to_html, name="entries"),
    path("search", views.get_search, name="search")
]
