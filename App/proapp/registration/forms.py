from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#Importing profile model
from user.models import Profile
class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text = "Campo Requerido")
    #Definiendo la clase meta
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError("Email ya se encuentra registrado")
        return email
    
    def save(self):
        #Saving the user in the data base
        data = super().clean()
        user = User.objects.create_user(
            username = data['username'],
            password = data['password2'],
            email = data['email']
        )
        #Creating profile
        p = Profile(user = user)
        p.save()
