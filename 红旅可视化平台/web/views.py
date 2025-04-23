from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from web.utils import query
from web.utils.getTableData import *
from django import forms
from web.utils import models

class LoginForm(forms.Form):
    username = forms.CharField(
        label='用户名',
        widget=forms.TextInput(attrs={'class':"form-control",'placeholder':"请输入用户名~"})
    )
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"请输入密码~"})
    )



# 登录页面及登录逻辑实现
def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request,'login.html',{"form":form})
    form = LoginForm(data=request.POST)
    # 对账号密码进行校验
    if form.is_valid():
        # {"userame":'xxx',"password":'xxx'}
        # print(form.cleaned_data)
        # 去数据库校验数据
        user_object = models.user.objects.filter(username=form.cleaned_data['username'],
                                   password=form.cleaned_data['password']).first()
        if user_object:
            return render(request,'index.html')
        else:
            return render(request, 'error.html', {'message': '用户邮箱或密码输入错误'})


def all_request(request):
    return render(request,'login.html')


def index(request):
    return render(request,"index.html")
def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    elif request.method == 'POST':
        form = dict(request.POST) # 判断第一次输入密码和第二次是否相同
        if form['password'] != form['passwordChecked']:
            return render(request,'error.html',{'message':'两次输入密码不同，请重新输入~'})
        def filter_fn(item):
            return form['email'] in item
        # 对users在数据库中进行查询
        users = query.querys('select * from web_user', [], 'select')
        filter_list = list(filter(filter_fn, users))
        if len(filter_list):
            return render(request, 'error.html', {'message': '该用户已被注册~'})
        else:
            # 将新注册的数据存储到数据库
            query.querys('insert into web_user(username,password) values(%s,%s)', [form['email'], form['password']])
            return redirect('/login')

def table(request):
    return render(request,'table.html')
def table_1(request):
    data = getTableData()
    data_1 = getTableData1()
    return render(request,
                  'table_1.html',
                  {'tableData':data,'tableData_1':data_1},
                  )
def table_2(request):
    data_2 = getTableData2()
    data_3 = getTableData3()
    return render(request,'table_2.html',{'tableData':data_2,'tableData_1':data_3})

def cor_analysis(request):
    return render(request,'cor_analysis.html')

def qinggan_analysis(request):
    return render(request,'qinggan_analysis.html')


def comment_cw(request):
    return render(request,'comment_cw.html')

def home(request):
    return render(request,'index.html')

