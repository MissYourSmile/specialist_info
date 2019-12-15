#!/usr/bin/env python3
"""管理员注册脚本"""
import sys
import os
import django

import re
import hashlib
import getpass

sys.path.append('../')
os.environ['DJANGO_SETTINGS_MODULE'] = 'specialist_info.settings'
django.setup()

from UserInfo.views import encrypt
from UserInfo.models import UserInfo

def sign_up_admin(username, password):
    """两次加密注册
    - username 用户名 string
    - password 密码 string
    - return bool  True-成功
    """
    password = hashlib.md5(password.encode(encoding='UTF-8')).hexdigest()
    password = encrypt(password)
    user = UserInfo(username=username, password=password, level=True)
    user.save()
    return True

def exist_username(username):
    """检测用户名是否已存在"""
    objs = UserInfo.objects.filter(username=username)
    if objs.exists():
        return False
    return True

def input_username():
    """输入用户名"""
    username = ''
    while True:
        username = input('username: ')
        if re.match(r'^\w{3,16}$', username) is None:
            print('用户名应为3-16位数字、字母、下划线')
            continue
        if not exist_username(username):
            print('用户名已存在')
            continue
        break
    return username

def input_password():
    """输入用户名"""
    password1 = ''
    password2 = ''
    while True:
        password1 = getpass.getpass('password: ')
        if re.match(r'^\w{6,18}$', password1) is None:
            print('用户名应为6-18位数字、字母、下划线')
            continue
        password2 = getpass.getpass('input again: ')
        if password2 != password1:
            print('两次密码不一样')
            continue
        break
    return password1

def main():
    """main"""
    username = input_username()
    password = input_password()
    print('username: ', username)
    print('password: ', password)
    sign_up_admin(username, password)

if __name__ == "__main__":
    main()
