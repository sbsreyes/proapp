#Django needed libraries
from django.shortcuts import render



# Create your views here.
def login(request):
    '''Login and thats the main page'''
    return render(
        request=request,
        template_name='core/login.html',
    )