#!/usr/bin/env python3

"""生成虚拟专家数据"""
import random
import sys
import os
import django
sys.path.append('../')
os.environ['DJANGO_SETTINGS_MODULE'] = 'specialist_info.settings'
django.setup()

from Specialist.models import SpecialistCategory
from Specialist.models import Specialist

NAMES = []

def init():
    """初始化"""
    f = open('name.txt', 'r')
    names = f.read()
    ret = names.split('   ')
    for i in ret:
        NAMES.append(i)
    f.close()

    Specialist.objects.all().delete()

def make_name():
    """生成随机姓名"""
    max_num = len(NAMES) - 1
    return NAMES[random.randint(0, max_num)]

def make_sex():
    """生成随机性别"""
    sex = ('男', '女')
    return sex[random.randint(0, 1)]

def make_birth():
    """"生成随机日期"""
    year = random.randint(1970, 1999)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return '' + str(year) + '-' + str(month) + '-' + str(day)

def make_category():
    """"生成随机分类"""
    objs = SpecialistCategory.objects.all()
    max_num = len(objs) - 1
    while True:
        obj = objs[random.randint(0, max_num)]
        if len(obj.key) == 3:
            continue
        break
    return obj

def make_phone():
    """生成随机手机号"""
    return '13333345544'


def make_email():
    """生成随机邮箱"""
    return 'specialist@email.com'

def make_data():
    """创建一个伪造数据"""
    obj = Specialist()
    obj.name = make_name()
    obj.sex = make_sex()
    obj.birth = make_birth()
    obj.category = make_category()
    obj.phone = make_phone()
    obj.email = make_email()
    obj.save()

def make_data_set(num):
    """创建 num 个伪造数据"""
    while num:
        make_data()
        num = num - 1

def main():
    """main"""
    init()
    num = input('请输入要生成的数据条数：')
    make_data_set(int(num))

if __name__ == "__main__":
    main()
