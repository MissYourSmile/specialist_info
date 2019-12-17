"""用户账户相关视图"""
import hashlib
from functools import wraps
from django.shortcuts import render
from django.shortcuts import redirect
from Specialist.models import UserInfo

# Create your views here.
def check_login(fun):
    """检测登录状态"""
    @wraps(fun)
    def inner(request, *arg, **kwargs):
        login_status = request.session.get('login_status')
        if login_status == '1' or login_status == '2':
            return fun(request, *arg, **kwargs)
        return redirect('/login')
    return inner

def login(request):
    """登录"""
    if request.method == 'GET':
        return render(request, 'login.html', {})

    username = request.POST.get('username')
    password = encrypt(request.POST.get('password'))

    # 判断用户是否存在
    objs = UserInfo.objects.filter(username=username)
    if not objs.exists():
        return render(request, 'login.html', {'no_user': '用户名不存在'})
    # 验证密码
    if objs[0].password != password:
        return render(request, 'login.html', {'error_pass': '密码错误'})

    # 登录成功
    if objs[0].level:
        request.session['login_status'] = '2'
    else:
        request.session['login_status'] = '1'
    request.session['username'] = objs[0].username

    return redirect('/')

@check_login
def logout(request):
    """登出"""
    del request.session['username']
    del request.session['login_status']
    return redirect('/login')

def signin(request):
    """注册"""
    if request.method == 'GET':
        return render(request, 'signin.html')

    username = request.POST.get('username')
    password = encrypt(request.POST.get('password1'))

    # 判断是否已存在
    if UserInfo.objects.filter(username=username).exists():
        return render(request, 'signin.html', {'tip': '用户名'+username+'已存在'})
    userinfo = UserInfo(username=username, password=password)
    userinfo.save()
    return redirect("/login")

@check_login
def change_username(request):
    """更改用户名"""
    if request.method == 'POST':
        username = request.POST.get('username')
        UserInfo.objects.filter(username=request.session['username']).update(username=username)
    return redirect("/logout")

@check_login
def change_password(request):
    """更改密码"""
    if request.method == 'POST':
        password = encrypt(request.POST.get('password1'))
        UserInfo.objects.filter(username=request.session['username']).update(password=password)
    return redirect("/logout")

def encrypt(password):
    """密码加密 MD5
    - 输入： 密码原文
    - 输出： 加盐 hash 后的结果
    """
    salt = 'fsldkfjlksdfjoweafafs'
    saltpass = salt + password
    ret = hashlib.md5(saltpass.encode(encoding='UTF-8')).hexdigest()
    return ret
