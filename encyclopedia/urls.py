from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("encyclopedia/entries", views.entries, name="entries")
    #path("<str:entryname>", views.entires, name="entires")
]
