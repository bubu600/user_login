#！/usr/bin/env python
# coding=utf-8
# @Time    : 2020/4/5 16:40
# @Author  : Xiaojing
# @Email   : xiao-jing@msn.com
# @File    : send_mail.py
# @Software: PyCharm

import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':
    send_mail(
        '来自www.xiaojing.com的注册通知邮件',
        '欢迎访问www.xiaojing.com，这里是肖景的博客和教程站点，本站专注于Python、Django和机器学习技术的分享！',
        '549268602@qq.com',
        ['bubu600@sina.com'],
    )