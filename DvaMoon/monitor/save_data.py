#!/usr/bin/python

import queue
from trigger.save_redis import Storage
q=queue.Queue(maxsize=20)
q2=queue.Queue(maxsize=20)
'''
{'cpu_data':'...'  , 'memory_data':'...'   ,   'disk_data':'...' }
'''
def save_place(data,ip):
#只拿到一种数据
    data=data  #字典  usage和infomation
    ip=ip
    con=Storage(data,ip)
    con.save_cpu()  #其他项未写
    con.save_memory()
    con.save_disk()
    print(data)
    if q.qsize()<20:
        q.put(data)
        q2.put(data)
    else :
        q.get()
        q2.get()
        q.put(data)
        q2.put(data)

'''
待改
'''
def put_data():   #实时监控数据
    data=[]
    usage=[]
    infomation=[]
    if q.qsize()>0:
        for i in range(20):
            usage.append(q.get()['cpu_data']['cpu_usage'])
            infomation.append(q.get()['cpu_data']['cpu_infomation'])
        return usage,infomation
    else:
        return False,False

def trigger_data():     #实时监测数据 判断阈值
    usage = []
    infomation = []
    if q2.qsize() > 0:
        for i in range(20):
            usage.append(q2.get()['cpu_data']['cpu_usage'])
            infomation.append(q2.get()['cpu_data']['cpu_infomation'])
        return usage, infomation
    else:
        return False, False