#!/usr/bin/python
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DvaMoon.settings")# project_name 项目名称
django.setup()
from monitor import models

def get_host_info():
    h=models.Host_info.objects.values_list()
    # print(type(h))
    # for i in h:
    #     print(i[1])
    #     print(type(i[1]))
    return h
get_host_info()