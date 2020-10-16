from django.urls import path, include
from . import views
# from .views import LoggsDeleteView

urlpatterns = [
    path('reminders/', views.reminders, name='logg-reminders'),
    path('new_logg/', views.LogCreateView.as_view(), name='new-log'),
    path('loggs/', views.LoggListView.as_view(), name='logg-view'),
    path('', views.home, name='logg-home')
]
