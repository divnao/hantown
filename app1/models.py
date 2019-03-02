import django.utils.timezone
from django.db import models

# Here is my Models


"""UserInfo 模型类"""


class UserInfo(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=10)
    age = models.IntegerField()
    gender = models.BooleanField(default=True)
    creation_date = models.DateField(default=django.utils.timezone.now)

    ''' 相当于java中的toString()重写
    '''
    def __str__(self):
        # 返回部分字段数据, 并编码为utf-8
        return self.user_name


class Admin(models.Model):
    admin_id = models.IntegerField()  # 管理员id
    user_id = models.ForeignKey(UserInfo, on_delete=True)  # 用户id, UserInfo.user_id的外键
    role = models.CharField(max_length=5)  # 用户角色
