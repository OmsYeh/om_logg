from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('user_login/', views.user_login, name='user-login'),
    path('logout/', views.user_logout, name='logg-logout')
]
