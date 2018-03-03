#!/usr/bin/python

from Agent.plugin.launch import launch_items
import json
import threading
from Agent.plugin.trans import Trans_data


class collect_api(object):
    cpu = Trans_data('CPU_info')
    memory = Trans_data('Mem_info')
    disk = Trans_data('Disk_info')
    def col_cpu(self):
        t1 = threading.Thread(target=self.cpu.save_place)
        t1.start()
        data=self.cpu.get_data()
        return data

    def col_memory(self):
        t1 = threading.Thread(target=self.memory.save_place)
        t1.start()
        data = self.memory.get_data()
        return data

    def col_disk(self):
        t1 = threading.Thread(target=self.disk.save_place)
        t1.start()
        data = self.disk.get_data()
        return data

class get_totalInfo(object):
    def __init__(self):
        pass
        # self.post_info()
    '''
    暂时拿到的是json格式的数据
    queue队列
    放到字典中
    '''
    def post_info(self):
        '''  queue无法json序列化
            直接得到到queue
        '''
        # cpu_data=launch_items().collect_data()
        cpu_data=launch_items().collect_cpudata()
        # memory_data=launch_items().collect_memdata()
        # disk_data=launch_items().collect_diskdata()
        dic={
            'cpu_data':cpu_data,
            # 'memory_data':memory_data,
            # 'disk_data':disk_data,
        }
        return dic

# a=get_totalInfo().post_info()
'''
直接全部发送，省事↑
'''


'''
等解决。。。

放弃此方法（暂时）
'''
# class cpu_info(get_totalInfo):
#     def __init__(self):
#         self.post_info()
#     def post_info(self):
#        super(cpu_info,self).post_info()
#        cpu_data=self.cpu_data
#        return cpu_data