"""视图
- 主页 home """
from functools import wraps
from django.shortcuts import render
from UserInfo.views import check_login

def base(fun):
    """顶层html"""
    @wraps(fun)
    def inner(request, *arg, **kwargs):
        response = {}
        response['level'] = request.session['login_status']
        response['username'] = request.session['username']
        return fun(request, response, *arg, **kwargs)
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
