from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from MyApp.models import *
import json


# Create your views here.


@login_required
def welcome(request):
    print('进来了')
    return render(request, "home.html")


# 控制不同页面返回不同的数据：数据分发器
def child_json(eid, oid=''):
    res = {}
    if eid == 'home.html':
        date = DB_home_href.objects.all()
        # projects=DB_project.objects.all()
        # res = {'hrefs': date,'projects':projects}
        res = {'hrefs': date}
    elif eid == 'project_list.html':
        date = DB_project.objects.all()
        res = {'hrefs': date, 'projects': date}

    elif eid == 'P_apis.html':
        project = DB_project.objects.filter(id=oid)[0]
        apis = DB_apis.objects.filter(project_id=oid)
        res = {'project': project, 'apis': apis}

    elif eid == 'P_cases.html':
        project = DB_project.objects.filter(id=oid)[0]
        res = {'project': project}

    elif eid == 'P_project_set.html':
        project = DB_project.objects.filter(id=oid)[0]
        res = {'project': project}

    return res


# 返回子页面
def child(request, eid, oid):
    res = child_json(eid, oid)
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


# 删除项目
def delete_project(request):
    id = request.GET['id']

    DB_project.objects.filter(id=id).delete()
    DB_apis.objects.filter(project_id=id).delete()
    return HttpResponse('')


def add_project(request):
    project_name = request.GET['project_name']
    DB_project.objects.create(name=project_name, remark='', user=request.user.username, other_user='')
    return HttpResponse('')


def open_apis(request, id):
    project_id = id
    return render(request, 'welcome.html', {"whichHTML": "P_apis.html", "oid": project_id})


def open_cases(request, id):
    project_id = id
    return render(request, 'welcome.html', {"whichHTML": "P_cases.html", "oid": project_id})


def open_project_set(request, id):
    project_id = id
    return render(request, 'welcome.html', {"whichHTML": "P_project_set.html", "oid": project_id})


def save_project_set(request, id):
    project_id = id
    name = request.GET['name']
    remark = request.GET['remark']
    other_user = request.GET['other_user']
    DB_project.objects.filter(id=project_id).update(name=name, remark=remark, other_user=other_user)

    return HttpResponse('')


# 新增接口
def project_api_add(request, Pid):
    project_id = Pid
    DB_apis.objects.create(project_id=project_id)
    return HttpResponseRedirect('/apis/%s/' % project_id)


# 删除接口
def project_api_del(request, id):
    project_id = DB_apis.objects.filter(id=id)[0].project_id
    DB_apis.objects.filter(id=id).delete()
    return HttpResponseRedirect('/apis/%s/' % project_id)


# 保存备注
def save_bz(request):
    api_id = request.GET['api_id']
    bz_value = request.GET['bz_value']
    DB_apis.objects.filter(id=api_id).update(des=bz_value)  # 这里的des就是描述也就是现在的备注
    return HttpResponse('')


# 获取备注
def get_bz(request):
    api_id = request.GET['api_id']
    bz_value = DB_apis.objects.filter(id=api_id)[0].des
    return HttpResponse(bz_value)


# 保存接口
def Api_save(request):
    # 提取所有数据
    api_id = request.GET['api_id']
    ts_method = request.GET['ts_method']
    ts_url = request.GET['ts_url']
    ts_host = request.GET['ts_host']
    ts_header = request.GET['ts_header']
    ts_body_method = request.GET['ts_body_method']
    api_name = request.GET['api_name']
    # ts_api_body = request.GET['ts_api_body']



    if ts_body_method == '返回体':
        api = DB_apis.objects.filter(id=api_id)[0]
        ts_body_method = api.last_body_method
        ts_api_body = api.last_api_body

    else:
        ts_api_body = request.GET['ts_api_body']

    # 保存数据
    DB_apis.objects.filter(id=api_id).update(
        api_method=ts_method,
        api_url=ts_url,
        api_header=ts_header,
        api_host=ts_host,
        body_method=ts_body_method,
        api_body=ts_api_body,
        name=api_name
    )
    # 返回
    return HttpResponse('success')


def get_api_data(request):
    api_id = request.GET['api_id']
    api = DB_apis.objects.filter(id=api_id).values()[0]
    return HttpResponse(json.dumps(api), content_type='application/json')


def Api_send(request):
    # 提取所有数据
    api_id = request.GET['api_id']
    ts_method = request.GET['ts_method']
    ts_url = request.GET['ts_url']
    ts_host = request.GET['ts_host']
    ts_header = request.GET['ts_header']
    ts_body_method = request.GET['ts_body_method']
    api_name = request.GET['api_name']

    if ts_body_method == '返回体':
        api = DB_apis.objects.filter(id=api_id)[0]
        ts_body_method = api.last_body_method
        ts_api_body = api.last_api_body

        if ts_body_method in ['', None]:
            return HttpResponse('请先选择好请求体编码格式和请求体，再点击Send按钮发送请求')
    else:
        ts_api_body = request.GET['ts_api_body']
        api = DB_apis.objects.filter(id=api_id)
        api.update(last_body_method=ts_body_method, last_api_body=ts_api_body)

    print(ts_body_method)

    # ts_api_body = request.GET['ts_api_body']

    # 发送请求获取返回值

    # 把返回值传递给前端页面
    return HttpResponse('{"code":200}')
