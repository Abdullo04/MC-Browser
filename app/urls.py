# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("search/", views.search, name="search"),
    path("history/", views.history, name="history"),
    path("save-search/", views.save_search, name="save-search")
]
