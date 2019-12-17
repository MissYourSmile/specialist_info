"""专家信息模型"""
from django.db import models
from django import template


register = template.Library()

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

class Specialist(models.Model):
    """专家信息
    - 姓名： name char 16
    - 性别: sex char 1
    - 出生年月： birth date
    - 手机号: phone char 11
    - 邮箱: email char 30
    - 类别: category ForeignKey SpecialistCategory.key
    - 照片: photo char 100
    """
    name = models.CharField(max_length=16)
    sex = models.CharField(max_length=6)
    birth = models.DateField()
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=30)
    category = models.ForeignKey('SpecialistCategory', on_delete=models.PROTECT)

class SpecialistCategory(models.Model):
    """专家分类
    - 分类key key char 8
    - 分类名 name char 20
    """
    key = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=20)

    @register.simple_tag
    def get_category1(self):
        return SpecialistCategory.objects.get(key=self.key[:2])

class Project(models.Model):
    """项目表
    - 项目名称 name char 30
    - 创建者 owner foreignkey UserInfo
    """
    name = models.CharField(max_length=30)
    owner = models.ForeignKey('UserInfo', on_delete=models.CASCADE)

class ProjectSpecialist(models.Model):
    """项目-专家表
    - 项目id pid ForeignKey Project
    - 专家id sid FroeignKey Specialist
    - 评价 comment char 100
    """
    pid = models.ForeignKey('Project', on_delete=models.CASCADE)
    sid = models.ForeignKey('Specialist', on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
