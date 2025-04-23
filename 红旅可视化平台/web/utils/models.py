# -*-coding:utf-8-*-
from django.db import models

class user(models.Model):
    '''用户表'''
    username = models.CharField(verbose_name='用户名',max_length=32)
    password = models.CharField(verbose_name='密码',max_length=64)

