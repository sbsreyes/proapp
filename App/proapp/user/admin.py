#Django admin imports
from django.contrib import admin
#Models
from user.models import Profile
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'picture')
    read_only_fields = ('created', 'updated')

admin.site.register(Profile, ProfileAdmin)
