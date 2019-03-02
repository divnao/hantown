from django.contrib import admin

# Register your models here.

from app1.models import UserInfo, Admin

admin.site.register(UserInfo)

admin.site.register(Admin)