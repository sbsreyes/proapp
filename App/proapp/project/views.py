#Django libraries
from django.shortcuts import render

# Create your views here.
def feed(request):
    return render(
            request = request,
            template_name='project/feed.html'
    )