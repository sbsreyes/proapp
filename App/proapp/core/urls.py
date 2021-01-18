#Importing path to handle the urls
from django.urls import path
#Importing views
from core import views

urlpatterns = [
    path(
        route='',
        view=views.login,
        name='login'
    ),
]
