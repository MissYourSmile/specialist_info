"""专家信息管理视图"""
from functools import wraps
import json
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from UserInfo.views import check_login
from Specialist.models import SpecialistCategory
from Specialist.models import Specialist
from specialist_info.base import base

# Create your views here.
def check_admin(fun):
    """检测是否为管理员
    用于管理员操作页面之前检测，主要为防止直接输入url跳转到无权访问的页面
    - 如果是，则可以直接访问此页面
    - 如果不是，跳转主页
    """
    @wraps(fun)
    def inner(request, *arg, **kwargs):
        level = request.session['login_status']
        if level == '2':
            return fun(request, *arg, **kwargs)
        return redirect('/')
    return inner

@check_login
@check_admin
@base
def add_specialist(requster, *arg):
    """新增专家信息"""
    if requster.method == 'GET':
        return render(requster, 'add.html', arg[0])
    if requster.method == 'POST':
        name = requster.POST.get('name')
        sex = requster.POST.get('sex')
        birth = requster.POST.get('birth')
        key = requster.POST.get('category2')
        category_obj = SpecialistCategory.objects.get(key=key)
        phone = requster.POST.get('phone')
        email = requster.POST.get('email')
        specialist = Specialist(
            name=name,
            sex=sex,
            birth=birth,
            phone=phone,
            email=email,
            category=category_obj
        )
        specialist.save()

        print(specialist.name)
        return render(requster, 'add.html', arg[0])

def category(requster):
    """获取分类信息"""
    response = {}
    key = requster.GET.get('key')
    if key:
        # 有参数，说明是一级分类改变时调用
        objs = SpecialistCategory.objects.filter(key__contains=key)
        for obj in objs:
            if len(obj.key) == 5:
                response[obj.key] = obj.name
    else:
        # 无参数，说明是页面载入时调用
        objs = SpecialistCategory.objects.all()
        for obj in objs:
            if len(obj.key) == 3:
                response[obj.key] = obj.name
    return HttpResponse(json.dumps(response))
