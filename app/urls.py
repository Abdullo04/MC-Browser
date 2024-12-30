# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('history/', views.history, name='history'),
    path('save-search/', views.save_search, name='save-search'),
    path('toggle-bookmark/<int:search_id>/', views.toggle_bookmark, name='toggle-bookmark'),
    path('delete-search/<int:search_id>/', views.delete_search, name='delete-search'),
    path('clear-history/', views.clear_history, name='clear-history'),
]
