'''importing django needed libraries '''
from django import forms

'''Creating class form update profile '''
class ProfileForm(forms.Form):
    '''We write all form fields '''
    bio = forms.CharField(max_length=700, required=False)
    url = forms.URLField(max_length=200, required=False)
    picture = forms.ImageField()
    
