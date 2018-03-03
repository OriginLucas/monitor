#!/usr/bin/python
import psutil

'''
获取CPU信息，使用getMethod中getInfo类中的方法实现
将具体的shell命令当做参数传入
'''
'''
linux获得参数:(user, nice, system, idle, iowait, irq, softirq, steal, guest, nice)
windows参数:(user, system, idle, interrupt, dpc)

usage得到cpu使用率
'''
def CPU_info():
    cpu_info=psutil.cpu_times()
    cpu_usage=psutil.cpu_percent(interval=1,percpu=False)
    res={
        'cpu_infomation':cpu_info,
        'cpu_usage':cpu_usage,
    }
    return res

a=CPU_info()
print(a)