from django.contrib import admin

from .models import User, Profile


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'date_of_birth', 'nickname']


admin.site.register(User)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'introduce']


admin.site.register(Profile)
