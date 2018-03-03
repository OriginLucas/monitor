#!/usr/bin/python
import psutil

'''
获取内存信息，使用getMethod中getInfo类中的方法实现
将具体的shell命令当做参数传入
'''

def Mem_info():
    memory_info=psutil.virtual_memory()
    swap_info=psutil.swap_memory()
    res={
        'memory_info':memory_info,
        'swap_info':swap_info,
    }
    return res

