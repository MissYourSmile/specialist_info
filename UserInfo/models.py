"""用户信息数据库模块
1. 用户名 username
2. 密码 password
3. 权限 level
"""

from django.db import models

# Create your models here.
class UserInfo(models.Model):
    """用户信息类
    - 用户名 username 16 char primary key
    - 密码 password 60 char
        前端MD5，后端MD5
    - 权限 level 1 boolean
        True: admin   False: user
    """
    username = models.CharField(max_length=16, primary_key=True)
    password = models.CharField(max_length=32)
    level = models.BooleanField(default=False)
