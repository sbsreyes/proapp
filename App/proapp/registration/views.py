#Django needed libraries
from django.shortcuts import render
from django.urls import reverse_lazy
# Importing forms
from django.contrib.auth.forms import UserCreationForm
from registration.forms import UserCreationFormWithEmail
from django import forms
#Importing classed based views
from django.views.generic import CreateView

class SignUpView(CreateView):
    '''Modifying the normal creation form '''
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    #Using manual created form
    def get_form(self, form_class = None):
        '''setting up the forms '''
        form = super(SignUpView, self).get_form()
        #adding the widgets for the form
        form.fields['username'].widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs = {'class':'form-control', 'placeholder':'Dirección de email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs = {'class':'form-control', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs = {'class':'form-control', 'placeholder':'Repite tu contraseña'})
        return form

    #Damos retroalimentacion al usuario
    def get_success_url(self):
        return reverse_lazy('login') + '?register'
