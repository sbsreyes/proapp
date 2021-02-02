#Django libraries
from django.shortcuts import render
#Restricting the access
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def feed(request):
    return render(
            request = request,
            template_name='project/feed.html'
    )