from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.md_to_html, name="entries"),
    path("search", views.get_search, name="search"),
    path("newpage", views.newpage, name="newpage"), 
    path("edit", views.edit, name="edit"), 
    path("random", views.random_page, name="random")
]
