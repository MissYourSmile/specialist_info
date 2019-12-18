"""项目信息管理视图"""
from functools import wraps
import json
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from Specialist.models import SpecialistCategory
from Specialist.models import Specialist
from specialist_info.base import base
from .user import check_login

def check_user(fun):
    """检测是否为用户
    用于用户操作页面之前检测，主要为防止直接输入url跳转到无权访问的页面
    - 如果是，则可以直接访问此页面
    - 如果不是，跳转主页
    """
    @wraps(fun)
    def inner(request, *arg, **kwargs):
        level = request.session['login_status']
        if level == '1':
            return fun(request, *arg, **kwargs)
        return redirect('/')
    return inner


@check_login
@check_user
@base
def extract(request, *arg):
    """专家抽取"""
    return render(request, 'extract.html', arg[0])
