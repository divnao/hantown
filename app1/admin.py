from django.contrib import admin

# Register your models here.

from app1.models import UserInfo, Admin


'''用于后台展示该模型类的数据的字段信息,而不是类名.需要注册才能生效'''


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user_name', 'age', 'gender', 'creation_date']


class AdminAdmin(admin.ModelAdmin):
    list_display = ['admin_id', 'user_id', 'role']


admin.site.register(UserInfo, UserInfoAdmin)  # 注册模型类
admin.site.register(Admin, AdminAdmin)

