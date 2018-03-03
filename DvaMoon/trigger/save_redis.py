#!/usr/bin/python

import redis
from monitor import models
from trigger.manager_redis import Manager

'''
data的形式
{'cpu_data':'...', 'memory_data':'...'   ,   'disk_data':'...' }
'''
'''
作用：存到redis中  拿到agent的ip
'''
class Storage(object):
    def __init__(self,data,ip):
        self.data=data
        self.ip=ip
        self.pool=redis.ConnectionPool(host='172.196.70.3', port=6379)
        # self.host_id = models.Host_info.objects.filter(ip=self.ip)  ####   得到主机ID
        self.host_id = 1

    def save_cpu(self):
        if self.data['cpu_data']:    #判断有这一个监控项项
            self.cpu=self.data['cpu_data']
            user_name = str(self.host_id) + '_cpu_user'
            system_name = str(self.host_id) + '_cpu_system'
            idel_name = str(self.host_id) + '_cpu_idel'
            interrupt_name = str(self.host_id) + '_cpu_interrupt'
            dpc_name = str(self.host_id) + '_cpu_dpc'
            usage_name=str(self.host_id)+'_cpu_usage'
            usage=self.cpu['cpu_usage']
            infomation_user = self.cpu['cpu_infomation'][0]         #save要做的工作  将堆在一起的数据分开
            infomation_system = self.cpu['cpu_infomation'][1]
            infomation_idel = self.cpu['cpu_infomation'][2]
            infomation_interrupt = self.cpu['cpu_infomation'][3]
            infomation_dpc = self.cpu['cpu_infomation'][4]
            obj=redis.Redis(connection_pool=self.pool)
            obj.lpush(usage_name,usage)
            obj.lpush(user_name,infomation_user)
            obj.lpush(system_name,infomation_system)
            obj.lpush(idel_name,infomation_idel)
            obj.lpush(interrupt_name,infomation_interrupt)
            obj.lpush(dpc_name,infomation_dpc)
            Manager(usage_name)
            Manager(user_name)
            Manager(system_name)
            Manager(idel_name)
            Manager(interrupt_name)
            Manager(dpc_name)
        else:                             #没有就算了
            return False



    '''
    待补完
    '''
    def save_memory(self):
        if self.data['memory_data']:
            self.memory=self.data['memory_data']


    def save_disk(self):
        if self.data['disk_data']:
            self.disk=self.data['disk_data']

