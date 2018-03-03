#!/usr/bin/python
import psutil
'''
获取磁盘使用情况
'''


def Disk_info():
    disk_info = psutil.disk_partitions()
    disk_usage = psutil.disk_usage('/')
    res={
        'disk_infomation':disk_info,
        'disk_usage':disk_usage
    }
    return res

a=Disk_info()
print(a)