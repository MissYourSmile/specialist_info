"""专家信息模型"""
from django.db import models

# Create your models here.
class SpecialistCategory(models.Model):
    """专家分类
    - 分类key key char 8
    - 分类名 name char 20
    """
    key = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=20)
