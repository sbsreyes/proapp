'''importing django needed libraries '''
from django.urls import path
#Importing class based views
from registration.views import SignUpView

urlpatterns = [
    path(
        route = 'signup/',
        view = SignUpView.as_view(),
        name = 'signup'
    )
]