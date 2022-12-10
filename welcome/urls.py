from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome_instructors, name = 'welcome_instructors'),
]