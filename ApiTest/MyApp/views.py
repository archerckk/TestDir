from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from MyApp.models import *


# Create your views here.
@login_required
def welcome(request):
    print('进来了')
    return render(request, "home.html")

#控制不同页面返回不同的数据：数据分发器
def child_json(eid):
    res={}
    if eid == 'home.html':
        date = DB_home_href.objects.all()
        res = {'hrefs': date}

    return res


# 返回子页面
def child(request, eid, oid):
    res = child_json(eid)
    return render(request, eid, res)


@login_required
def home(request):
    return render(request, "welcome.html", {"whichHTML": "home.html", "oid": ""})


def login(request):
    return render(request, "login.html")


# 开始登录
def login_action(request):
    u_name = request.GET['username']
    p_word = request.GET['password']
    print(u_name, p_word)

    from django.contrib import auth
    user = auth.authenticate(username=u_name, password=p_word)
    print(user)
    if user is not None:
        # 执行正确的动作
        auth.login(request, user)
        request.session['user'] = u_name
        return HttpResponse('成功')
    else:
        # 返回前端告诉用户名/密码不对
        return HttpResponse('失败')


# 注册
def register_action(request):
    u_name = request.GET['username']
    p_word = request.GET['password']
    print(u_name, p_word)

    from django.contrib.auth.models import User

    try:
        user = User.objects.create_user(username=u_name, password=p_word)
        user.save()
        return HttpResponse('注册成功！！')
    except:
        return HttpResponse('注册失败~用户名好像已经存在了~~')


def logout(request):
    from django.contrib import auth
    auth.logout(request)
    return HttpResponseRedirect('/login/')


def diss(request):
    diss_text = request.GET['diss_text']
    if diss_text == "":
        return HttpResponse('空')
    DB_diss.objects.create(user=request.user.username, text=diss_text)
    # 不需要填写提交的内容可以直接通过request.的方式获得，提交的需要用到GET方法['字段名']
    return HttpResponse('')


def api_help(request):
    return render(request, 'welcome.html', {"whichHTML": "help.html", "oid": ""})
