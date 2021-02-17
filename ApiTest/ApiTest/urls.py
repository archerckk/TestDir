"""ApiTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from MyApp.views import *
from django.conf.urls import url

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r"^welcome/$", welcome),#获取菜单
    url(r"^home/$", home),#进入主页
    url(r"^login/$", login),#进入登录页
    url(r"^child/(?P<eid>.+)/(?P<oid>.*)/$",child),#加载子页面
    url(r"^login_action/$",login_action),#登录
    url(r"^register_action/$",register_action),#注册
    url(r"^accounts/login/$",login),#未登录跳转注册
    url(r"^logout/$",logout),#退出登录
    url(r"^diss/$",diss),#退出登录
    url(r"^help/$",api_help),#进入帮助文档
    url(r"^project_list/$",project_list),#项目列表
    url(r"^delete_project/$",delete_project),#删除项目
    url(r"^add_project/$",add_project),#新增项目
    url(r"^apis/(?P<id>.*)/$",open_apis),#进入接口库
    url(r"^cases/(?P<id>.*)/$",open_cases),#进入用例设置
    url(r"^project_set/(?P<id>.*)/$",open_project_set),#进入项目设置
    url(r"^save_project_set/(?P<id>.*)/$",save_project_set),#进入项目设置

]
