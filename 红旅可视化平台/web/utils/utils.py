# -*-coding:utf-8-*-
import pandas as pd
from sqlalchemy import create_engine

# 连接到数据库
con = create_engine('mysql+pymysql://root:qwer123.@localhost:3306/db_red')
# 读取数据库中爬取到的电影数据
df = pd.read_sql('select * from yuanmingyuan_comment',con=con)
df_1 = pd.read_sql('select * from yuelushan_comment',con=con)
df_2 = pd.read_sql('select * from manzhouliguomen_comment',con=con)
df_3 = pd.read_sql('select * from baotashan_comment',con=con)

# print(df) # 打印数据
# typeList 用于分割逗号

def typeList(type):
    type = df[type].values
    type = list(map(lambda x:x.split(','),type))
    typeList = []
    for i in type:
        for j in i:
            typeList.append(j)
    return typeList
# print(typeList('date'))
def typeList1(type):
    type_1 = df_1[type].values
    type_1 = list(map(lambda x: x.split(','), type_1))
    typeList1 = []
    for i in type_1:
        for j in i:
            typeList1.append(j)
    return typeList1
# print(typeList1('date'))
def typeList2(type):
    type_2 = df_2[type].values
    type_2 = list(map(lambda x: x.split(','), type_2))
    typeList2 = []
    for i in type_2:
        for j in i:
            typeList2.append(j)
    return typeList2
def tyeplist3(type):
    type_3 = df_3[type].values
    type_3 = list(map(lambda x: x.split(','), type_3))
    typeList3 = []
    for i in type_3:
        for j in i:
            typeList3.append(j)
    return typeList3