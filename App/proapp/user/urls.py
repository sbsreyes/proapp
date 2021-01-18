#importing django needed libraries
from django.urls import path
#importing app and used views
from user import views

#Creating the urls

urlpatterns=[
    path(
        route = 'profile/<str:username>/',
        view = views.profile,
        name = 'profile',
    ),
    path(
        route='profile/<str:username>/update/',
        view=views.profile_update,
        name='profile_update'
    )
    
]