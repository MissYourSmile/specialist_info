"""specialist_info URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import user
from . import specialist
from . import base
from . import project

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user.login),
    path('signin/', user.signin),
    path('logout/', user.logout),
    path('', base.home),
    path('user/', base.user),
    path('user/changeusername', user.change_username),
    path('user/changepassword', user.change_password),
    path('specialist/add/', specialist.add_specialist),
    path('specialist/category/', specialist.category),
    path('specialist/list/', specialist.list_specialist),
    path('specialist/view/', specialist.view_specialist),
    path('specialist/del/', specialist.del_specialist),
    path('specialist/update/', specialist.update_specialist),
    path('project/extract/', project.extract),
    path('project/view/', project.view_project),
    path('project/list/', project.list_project),
]
