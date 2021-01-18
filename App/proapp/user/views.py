#Django needed libraries
from django.shortcuts import render, redirect
from django.urls import reverse
#user app models
from user.models import Profile
#Importing forms from user forms
from user.forms import ProfileForm
# Create your views here.

def profile(request, username):
    profile = Profile.objects.get(user=username)
    return render(
        request=request,
        template_name='user/profile.html',
        context={'profile':profile}  
    )

def profile_update(request, username):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        '''Running all validations'''
        if form.is_valid():
            data = form.cleaned_data
            profile.url = data['url']
            profile.bio = data['bio']
            profile.picture = data['picture']
            profile.save()
            ruta = reverse('profile',kwargs={'username':request.user.pk})
            return redirect(ruta)
    else:
        form = ProfileForm()
    return render(
        request = request,
        template_name = 'user/update_profile.html',
        context = {'form':form}
    )


    return render(
        request = request,
        template_name='user/update_profile.html'
    )