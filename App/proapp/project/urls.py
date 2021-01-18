#importing django urls library
from django.urls import path
#Importing views
from project import views
#Creating paths

urlpatterns = [
    path(
        route='feed/',
        view=views.feed,
        name='feed'
    )
]