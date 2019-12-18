"""专家信息管理视图"""
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
def view_specialist(request):
    """查看专家信息"""
    response = {}
    response['specialist'] = Specialist.objects.get(id=request.GET.get('id'))
    return render(request, 'specialist_view.html', response)

@check_login
@check_admin
def del_specialist(request):
    """查看专家信息"""
    objs = Specialist.objects.filter(id=request.GET.get('id'))
    if objs:
        for obj in objs:
            obj.delete()
    return redirect('/specialist/list/')

@check_login
@check_admin
@base
def list_specialist(request, *arg):
    """专家分页列表"""
    page = request.GET.get('page')
    name = request.POST.get('name')
    cate = request.POST.get('category')
    specialist_list = get_specialist_list(name, cate)
    paginator = Paginator(specialist_list, 20)
    try:
        # 用于得到指定页面的内容
        current_page = paginator.page(page)
        # 得到当前页的所有对象列表
        specialists = current_page.object_list
    # 请求页码数值不是整数
    except PageNotAnInteger:
        current_page = paginator.page(1)
        specialists = current_page.object_list
    # 请求页码数值为空或者在URL参数中没有page
    except EmptyPage:
        # paginator.num_pages返回的是页数
        current_page = paginator.page(paginator.num_pages)
        specialists = current_page.object_list
    arg[0]['page'] = current_page
    arg[0]['specialists'] = specialists
    #response.copy(arg[0])
    return render(request, 'specialist_list.html', arg[0])

@check_login
@check_admin
@base
def add_specialist(request, *arg):
    """新增专家信息"""
    if request.method == 'GET':
        return render(request, 'specialist_add.html', arg[0])
    if request.method == 'POST':
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        birth = request.POST.get('birth')
        key = request.POST.get('category')
        category_obj = SpecialistCategory.objects.get(key=key)
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        specialist = Specialist(
            name=name, sex=sex, birth=birth, 
            phone=phone, email=email, category=category_obj
            )
        specialist.save()
        return render(request, 'specialist_add.html', arg[0])

@check_login
@check_admin
def update_specialist(request):
    """修改专家信息"""
    if request.method == 'POST':
        r_id = request.POST.get('id')
        specialist = Specialist.objects.get(id=r_id)
        specialist.phone = request.POST.get('phone')
        specialist.email = request.POST.get('email')
        specialist.save()
        return redirect('/specialist/view?id=' + r_id)
    response = {}
    response['specialist'] = Specialist.objects.get(id=request.GET.get('id'))
    return render(request, 'specialist_update.html', response)


def category(request):
    """获取分类信息"""
    response = {}
    objs = SpecialistCategory.objects.all()
    for obj in objs:
        response[obj.key] = obj.name
    return HttpResponse(json.dumps(response))

def get_specialist_list(name, cate):
    if name or cate:
        if name == '':
            if cate == '0':
                return Specialist.objects.all()
            else:
                return Specialist.objects.filter(category=cate)
        else:
            if cate == '0':
                return Specialist.objects.filter(name__contains=name)
            else:
                return Specialist.objects.filter(name__contains=name).filter(category=cate)
    else:
        return Specialist.objects.all()
