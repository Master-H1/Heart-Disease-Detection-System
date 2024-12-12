from django.contrib import admin
from .models import UserRole, UserRoleManager
# Register your models here.
admin.site.register(UserRole)
admin.site.register(UserRoleManager)
