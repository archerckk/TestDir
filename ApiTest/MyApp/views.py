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
def child_json(eid,oid=''):
    res={}
    if eid == 'home.html':
        date = DB_home_href.objects.all()
        # projects=DB_project.objects.all()
        # res = {'hrefs': date,'projects':projects}
        res = {'hrefs': date}
    elif eid == 'project_list.html':
        date=DB_project.objects.all()
        res = {'hrefs': date,'projects':date}

    elif eid=='P_apis.html':
        project = DB_project.objects.filter(id=oid)[0]
        apis=DB_apis.objects.filter(project_id=oid)
        res={'project':project,'apis':apis}

    elif eid == 'P_cases.html':
        project = DB_project.objects.filter(id=oid)[0]
        res = {'project': project}

    elif eid == 'P_project_set.html':
        project = DB_project.objects.filter(id=oid)[0]
        res = {'project': project}

    return res


# 返回子页面
def child(request, eid, oid):
    res = child_json(eid,oid)
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

def project_list(request):
    return render(request, 'welcome.html', {"whichHTML": "project_list.html", "oid": ""})

def delete_project(request):
    id=request.GET['id']

    DB_project.objects.filter(id=id).delete()
    return HttpResponse('')

def add_project(request):
    project_name=request.GET['project_name']
    DB_project.objects.create(name=project_name,remark='',user=request.user.username,other_user='')
    return HttpResponse('')

def open_apis(request,id):
    project_id=id
    return render(request, 'welcome.html', {"whichHTML": "P_apis.html", "oid": project_id})

def open_cases(request,id):
    project_id=id
    return render(request, 'welcome.html', {"whichHTML": "P_cases.html", "oid": project_id})

def open_project_set(request,id):
    project_id=id
    return render(request, 'welcome.html', {"whichHTML": "P_project_set.html", "oid": project_id})

def save_project_set(request,id):
    project_id= id
    name= request.GET['name']
    remark= request.GET['remark']
    other_user=request.GET['other_user']
    DB_project.objects.filter(id=project_id).update(name=name,remark=remark,other_user=other_user)

    return HttpResponse('')