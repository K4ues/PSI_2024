from django.urls import path
from Projeto.views.HomeView import home_view
urlpatterns = [
    path("", home_view, name= 'home'),
]