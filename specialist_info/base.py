"""视图
- 主页 home """
from functools import wraps
from django.shortcuts import render
from django.shortcuts import redirect
from .user import check_login

def base(fun):
    """顶层html"""
    @wraps(fun)
    def inner(request, *arg, **kwargs):
        response = {}
        response['level'] = request.session['login_status']
        response['username'] = request.session['username']
        return fun(request, response, *arg, **kwargs)
    return inner

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
@base
def home(request, *arg):
    """主页"""
    return render(request, 'home.html', arg[0])

@check_login
@base
def user(request, *arg):
    """个人中心"""
    return render(request, 'user.html', arg[0])

@check_login
@check_user
@base
def test(request, *arg):
    """用户操作页面测试"""
    return render(request, 'base.html', arg[0])
