from django.contrib import admin
from devpro.base.models import User
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['email', 'password']