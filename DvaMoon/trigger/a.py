#!/usr/bin/python

from django.core.cache import cache
from django.conf import settings
import json
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

msg=MIMEText('hello,the DvaMoon has checkd the CPU data,and the usage is higher than 90% for 1min,please come on and check what happentd','plain','utf-8')
msg_root=MIMEMultipart('related')

f='18235105708@163.com'
t='zgw747897@gmail.com'
p='wy7478'
msg_root.attach(msg)
msg_root['From']=f
msg_root['To']=t
msg_root['Subject']='wrsndm'
server=SMTP('smtp.163.com',25)
# server.set_debuglevel(1)   #显示发送过程
server.login(f,p)
server.sendmail(f,[t],msg_root.as_string())
server.quit()
