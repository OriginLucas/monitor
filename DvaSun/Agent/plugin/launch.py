#!/usr/bin/python

from Agent.plugin.Items.CPU import CPU_info
from Agent.plugin.Items.Memory import Mem_info
from Agent.plugin.Items.Disk import Disk_info
import threading
import queue
import time
'''
启动所有的监控项

主要是items里的程序

监控项要无限循环执行，设定循环周期
'''
space_cpu = queue.Queue(maxsize=10)
space_memory = queue.Queue(maxsize=10)
space_disk = queue.Queue(maxsize=10)
class launch_items(object):
    # def __init__(self,interval):
    #     self.interval=interval

    '''
    用于启动各个线程
    '''
    def start_item(self):
        c=threading.Thread(target=self.launch_cpu)
        c.start()
        # c=threading.Thread(target=self.launch_cpu)
        # d=threading.Thread(target=self.launch_disk)
        # m=threading.Thread(target=self.launch_mem)
        # # col=threading.Thread(target=self.collect_data)
        # items_list=[c,d,m]
        # for i in items_list:
        #     i.start()
    '''
    用于将各个线程中的数据收集起来
    发送到前段
    被trigger收集
    '''
    def collect_cpudata(self):
        cpu_data=[]
        while True:
            res=self.launch_cpu()       
            # print(res)
            return res

    def collect_memdata(self):
        memory_data = []
        while True:
            res = self.launch_mem()
            print(res)
            return res

    def collect_diskdata(self):
        disk_data = []
        while True:
            res = self.launch_disk()
            print(res)
            return res

        #     cpu_data.clear()
        #     long=space_cpu.qsize()
        #     print(long)
        # # for i in range(3):
        # #     time.sleep()
        # #     if not self.space_cpu.empty():
        #     if long >0:
        #         print('ojbk1')
        #         for i in range(space_cpu.qsize()):
        #             print('ojbk2')
        #     # self.space_cpu.get()
        #             cpu_data.append(space_cpu.get())
        #             print('ojbk')
        #
        #     else:
        #         print('wrsndm')
        #     # memory_data.append(self.space_memory.get())
        #     # disk_data.append(self.space_disk.get())
        #     return cpu_data

            # return cpu_data,memory_data,disk_da
    def launch_cpu(self):
        cpu_list=[]
        for i in range(20):
            cpu_list.append(CPU_info())
        print(cpu_list)
        return cpu_list


        # while True:
        #     res=CPU_info()  #返回字典  包含cpu的两种信息
        #     time.sleep(0.1)
        #     if not space_cpu.full():
        #         space_cpu.put(res)
        #     else:
        #         space_cpu.get()
        #         # print(a["cpu_usage"])
        #         # self.space_cpu.put(res)
        #     print(space_cpu.qsize())
            # time.sleep(1)
            # print(res)
            # print(self .space_cpu)

    def launch_mem(self):
        while True:
            res=Mem_info()
            if space_memory.empty():
                space_memory.put(res)
            else:
                space_memory.get()
                space_memory.put(res)
            time.sleep(1)
    def launch_disk(self):
        while True:
            res=Disk_info()
            if space_disk.empty():
                space_disk.put(res)
            else:
                space_disk.get()
                space_disk.put(res)
            time.sleep(1)
