from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model

from store.accounts.models import Profile

UserModel = get_user_model()


@admin.register(UserModel)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'first_name', 'last_name')