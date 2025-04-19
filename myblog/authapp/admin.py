from django.contrib import admin
from .models import User

# Register your models here.
class UserInfos(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active','is_staff', 'password')

admin.site.register(User, UserInfos,)
