# -*-coding:utf-8-*-
from pymysql import *
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:qwer123.@localhost:3306/db_red')

class spider(object):
    def init(self):
        try:
            # 更改为本地数据库信息
            conn = connect(host='localhost', user='root', password='qwer123.', database='db_red', port=3306,
                           charset='utf8mb4')

            cursor = conn.cursor() # 创建游标对象
            # 连接到数据库
            sql = '''
                        create table manzhouliguomen_comment(
                            id int primary key auto_increment,
                            author varchar(255),
                            date varchar(255),
                            score varchar(255),
                            comment text
                        )
                '''
            cursor.execute(sql) # 执行sql语句
            conn.commit() # 提交更改
            print("sql语句执行成功~")
        except:
            pass


    def save_to_sql(sqlf,df):
        pd.read_csv('./岳麓山评论信息.csv')
        df.to_sql('manzhouliguomen_comment', con=engine, index=False, if_exists='append')
        print('数据存储成功~')
df = pd.read_csv('./岳麓山评论信息.csv')
if __name__ == '__main__':
    spiderObj = spider()
    spiderObj.init()
    spiderObj.save_to_sql(df)



