"""专家信息模型"""
from django.db import models
from django import template


register = template.Library()

# Create your models here.
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
    MALE = 'male'
    FEMALE = 'female'
    SEX = (
        (MALE, u'男'),
        (FEMALE, u'女')
    )
    name = models.CharField(max_length=16)
    sex = models.CharField(max_length=6, choices=SEX)
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
