# -*-coding:utf-8-*-
from pymysql import *
# 连接数据库
''' ！！！改为自己本地的数据库↓'''
conn = connect(host='localhost',user='root',password='qwer123.',database='db_red',port=3306)
cursor = conn.cursor()

# 定义querys函数方法
def querys(sql,params,type='no_select'):
    params = tuple(params)
    cursor.execute(sql,params)
    if type != 'no_select':
        data_list = cursor.fetchall()
        conn.commit()
        return data_list
    else:
        conn.commit()
        return '数据库语句执行成功'
